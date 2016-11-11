#!/usr/bin/env python
# -*- coding: utf-8 -*-

# client_insert_pkg_centos.py: obtain and insert CentOS packages update type
#
# Copyright (C) 2014 Politecnico di Torino, Italy
#                    TORSEC group -- http://security.polito.it
#
# Author: Tao Su <tao.su@polito.it>
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

import time
import sys
import os
import getopt
import string
import datetime
from dateutil.relativedelta import relativedelta

from lxml.html import *
import urllib
import pycassa
import insert_rpm_library

import utils

CENTOSANNOUNCE = "http://lists.centos.org/pipermail/centos-announce/"
CENTOSCRANNOUNCE = "http://lists.centos.org/pipermail/centos-cr-announce/"

def usage():
    print "python client_insert_pkg_centos.py {-h help | -K keyspace | -l log-file | -c cassandra-url | -d distribution | -b base-directory | -p package-list-file}"

def getZeroDayUpdates(url_level3):
    global packageUpdateType
    emailContent = fromstring(urllib.urlopen(url_level3).read())
    content = emailContent.xpath("//html/body/pre")
    links = emailContent.xpath("//html/body/pre/a/@href")
    length_links=len(links)

    for i in content:
        packages = i.xpath("./text()")
        counter = 0
        for j in packages:
            list_level2 = j.split()
            upstream = links[counter]
            if 'RHEA' in upstream :
                updateType = 'enhancement'
            elif 'RHBA' in upstream :
                updateType = 'bugfix'
            elif 'RHSA' in upstream :
                updateType = 'security'

            for m in list_level2:
                if '.src.rpm' in m:
                    packageUpdateType[m] = updateType
            if counter >= length_links-1:
                break
            else:
                counter+=1

def getSourcePackages(url_level3):
    global packageUpdateType
    emailContent = fromstring(urllib.urlopen(url_level3).read())
    content = emailContent.xpath("//html/body/pre/text()")
    if "security advisory" in content[0].lower():
        updateType = 'security'
    elif "bugfix advisory" in content[0].lower():
        updateType = 'bugfix'
    elif "enhancement advisory" in content[0].lower():
        updateType = 'enhancement'

    for i in content:
        list_level1 = i.split('\n')
        for j in list_level1:
            list_level2 = j.split()
            for m in list_level2:
                 if '.src.rpm' in m:
                     packageUpdateType[m] = updateType
        else:
            continue

def getEmails(url_level2, keyword):
    print "Searching update type in " + url_level2
    keyword = keyword.lower()
    tree_threads = fromstring(urllib.urlopen(url_level2).read())
    thread = tree_threads.xpath("//html/body/ul/li")
    tempurl = url_level2.replace('thread.html', '')
    for i in thread:
        emails = i.xpath("./a/text()")
	for j in emails:
            j = j.lower()
            if 'update' in j and keyword in j and not 'zero day' in j :
                emailAddress = i.xpath("./a/@href")[0]
                getSourcePackages(tempurl+emailAddress)
            elif 'update' in j and keyword in j and 'zero day' in j:
                emailAddress = i.xpath("./a/@href")[0]
                getZeroDayUpdates(tempurl+emailAddress)

def getThreads(url_level1, keyword_list):
    tree = fromstring(urllib.urlopen(url_level1).read())
    threads = tree.xpath("//html/body/table/tr")
    for i in threads:
        thread = i.xpath("./td[2]/a[1]/@href")
        for j in thread:
            for keyword in keyword_list:
                getEmails(url_level1+j, keyword)

def insertCentosDB(DBlink, pkg_name, pkg_version, distname, updateType):
    global counterNumber
    DBlink.insert(pkg_name + '-' + distname, { pkg_version : { 'name' : pkg_name + '-' + pkg_version } } );
    DBlink.insert(pkg_name + '-' + distname, { pkg_version : { 'updatetype': updateType } } );
    print "[%s/%s] %s is inserted into PackagesHistory" %(counterNumber,totNumber,pkg_name)
    counterNumber = counterNumber+1


def main(argv):
    global flog
    global packageUpdateType
    global counterNumber,totNumber

    counterNumber = 1
    packageUpdateType = {}
    cassandra_url='localhost:9160'
    packages_dir = ""
    packages_list = ""
    keyspace = "PackagesDB"
    distribution = "CentOS7"
    logfile = "/srv/ra/db/logs/cassandra_err.log"
    base_directory = '/srv/ra/'
    counterNumber = 1
    packagesdb = {}

    try:
        opts, args = getopt.getopt(argv, "hK:l:c:d:b:p:f:", ["help", "keyspace=", "log-file=", "cassandra-url=", "distribution=", "base-directory=","package-dir=","package-list="])
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
            distribution = arg.replace('-', ' ')
        elif opt in ("-b", "--base-directory"):
            RABASEDIR = arg
        elif opt in ("-p", "--package-dir"):
            packages_dir = arg
            if packages_dir.endswith('/'):
                packages_dir=packages_dir[:-1]
        elif opt in ("-f", "package-list"):
            package_list = arg

    epoch_dict = utils.get_epoch_dict(packages_dir,package_list)
    DBdistribution = distribution.replace(' ', '')
    emailDistribution = distribution.split('.')[0]
    distributionVersion = emailDistribution.split(' ')[1]

    log_missing_package = []
    with open(logfile,'a+') as f:
	f.seek(0)
	while True:
	    message =  f.readline()
	    if len(message) == 0:
		break
	    if '-pkghistorynotfound-' in message and 'solved' not in message:
		pkg_name = message.split(' ')[4].strip()
		if 'el'+distributionVersion in pkg_name and pkg_name not in log_missing_package:
		    log_missing_package.append(pkg_name)
	    elif '-pkghistorynotfound-' in message and 'solved' in message:
		pkg_name = message.split(' ')[4].strip()
		if pkg_name in log_missing_package:
		    log_missing_package.remove(pkg_name)

    try:
        flog = open(logfile, 'ac');
    except:
        print "Error opening %s for writing " %(logfile)
        sys.exit(2)

    for pkg in log_missing_package:
	current = datetime.datetime.now().date()-relativedelta(months=1)
	pkg_key = pkg.split(':')[0] + '.src.rpm'
	print '\nsearching previous unknown pkgs: ', pkg_key
	pkg_name = '-'.join(pkg.split('-')[:-2])
	while current < datetime.datetime.now().date()+relativedelta(days=1):
	    getEmails(CENTOSANNOUNCE+current.strftime('%Y-%B')+'/thread.html', pkg_name)
	    getEmails(CENTOSCRANNOUNCE+current.strftime('%Y-%B')+'/thread.html', pkg_name)
	    current = current+relativedelta(months=1)
	if pkg_key in packageUpdateType:
	    print "pkg found " + pkg_key
            message = "[%s]: solved -pkghistorynotfound- %s\n" %(datetime.datetime.now(), pkg)
            flog.write(message)
            epoch_dict[pkg.split(':')[0]] = pkg.split(':')[1]

    try :
        (latest, oldest) = utils.get_date_pushed_interval(packages_dir,package_list)
        latest = datetime.datetime.strptime(latest,'%Y-%m-%d %H:%M:%S')
        oldest = datetime.datetime.strptime(oldest,'%Y-%m-%d %H:%M:%S')
        current = oldest-relativedelta(months=1)
        print "\nRetrieving update types in CentOS mailing list..."
        while True:
            if current > latest :
                break
            else:
                getEmails(CENTOSANNOUNCE+current.strftime('%Y-%B')+'/thread.html', emailDistribution)
                getEmails(CENTOSCRANNOUNCE+current.strftime('%Y-%B')+'/thread.html',emailDistribution)
                current = current+relativedelta(months=1)
    except Exception as e:
        message = "[%s]: error -readingmailinglist- %s\n" %(datetime.datetime.now(), e)
        print message
        flog.write(message)
        pass

    try:
        client = pycassa.ConnectionPool(keyspace, [CASSANDRA_URL], pool_timeout = -1, max_retries = -1)
    except pycassa.TException, tx:
        message = "[%s]: error -dbserverconnfailed- %s\n" %(datetime.datetime.now(), CASSANDRA_URL)
        flog.write(message)
        flog.close()
        sys.exit(2)

    column_path_packagesh = pycassa.ColumnFamily(client,'PackagesHistory')

    totNumber=len(epoch_dict)

    for pkg in epoch_dict:
        pkg_key = pkg + '.src.rpm'
        if pkg_key not in packageUpdateType:
            print 'searching missing pkg: ', pkg_key
            packageUpdateType[pkg + '.src.rpm'] = 'unknown'
            current = utils.get_pkg_datetime(packages_dir, package_list, pkg_key)
            pkg_name = '-'.join(pkg.split('-')[:-2])
            getEmails(CENTOSANNOUNCE+current.strftime('%Y-%B')+'/thread.html', pkg_name)
            getEmails(CENTOSCRANNOUNCE+current.strftime('%Y-%B')+'/thread.html', pkg_name)

    for pkg in epoch_dict:
        epoch_prefix = ''
        if len(epoch_dict[pkg]) > 0:
                epoch_prefix = epoch_dict[pkg] + ':'

        pkg_name = '-'.join(pkg.split('-')[:-2])
        pkg_version = epoch_prefix + '-'.join(pkg.split('-')[-2:])
        update_type = packageUpdateType[pkg + '.src.rpm']
        if update_type == 'unknown':
            message = "[%s]: error -pkghistorynotfound- %s:%s\n" %(datetime.datetime.now(), pkg,epoch_dict[pkg])
            flog.write(message)

        try:
            insertCentosDB(column_path_packagesh, pkg_name, pkg_version, DBdistribution, update_type)
        except pycassa.NotFoundException, TException:
            message = "[%s]: error -dbinserterror- %s\n" %(datetime.datetime.now(), pkg)
            flog.write(message)
            flog.close()
            sys.exit(2)

    flog.close()

if __name__ == '__main__':
	main(sys.argv[1:])
