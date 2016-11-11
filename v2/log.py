#!/usr/bin/env python
# -*- coding: utf-8 -*-

# log.py: display log messages
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

import sys

verbose_mode = False
fdlog = None


# TODO: make a class?
def set_verbose_mode(mode):
	global verbose_mode
	verbose_mode = mode

def log_init(logfile = None):
	global fdlog

	if fdlog != None:
		return

	if logfile == None:
		fdlog = sys.stdout
	else:
		try:
			fdlog = open(logfile, 'wc')
		except:
			sys.stdout('Error opening %s' %(logfile))
			sys.exit(2)

def log_end():
	if fdlog != None and fdlog != sys.stdout:
		fdlog.close()

def log_message(message = None):
	try:
		fdlog.write(message)
		fdlog.write('\n')
	except:
		pass

def log_info(message = None):
	if verbose_mode == False:
		return

	log_message('Info: ' + message)

def log_error(message = None):
	log_message('Error: ' + message)
