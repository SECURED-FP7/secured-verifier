#!/usr/bin/env python
# -*- coding: utf-8 -*-

# connection.py: query the database
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

from util import *
import pycassa

class DBConnection(object):
    def __init__(self, keyspace = None, host_list = None):
        self.client = pycassa.ConnectionPool(keyspace, host_list,
                                             pool_timeout = -1,
                                             max_retries = -1)

    def multiget_query(self, row_keys = [], cf_name = None, distro = "Fedora18",
                       include_cf_test = False, sort_reverse = False):
        query_result = {}

        if distro.startswith('Ubuntu') and cf_name is 'PackagesHistory':
            cf_name += 'DEB'

        cf = pycassa.ColumnFamily(self.client, cf_name)
        try:
            query_result = cf.multiget(row_keys, column_reversed = sort_reverse)
        except pycassa.NotFoundException, TException:
            pass

        if include_cf_test == False:
            return query_result

        cf = pycassa.ColumnFamily(self.client, cf_name + '_test')
        try:
            query_result_test = cf.multiget(row_keys,
                                            column_reversed = sort_reverse)
            merge_dict(query_result, query_result_test)
        except pycassa.NotFoundException, TException:
            pass

        return query_result

    def insert(self, platform, cf_name, pathname, digest_type, digest_string):
        query_result = {}

        cf = pycassa.ColumnFamily(self.client, cf_name)
        try:
            cf.insert(platform, {pathname: {digest_type: digest_string}})
        except pycassa.NotFoundException, TException:
                pass
