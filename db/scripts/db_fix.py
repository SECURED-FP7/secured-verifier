#! /usr/bin/python

# db_fix.py: tool to fix the database
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
keyspace = "PackagesDB"
cassandra_url='130.192.1.104:9160'
client = pycassa.ConnectionPool("PackagesDB",[cassandra_url],)
clientb = pycassa.ConnectionPool('BodhiDB',[cassandra_url],)
cf = pycassa.ColumnFamily(client, 'PackagesHistory')
cf_bodhi = pycassa.ColumnFamily(clientb, 'Bodhi')

for item in cf.get_range():
    if '-Fedora' in item[0]:
        for version in item[1].keys():
            if item[1][version]['updatetype'] != 'updates':
                continue

            try:
                source_pkg = '-'.join(item[0].split('-')[:-1])
                if ':' in version:
                    version = version.split(':')[1]
                updatetype = cf_bodhi.get('update', super_column = source_pkg + '-' + version)['updatetype']
                cf.insert(item[0], {version: {'updatetype' : updatetype}})
            except pycassa.NotFoundException as e:
                cf.remove(item[0], None, version)
            except Exception as e:
                print e
