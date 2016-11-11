#!/usr/bin/env python
# -*- coding: utf-8 -*-

# client_insert_pkg_bodhi.py: obtain and insert Fedora packages update type
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
import string
from datetime import datetime, timedelta
from subprocess import *
from fedora.client import AuthError, ServerError
from fedora.client.bodhi import BodhiClient
from utils import *

MAX_QUERY_LIMIT = 200

def main(argv):
	keyspace = "BodhiDB"
	logfile = "/srv/ra/db/logs/bodhi_err.log"
	BODHI_URL = 'https://admin.fedoraproject.org/updates/'
	CASSANDRA_URL = 'localhost:9160'
	saved_end_date=''
	saved_start_date=''
	release_packages = False
	total_records = 0;
	distribution = 'F14'
	packages_dir = None
	packages_list = None

	try:
		opts, args = getopt.getopt(argv, "hK:l:b:c:rd:p:q:", ["help", "keyspace=", "log-file=", "bodhi-url=", 
				"cassandra-url=", "release-packages=", "distribution=", "packages-dir=", "packages-list="])
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
		elif opt in ("-b", "--bodhi-url"):
			BODHI_URL = arg
		elif opt in ("-c", "--cassandra-url"):
			CASSANDRA_URL = arg
		elif opt in ("-r", "--release-packages"):
			release_packages = True
		elif opt in ("-d", "--distribution"):
			distribution = arg
		elif opt in ("-p", "--packages-dir"):
			packages_dir = arg
                elif opt in ("-q", "--packages-list"):
                        packages_list = arg

	distroupdate = 'update-' + distribution

	try:
		flog = open(logfile, 'ac');
	except:
		print "Error opening %s for writing" %(logfile)
		sys.exit(2)

	try:
		client = pycassa.ConnectionPool(keyspace, [CASSANDRA_URL], pool_timeout = -1, max_retries = -1)
		clientb = pycassa.ConnectionPool("PackagesDB", [CASSANDRA_URL], pool_timeout = -1, max_retries = -1)
	except pycassa.TException, tx:
		message = "[%s]: error -dbserverconnfailed- %s\n" %(datetime.datetime.now(), CASSANDRA_URL)
		flog.write(message)
		flog.close()
		sys.exit(2)

	try:
		bodhi = BodhiClient(BODHI_URL, username='', debug='')
		bodhi.timeout = 500
	except ServerError, e:
		message = "[%s]: error -bodhiserverconnfailed- %s\n" %(datetime.datetime.now(), BODHI_URL)
		flog.write(message)
		flog.close()
		sys.exit(2)

	column_path_packagesh = pycassa.ColumnFamily(clientb, 'PackagesHistory');
	epoch_dict = get_epoch_dict(packages_dir, packages_list)
	date_pushed_interval = get_date_pushed_interval(packages_dir, packages_list)
	saved_end_date = date_pushed_interval[0]
	count = len(epoch_dict.keys())

	while count > 0:
		print "Querying bodhi - distribution: %s, end_date: %s, remaining pkgs: %d" %(distribution, saved_end_date, count)

		data = bodhi.query(release=distribution, 
				status='stable', type_='', bugs='',
				request='', mine='', limit=MAX_QUERY_LIMIT, end_date=str(saved_end_date))

		if data['num_items'] == 0:
			break

		for update in data['updates']:
			for build in update['builds']:
				if build['nvr'] not in epoch_dict:
					continue

				count -= 1
				epoch_prefix = ''
				if len(epoch_dict[build['nvr']]) > 0:
					epoch_prefix = epoch_dict[build['nvr']] + ':'
				epoch_dict[build['nvr']] = None

				pkg_name = '-'.join(build['nvr'].split('-')[:-2])
				pkg_version = epoch_prefix + '-'.join(build['nvr'].split('-')[-2:])

				try:
					column_path_packagesh.insert(pkg_name + '-' + distribution.replace('F', 'Fedora'),
								     {pkg_version: {'name': pkg_name + '-' + pkg_version}})
					column_path_packagesh.insert(pkg_name + '-' + distribution.replace('F', 'Fedora'),
								     {pkg_version: {'updatetype': update['type']}})
				except pycassa.NotFoundException, TException:
					message = "[%s]: error -dbinserterror- %s\n" %(datetime.now(), build['nvr'])
					flog.write(message)
					flog.close()
					sys.exit(2)

		saved_end_date = data['updates'][-1]['date_pushed']
		if date_is_older(saved_end_date, date_pushed_interval[1]):
			break

	if count > 0:
		for pkg in epoch_dict:
			if epoch_dict[pkg] is not None:
				message = "[%s]: error -pkghistorynotfound- %s\n" %(datetime.now(), pkg)
				flog.write(message)
				flog.close()

		sys.exit(2)

	flog.close()

if __name__ == '__main__':
	main(sys.argv[1:])
