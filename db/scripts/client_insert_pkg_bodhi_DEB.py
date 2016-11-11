#!/usr/bin/env python
# -*- coding: utf-8 -*-

# client_insert_pkg_bodhi_DEB.py: obtain and insert Ubuntu packages update type
#
# Copyright (C) 2013 Politecnico di Torino, Italy
#                    TORSEC group -- http://security.polito.it
#
# Author: Giuseppe Baglio <giuseppebag@gmail.com>
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

import getopt
import pycassa
import datetime
import sys
import os
from subprocess import *
import tempfile
import shutil
from shutil import copyfile
from collections import defaultdict
from time import sleep
import time
import itertools
import math
from time import gmtime, strftime
import pdb

dist_filter = ['empty']
tmpdirstr = 'dist_extr_'
row_priority = 'Priority'
#row_arch = 'Architecture'
row_source = 'Source'
row_version = 'Version'
row_filename = 'Filename'

def get_all_files(folder):
    p = Popen(['find ' + folder + ' -type f -name "*.bz2"'], shell = True, stdout = PIPE, stderr = PIPE)
#    p2 = Popen(['grep -v temp'],shell=True,stdin=p.stdout,stdout=PIPE,stderr=PIPE)
#    stdout,stderr = p2.communicate()
    stdout, stderr = p.communicate()

    if len(stderr) > 0:
        return stderr

    if 'empty' in dist_filter:
        return stdout.split('\n')

    result = []
    for filepath in stdout.split('\n'):
        add2result = False
        for uptype in dist_filter:
            key = uptype + "/"
            if filepath.find(key) != -1:
                add2result = True
                break
        if add2result == True:
            result.append(filepath)

    return result

def extractDistFile(fpath):
    p = Popen(['bunzip2 ' + fpath], shell = True, stdout = PIPE, stderr = PIPE)
    stdout, stderr = p.communicate()

    if len(stderr) > 0:
        return [stderr]
    return

def get_elements(fd, package):
    dict_rows = {}
    line = ''

    # priority line
    while not line.startswith(row_priority):
        line = fd.readline()
    dict_rows[row_priority] = line.replace('\n', '').split(':')[-1].strip()

    # source name or version
    keep_reading = True
    while keep_reading == True:
        line = fd.readline()
        if line.startswith(row_source):
            keep_reading = False

        if line.startswith(row_version):
            keep_reading = False

    # it means the package have a source
    if line.startswith(row_source):
        #workaround for packages which have a different version compared to their source package
        if line.find('(') != -1:
            line = line.replace('\n', '').split(':', 1)[-1].split('(')
            source_version = line[-1].replace(')', '').strip()
            dict_rows[row_version] = source_version
            line = line[-2]
        dict_rows[row_source] = line.replace('\n', '').split(':')[-1].strip()

    # the row_version is already inserted when package and source have different version
    if not row_version in dict_rows:
        while not line.startswith(row_version):
            line = fd.readline()
        dict_rows[row_version] = line.replace('\n', '').split(':', 1)[-1].strip()

    # it happens when a package has no source
    if not row_source in dict_rows:
        dict_rows[row_source] = package

    while not line.startswith(row_filename):
        line = fd.readline()
    dict_rows[row_filename] = line.replace('\n', '').split(':')[-1].strip()

    # set line to the last row
    while not line == '\n':
        line = fd.readline()

    return dict_rows

def log(flog, message, mustExit):
    flog.write(message)
    flog.close()
    if mustExit == True:
        sys.exit(2)

def usage():
    print "usage():"
    print "\t-d, --directory : directory containing the Packages.bz2 files"
    print "\t-l, --log-file"
    print "\t-K, --keyspace"
    print "\t-H, --host"
    print "\t-f, --filter filter1|filter2|..."
    print "\t-b, --backupdir"

def main(argv):
    backup_folder = '/srv/ra/dist/backup'
    folder_dist = ''
    logfile = '/srv/ra/db/logs/distinsert_err.log'
    keyspace = "PackagesDB"
    cassandra_url = 'localhost:9160'
    verbose = True
    checkDB = False

    # parse command line
    try:
        opts, args = getopt.getopt(argv, "d:l:H:k:f:b:", ["directory=", "log-file=", "host=", "keyspace=", "filter=", "backupdir="])
    except getopt.GetoptError, ex:
        print ex
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-d", "--directory"):
            folder_dist = arg
        elif opt in ("-l", "--log-file"):
            logfile = arg
        elif opt in ("-H", "--host"):
            cassandra_url = arg
        elif opt in ("-K", "--keyspace"):
            keyspace = arg
        elif opt in ("-f", "--filter"):
            filter_args = arg.split('|')
            global dist_filter
            dist_filter = []
            for el in filter_args:
                dist_filter.append(el)
        elif opt in ("-b", "--backupdir"):
            backup_folder = arg
            if backup_folder.endswith('/'):
                backup_folder = backup_folder[:-1]

    try:
        flog = open(logfile, 'ac');
    except:
            print "Error opening %s for writing" % (logfile)
            sys.exit(2)

    all_files = get_all_files(folder_dist)
    if not isinstance(all_files, list):
        print all_files
        return
    n_tot = len (all_files)
    n_current = 1
    n_count = 0
    pkgstat = {'newpackage':0, 'updates':0, 'security':0}
    for distfile_path in all_files:
        if n_current == n_tot:
            pass

#        n_missing_pkg = 0
        print '\nAnalyzing %d of %d files: "%s"' % (n_current, n_tot, distfile_path)
        if distfile_path == '':
            continue
        if distfile_path.find('.temp') != -1:
            print "Temporary file: skipping..."
            continue

        tmpdir = tempfile.mkdtemp(prefix = tmpdirstr)
        mydir = os.getcwd()
        os.chdir(tmpdir)

        # copy file and extract
        copy_filename = 'Packages.bz2'
        try:
            copyfile(distfile_path, copy_filename)
        except Exception, ex:
            message = "[%s]: error -filecopyerror- %s\n" % (datetime.datetime.now(), ex)
            flog.write(message)
            continue

        extr_out = extractDistFile(copy_filename)
        if isinstance(extr_out, list):
            message = "[%s]: error -packagesfilextraction- %s\n" % (datetime.datetime.now(), extr_out)
            flog.write(message)
            continue

        filelist = os.listdir(".")
        if not 'Packages' in filelist:
            message = "[%s]: error -packagesfilextraction- content%s\n" % (datetime.datetime.now(),)
            flog.write(message)
            flog.close()
            sys.exit(2)

        try:
            fd = open('Packages', 'r')
        except:
            message = "[%s]: error -openpkgfilerror- %s\n" % (datetime.datetime.now(), tmpdir)
            flog.write(message)
            flog.close()
            sys.exit(2)

        try:
            client = pycassa.ConnectionPool(keyspace, [cassandra_url], pool_timeout = -1, max_retries = -1)
        except:
            message = "[%s]: error -dbserverconnfailed- %s\n" % (datetime.datetime.now(), cassandra_url)
            flog.write(message)
            fd.close()
            flog.close()
            sys.exit(2)

        column_path_packagesh = pycassa.ColumnFamily(client, 'PackagesHistoryDEB')
        # for update_type it's not possible to do:
        #     distfile_path.split('/')[-2].split('-')[-4]
        index = distfile_path.find('dist') + len('dist') + 2
        distro = distfile_path[index:].split('/')[0]
        if distro.find('-') != -1:
            update_type = distro.split('-')[-1]
            distro = distro.split('-')[-2]
        else:
            update_type = 'newpackage'

        #backup file
        if os.path.exists(backup_folder):
            try:
                backupfile = backup_folder + '/Packages-' + strftime("%Y%m%d_%H%M", gmtime()) + '.bz2'
                copyfile(distfile_path, backupfile)
            except Exception, ex:
                message = "[%s]: error -savebackupcopyerror- %s\n" % (datetime.datetime.now(), ex)
                flog.write(message)
        else:
            message = "[%s]: error -backupdirnotexist- %s\n" % (datetime.datetime.now(), backup_folder)
            flog.write(message)

        while True:
            line = fd.readline()
            if line == '':#end of file
                break
            if not line.startswith('Package'):
                continue

            dicitonary = get_elements(fd, line.split(':')[-1].strip())
            if not row_source in dicitonary:
                message = "[%s]: error -missingkeyerror- %s in %s\n" % (datetime.datetime.now(), row_source , dicitonary)
                flog.write(message)
                continue

            n_count = n_count + 1
            pkgstat[update_type] += 1
            key = dicitonary[row_source] + '-' + distro
#            # check DB
#            try:
#                db_dict = column_path_packagesh.get(key)
#                if not dicitonary[row_version] in db_dict and checkDB == True:
#                    n_missing_pkg = n_missing_pkg + 1
#                    message = "[%s]: error -missingDBversionerror- key = %s, distro = %s, update_type = %s, filename = %s\n" % (datetime.datetime.now(), key, distro, update_type, dicitonary[row_filename])
#                    flog.write(message)
#            except:
#                n_missing_pkg = n_missing_pkg + 1
#                if checkDB:
#                    message = "[%s]: error -missingDBkeyerror- key = %s, distro = %s, update_type = %s, filename = %s\n" % (datetime.datetime.now(), key, distro, update_type, dicitonary[row_filename])
#                    flog.write(message)
            column_path_packagesh.insert(key, { dicitonary[row_version] : { 'updatetype' : update_type } })
            column_path_packagesh.insert(key, { dicitonary[row_version] : { 'priority' : dicitonary[row_priority] } })

        fd.close()
        os.chdir(mydir)
        shutil.rmtree(tmpdir)
        n_current = n_current + 1

    if verbose:
        print '\n\tTotal num of packages processed: %d' % (n_count)
        print '\t\tnewpackage: %d\n\t\tupdates: %d\n\t\tsecurity: %d' % (pkgstat['newpackage'], pkgstat['updates'], pkgstat['security'])
    return

if __name__ == '__main__':
    print os.path.basename(__file__) + ': execution started.'
    main(sys.argv[1:])
