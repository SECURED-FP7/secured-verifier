#!/usr/bin/env python
# -*- coding: utf-8 -*-

# client_insert_pkg_http.py: obtain and insert Fedora/EPEL packages update type
#
# Copyright (C) 2014 Politecnico di Torino, Italy
#                    TORSEC group -- http://security.polito.it
#
# Author: Roberto Sassu <roberto.sassu@polito.it>
#         Tao Su <tao.su@polito.it>
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

import datetime
import getopt
import lxml.html
import os
import pycassa
import sys
import urllib
import utils


def main(argv):
	keyspace = "PackagesDB"
	logfile = "/srv/ra/db/logs/http_err.log"
	CASSANDRA_URL = 'localhost:9160'
	release_packages = False
	distribution = 'Fedora19'
	packages_dir = None
	packages_list = None

	try:
		opts, args = getopt.getopt(argv, "hK:l:b:c:rd:p:q:", ["help", "keyspace=", "log-file=", "cassandra-url=",
					   "distribution=", "packages-dir=", "packages-list="])
	except getopt.GetoptError:
		usage()
		sys.exit(2)

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt in ("-K", "--keyspace"):
			keyspace = arg
		elif opt in ("-l", "--log-file"):
			logfile = arg
		elif opt in ("-c", "--cassandra-url"):
			CASSANDRA_URL = arg
		elif opt in ("-d", "--distribution"):
			distribution = arg.replace('-', '')
		elif opt in ("-p", "--packages-dir"):
			packages_dir = arg
		elif opt in ("-q", "--packages-list"):
			packages_list = arg

	try:
		flog = open(logfile, 'ac');
	except:
		print "Error opening %s for writing" %(logfile)
		sys.exit(2)

	try:
		client = pycassa.ConnectionPool(keyspace, [CASSANDRA_URL], pool_timeout = -1, max_retries = -1)
	except pycassa.TException, tx:
		message = "[%s]: error -dbserverconnfailed- %s\n" %(datetime.datetime.now(), CASSANDRA_URL)
		flog.write(message)
		flog.close()
		sys.exit(2)

	column_path_packagesh = pycassa.ColumnFamily(client, 'PackagesHistory');
	epoch_dict = utils.get_epoch_dict(packages_dir, packages_list)
	date_pushed_interval = utils.get_date_pushed_interval(packages_dir, packages_list)
	saved_end_date = date_pushed_interval[0]
	count = len(epoch_dict.keys())
	current_page = 1
	updatetype_db = {}

	distribution_id = distribution
	if distribution.startswith('Fedora'):
		distribution_id = distribution.replace('edora', '')
	elif distribution.startswith('EPEL'):
		if distribution in ['EPEL5', 'EPEL6']:
			distribution_id = distribution.replace('EPEL', 'EL-')
		else:
			distribution_id = distribution.replace('EPEL', 'EPEL-')

	while count > 0:
		fedora_url = 'https://bodhi.fedoraproject.org/updates/?status=stable&releases=%s&page=%s' % (distribution_id, current_page)
		print "Querying Fedora Web site - distribution: %s, current page: %d, remaining pkgs: %d" %(distribution_id, current_page, count)

		response_str = urllib.urlopen(fedora_url).read();
		response_dict = yaml.load(response_str);

		accessed_page = response_dict['page'];

		if accessed_page != current_page:
			break

		for item in response_dict['updates']:

			if ' ' in item['title']:
				pkg_list = item['title'].split(' ')
			elif "," in item['title']:
				pkg_list = item['title'].split(',')
			else :
				pkg_list = item['title'].split('?')

			update = item['type']
			if item['date_pushed'] is None:
				date_released = date_pushed_interval[1]
			else:
				date_released = item['date_pushed'].strip()

			for pkg in pkg_list:
				if pkg not in epoch_dict:
					continue

				count -= 1
				updatetype_db[pkg] = update

		if utils.date_is_older(date_released, date_pushed_interval[1]):
			break

		current_page += 1

	for pkg in epoch_dict:
		try:
			update_type = updatetype_db[pkg]
		except:
			update_type = 'unknown'
			message = "[%s]: error -pkghistorynotfound- %s\n" %(datetime.datetime.now(), pkg)
			flog.write(message)

		epoch_prefix = ''
		if len(epoch_dict[pkg]) > 0:
			epoch_prefix = epoch_dict[pkg] + ':'

		pkg_name = '-'.join(pkg.split('-')[:-2])
		pkg_version = epoch_prefix + '-'.join(pkg.split('-')[-2:])

		try:
			column_path_packagesh.insert(pkg_name + '-' + distribution, {pkg_version: {'name': pkg_name + '-' + pkg_version}})
			column_path_packagesh.insert(pkg_name + '-' + distribution, {pkg_version: {'updatetype': update_type}})
		except pycassa.NotFoundException, TException:
			message = "[%s]: error -dbinserterror- %s\n" %(datetime.datetime.now(), pkg)
			flog.write(message)
			flog.close()
			sys.exit(2)

	flog.close()

if __name__ == '__main__':
	main(sys.argv[1:])
