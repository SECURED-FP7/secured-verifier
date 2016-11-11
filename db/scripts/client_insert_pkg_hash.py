#!/usr/bin/env python
# -*- coding: utf-8 -*-

# client_insert_pkg_hash.py: insert digest information to the DB
#
# Copyright (C) 2014 Politecnico di Torino, Italy
#                    TORSEC group -- http://security.polito.it
#
# Author: Roberto Sassu <roberto.sassu@polito.it>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library.  If not, see
# <http://www.gnu.org/licenses/>.

import pycassa

import time
import pprint
import sys
import os
import getopt
import rpm
import string
from subprocess import *
import re
import tempfile
import hashlib
import shutil
import datetime
import time
from collections import defaultdict
import insert_deb_library,insert_rpm_library

insert_modes = [ 'newpackage', 'updates', 'testing' , 'security', 'pyunit' ]

handlers = {'rpm': {'module': insert_rpm_library,
		    'packagesh_cf_name': 'PackagesHistory', 'separator': '-'},
	    'deb': {'module': insert_deb_library,
		    'packagesh_cf_name': 'PackagesHistoryDEB',
		    'separator': '_'}
}

MAX_NUM_RETRIES = 10

#def get_db_pkg(db):
#	sources_key = db.keys()
#	if len(sources_key) == 0:
#		return None
#	arch_keys = db[sources_key[0]].keys()
#	if len(arch_keys) == 0:
#		return None
#	return db[sources_key[0]][arch_keys[0]][0]


def main(argv):
	cassandra_url='localhost:9160'
	packages_dir = ""
	packages_list = ""
	keyspace = "PackagesDB"
	cfsuffix = ""
	distname = "Fedora14"
	distarch = "x86_64"
	logfile = "/srv/ra/db/logs/cassandra_err.log"
	only_package_info = False
	insert_mode = None
	resumepkgnum = '0'

	try:
		opts, args = getopt.getopt(argv, "hK:p:d:l:iI:c:m:z:", ["help", "keyspace=", "package-list=", "package-dir=",
				"log-file=", "only-package-info", "insert-mode=", "cassandra-url=", "resumepkgnum="
				"dist-name="])

	except getopt.GetoptError:          
		usage()                         
		sys.exit(2)      
	
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()                     
			sys.exit()                  
		elif opt in ("-K", "--keyspace"):            
			keyspace = arg
		elif opt in ("-p", "--package-list"):
			packages_list = arg      
		elif opt in ("-d", "--package-dir"):
			packages_dir = arg
			if packages_dir.endswith('/'):
				packages_dir=packages_dir[:-1]
		elif opt in ("-l", "--log-file"):
			logfile = arg
		elif opt in ("-i", "--only-package-info"):
			only_package_info = True
		elif opt in ("-I", "--insert-mode"):
			insert_mode = arg
		elif opt in ("-c", "--cassandra-url"):
			cassandra_url = arg
		elif opt in ("-m", "--resume"):
			resumepkgnum = arg
		elif opt in ("-z", "--dist-name"):
			distname = arg
	
	resumepkgnum = string.atoi(resumepkgnum)

	try:
		flog = open(logfile, 'ac');
	except:
		print "Error opening %s for writing" %(logfile)
		sys.exit(2)

	if insert_mode not in insert_modes:
		message = "[%s]: error -insertmodeunknown-\n" %(datetime.datetime.now())
		flog.write(message)
		flog.close()
		sys.exit(2)

	if insert_mode == 'testing':
		cfsuffix = '_test'
	elif insert_mode == 'pyunit':
		cfsuffix = '_pyunit'

	try:
		fd = open(packages_list, 'r')
	except:
		message = "[%s]: error -packagelistnotfound- %s\n" %(datetime.datetime.now(), packages_list)
		flog.write(message)
		flog.close()
		sys.exit(2)
		
	try:
		client = pycassa.ConnectionPool(keyspace, [cassandra_url], pool_timeout = -1, max_retries = -1)
#		clientB = pycassa.ConnectionPool('BodhiDB', [cassandra_url], pool_timeout = -1, max_retries = -1)
	except:
		message = "[%s]: error -dbserverconnfailed- %s\n" %(datetime.datetime.now(), cassandra_url)
		flog.write(message)
		fd.close()
		flog.close()
		sys.exit(2)

#	column_path_files = pycassa.ColumnFamily(client, 'Files');
	column_path_filestop = pycassa.ColumnFamily(client, 'FilesToPackages' + cfsuffix)
#	column_path_packagesh = pycassa.ColumnFamily(client, 'PackagesHistory' + cfsuffix)
#	column_path_bodhidb = pycassa.ColumnFamily(clientB, 'Bodhi');

	packagedb = {}
	epoch_dict = {}

	for package in fd.readlines():
		if len(package) == 0:
			continue

		package = package.strip()
		package_type = package.split('.')[-1]
		if package_type not in handlers:
			continue

		# FIXME: check if this is needed
#		if package.endswith('deb'):
#			package = package.split(' ')[-1]

		if len(packages_dir) != 0:
			package_path = "%s/%s" %(packages_dir, package)
		else:
			package_path = package

		try:
			# Get: source package name, source package version and release, package arch, errors
			result = handlers[package_type]['module'].getSrcAndArch(package_path)
			if result[3] is not None:
				message = "[%s]: error -accesserror- %s %s\n" %(datetime.datetime.now(), package, result[3])
				flog.write(message)
				continue
		except Exception, ex:
			message = "[%s]: error -accesserror- %s %s\n" %(datetime.datetime.now(), package, ex)
			flog.write(message)
			continue

		# remove the epoch from RPM packages to correctly group them
		pkg_version_release = result[1]
		if package_type == 'rpm':
			epoch = ''
			if ':' in result[1]:
				epoch = result[1].split(':')[0]
				pkg_version_release = result[1].split(':', 1)[1]

			epoch_key = result[0] + '-' + pkg_version_release
			pkg_key = '.'.join(os.path.basename(package).split('.')[:-2])
			if epoch_key not in epoch_dict or pkg_key == epoch_key:
				epoch_dict[epoch_key] = epoch

		# Create the packagedb key in a way that it is easy to split
		packagedb_key = (result[0], pkg_version_release, package_type)
		if packagedb_key not in packagedb:
			packagedb[packagedb_key] = {}
		if result[2] not in packagedb[packagedb_key]:
			packagedb[packagedb_key][result[2]] = set()

		# FIXME: check if ordering packages is needed
		packagedb[packagedb_key][result[2]].add(package)

	totcount = len(packagedb)
	print "\nStarting insert of package's data [%d]...\n" % (totcount)

	pcount = 1
	num_retries = 0
	do_restart = False
	packagedb_iterator = packagedb.iterkeys()
	current_package = None

	while True:
		if not do_restart:
			try:
				package_source_rpm = packagedb_iterator.next()
				num_retries = 0
			except StopIteration:
				break
		else:
			do_restart = False
			num_retries = num_retries + 1
			if num_retries > MAX_NUM_RETRIES:
				message = "[%s]: error -maxnumretriesreached- %s\n" %(datetime.datetime.now(), package_source_rpm)
				flog.write(message)
				break

			message = "[%s]: error -retrysourcepackage- %s\n" %(datetime.datetime.now(), package_source_rpm)
			flog.write(message)
			time.sleep(5)

		if pcount < resumepkgnum:
			pcount = pcount + 1
			continue

		message = "[%d of %d] %s:\n" % (pcount, totcount, package_source_rpm)
		sys.stdout.write(message)

		source_package_type = package_source_rpm[2]
		package_handler = handlers[source_package_type]['module']
		packagesh_cf_name = handlers[source_package_type]['packagesh_cf_name'] + cfsuffix
		column_path_packagesh = pycassa.ColumnFamily(client, packagesh_cf_name)
		packagesh_row = '-'.join([package_source_rpm[0], distname])
		packagesh_super_column = package_source_rpm[1]
		epoch_dict_key = '-'.join(package_source_rpm[0:2])
		if source_package_type == 'rpm' and epoch_dict_key in epoch_dict and len(epoch_dict[epoch_dict_key]) > 0:
			packagesh_super_column = '%s:%s' % (epoch_dict[epoch_dict_key], packagesh_super_column)
		source_package_name = handlers[source_package_type]['separator'].join([package_source_rpm[0], packagesh_super_column])

		if source_package_type != 'rpm' or insert_mode != 'updates':
			try:
				column_path_packagesh.insert(packagesh_row, {packagesh_super_column: {'name' : source_package_name}})
				column_path_packagesh.insert(packagesh_row, {packagesh_super_column: {'updatetype' : insert_mode}})
			except Exception as e:
				message = "[%s]: error -dberror- %s %s\n" %(datetime.datetime.now(), package_source_rpm, e)
				flog.write(message)
				do_restart = True
				continue

		try:
			pkg_history = column_path_packagesh.get(packagesh_row, column_reversed=True)
			pkg_history_versions = pkg_history.keys()
			index_new_pkg_version = pkg_history_versions.index(packagesh_super_column)
		except:
			column_path_packagesh.insert(packagesh_row, {packagesh_super_column: {'name' : source_package_name}})
			column_path_packagesh.insert(packagesh_row, {packagesh_super_column: {'updatetype' : 'unknown'}})
			message = "[%s]: error -pkghistorynotfound- %s\n" %(datetime.datetime.now(), package_source_rpm[0])
			flog.write(message)
			do_restart = True
			continue

		if only_package_info == True:
			pcount = pcount + 1
			sys.stdout.write('.\n')
			continue

		# NOTE: to avoid error messages about existing files, extract in the tmp dir
		#       only packages of one architecture.
		# TODO: check if it is possible to have a library link in the 'all' architecture
		#       that points to a library in a different architecture ('i386' or 'amd64').
		for distarch in packagedb[package_source_rpm]:
			sys.stdout.write(distarch)

			files = []
			links = []
			tmpdir = tempfile.mkdtemp(prefix="rpm_extract.")
			mydir = os.getcwd()
			os.chdir(tmpdir)

			for package in packagedb[package_source_rpm][distarch]:
				if len(packages_dir) != 0:
					package_path = "%s/%s" %(packages_dir, package)
				else:
					package_path = package

				# Extract in tmpdir/package_filename
				destdir = os.path.join(tmpdir, os.path.basename(package))
				# Workaround: cpio does not support destination directory parameter
				os.mkdir(destdir)
				os.chdir(destdir)
				package_files, errors = package_handler.extract_package_files(package_path)
				os.chdir(tmpdir)
				if errors is not None:
					message = "[%s]: error -listpackagefileserror- %s: %s\n" %(datetime.datetime.now(), package, errors)
					flog.write(message)
					continue

				for f in package_files:
					fpathname = os.path.join(os.path.basename(package), os.path.normpath(f))
					if os.path.islink(fpathname):
						links.append(fpathname)
					files.append((os.path.basename(package), fpathname))

			for l in links:
				linkvalue = os.readlink(l)
				for package in packagedb[package_source_rpm][distarch]:
					if linkvalue.startswith('/'):
						resolvedlink = os.path.join(tmpdir, os.path.basename(package), linkvalue[1:])
					else:
						resolvedlink = os.path.join(tmpdir, os.path.basename(package), '/'.join(os.path.dirname(l).split('/')[1:]), linkvalue)

					if os.path.lexists(resolvedlink):
						found_link_dest = True
						os.unlink(l)
						os.symlink(resolvedlink, l)
						break


			do_restart_package_files = False
			num_retries_package_files = 0
			files_iterator = files.__iter__()

			while True:
				if not do_restart_package_files:
					try:
						files_entry = files_iterator.next()
						num_retries_package_files = 0
					except StopIteration:
						break
				else:
					do_restart_package_files = False
					num_retries_package_files = num_retries_package_files + 1
					if num_retries_package_files > MAX_NUM_RETRIES:
						message = "[%s]: error -maxnumretriesreachedpackagefiles- %s\n" %(datetime.datetime.now(), package_source_rpm)
						flog.write(message)
						break

					message = "[%s]: error -retrypackagefiles- %s %s\n" %(datetime.datetime.now(), package_source_rpm, distarch)
					flog.write(message)
					time.sleep(5)

				curpackage, fpathname = files_entry
				fname = os.path.basename(fpathname)

				if not os.path.exists(fpathname):
					if  '.so' in fpathname:
						message = "[%s]: error -extractedfilenotfound- %s %s\n" %(datetime.datetime.now(), package_source_rpm, fpathname)
						flog.write(message)
					continue

				if not os.path.isfile(fpathname):
					continue

				extra = []

				is_link = os.path.islink(fpathname)
				is_elf = False

				sys.stdout.write('.')

				elf_type = 'undefined'
				shared_libraries = []

				fd = open(fpathname, 'rb')
				header = fd.read(4)
				fd.close()
				if header == b'\x7fELF':
					is_elf = True
					p1 = Popen(['readelf', '-h', '-s', '-d', fpathname],stdout=PIPE, stderr=PIPE).communicate()[0]
					for line in p1.split('\n'):
						if len(line) == 0:
							continue
						line_split = line.split()
						if len(line_split) > 1 and line_split[0] == 'Type:':
							elf_type = line_split[1]
						# override elf_type if there is the symbol __libc_start_main (some executables have type DYN, like /sbin/pam_timestamp_check)
						if len(line_split) > 7 and line_split[6] == 'UND' and line_split[7].startswith('__libc_start_main'):
							elf_type = 'EXEC'
						if len(line_split) > 2 and line_split[1] == '(NEEDED)':
							shared_libraries.append(line_split[4][1:-1])

				filetype = 'other'
				if is_link:
					if is_elf and elf_type == 'DYN':
						filetype = 'linklib'
						extra.append(os.path.relpath(os.path.realpath(fpathname), tmpdir))
					else:
						filetype = 'link'
				elif not is_link and is_elf and elf_type in ['EXEC', 'DYN']:
					extra.extend(shared_libraries)
					if elf_type == 'EXEC':
						filetype = 'exe'
					elif elf_type == 'DYN':
						filetype = 'lib'

				if filetype is 'link':
					continue

				try:
					f = open(fpathname)
					h = hashlib.sha1()
					h.update(f.read())
					fdigest = h.hexdigest()
					f.close()
				except IOError, reason:
					message = "[%s]: error -fileioerror- %s %s\n" %(datetime.datetime.now(), package_source_rpm, fpathname)
					flog.write(message)
					do_restart_package_files = True
					continue
				try:
					# Temporaney cleanup
#					column_path_filestop.remove( fdigest , super_column=distname + '-' + distarch, columns = [files[fpathname]] )
#					column_path_filestop.remove( fdigest , super_column='-w-' + distarch)

					if filetype is not "linklib":
#							column_path_files.insert( fdigest , { 'name' : fname } )
						fullpath = '/' + '/'.join(fpathname.split('/')[1:])
						column_path_filestop.insert( fdigest , { distname + '-' + distarch : { 'fullpath' : fullpath } } )

						filestop_pkg_super_column =  'pkg-' + package_source_rpm[0]
						insert_current_pkg_version = False
						current_pkg_version = None

						try:
							current_pkg_version = column_path_filestop.get(fdigest, super_column=distname + '-' + distarch)[filestop_pkg_super_column]
						except:
							insert_current_pkg_version = True

						if current_pkg_version is not None:
							index_current_pkg_version = pkg_history_versions.index(current_pkg_version)
							if index_new_pkg_version < index_current_pkg_version:
								insert_current_pkg_version = True

						if insert_current_pkg_version:
							column_path_filestop.insert(fdigest, {distname + '-' + distarch: {filestop_pkg_super_column: packagesh_super_column}})

						if filetype in ["lib", "exe"]:
							column_path_filestop.insert(fdigest, {distname + '-' + distarch: {'libraries': ','.join(extra)}})
						if filetype is "exe":
							column_path_filestop.insert(fdigest, {distname + '-' + distarch: {'is_executable': 'yes'}})

					if filetype in ["lib", "linklib"]:
						insert_library_list = True

						try:
							item = column_path_filestop.get( fdigest , super_column = distname + "-" + distarch)
							library_list = item['lib_aliases'].split(',')
							if fname not in library_list:
								library_list.append(fname)
							else:
								insert_library_list = False
						except (pycassa.NotFoundException, KeyError):
							library_list = [fname]

						if insert_library_list:
							column_path_filestop.insert( fdigest , { distname + '-' + distarch : { 'lib_aliases' : ','.join(library_list) } } )
				except Exception, ex:
					message = "[%s]: error -dbinserterror- %s %s: %s\n" %(datetime.datetime.now(), package_source_rpm, fpathname, ex)
					flog.write(message)
					do_restart_package_files = True
					continue

			sys.stdout.write('\n')
			os.chdir(mydir)
			try:
				shutil.rmtree(tmpdir)
			except OSError, reason:
				message = "[%s]: error -tmpdirnotremoved- %s %s\n" %(datetime.datetime.now(), package_source_rpm, tmpdir)
				flog.write(message)
		pcount = pcount + 1

	flog.close()
	fd.close()
if __name__ == '__main__':
	main(sys.argv[1:])
