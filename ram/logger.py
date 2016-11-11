'''
The MIT License (MIT)

Copyright (c) 2015 Paolo Smiraglia <paolo.smiraglia@polito.it>
                   Tao Su <tao.su@polito.it>
                   TORSEC Group (http://security.polito.it)
                   Politecnico di Torino

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import config as cfg
import logging

# this catch warning messages (if enabled) issued by urllib3
logging.captureWarnings(True)
_py_warn = logging.getLogger('py.warnings')

# set logging level according to LOG_LEVEL configuration directive
_lvl = logging.NOTSET
if cfg.LOG_LEVEL == 'debug':
    _lvl = logging.DEBUG
elif cfg.LOG_LEVEL == 'info':
    _lvl = logging.INFO
elif cfg.LOG_LEVEL == 'warn':
    _lvl = logging.WARNING
elif cfg.LOG_LEVEL == 'err':
    _lvl = logging.ERROR
else:
    _lvl = logging.DEBUG

# define console handler
ch = logging.StreamHandler()
ch.setLevel(_lvl)

# define file handlers
fh_general = logging.FileHandler(('%s/general.log' % cfg.LOG_DIR))
fh_access = logging.FileHandler(('%s/access.log' % cfg.LOG_DIR))
fh_app = logging.FileHandler(('%s/app.log' % cfg.LOG_DIR))

# log entries format
fmt = logging.Formatter('%(asctime)s - %(name)-16s - '
                        '%(levelname)-8s - %(message)s')

# set the formatter in each handler
ch.setFormatter(fmt)
fh_general.setFormatter(fmt)
fh_access.setFormatter(fmt)
fh_app.setFormatter(fmt)

# get 'tornado.general' logger
general_log = logging.getLogger('tornado.general')
general_log.setLevel(_lvl)
if cfg.WEBAPP_AS_DAEMON is True:
    general_log.addHandler(fh_general)
else:
    general_log.addHandler(ch)
general_log.propagate = False

# get 'tornado.access' logger
access_log = logging.getLogger('tornado.access')
access_log.setLevel(_lvl)
if cfg.WEBAPP_AS_DAEMON is True:
    access_log.addHandler(fh_access)
else:
    access_log.addHandler(ch)
access_log.propagate = False

# get 'tornado.application' logger
app_log = logging.getLogger('tornado.application')
app_log.setLevel(_lvl)
if cfg.WEBAPP_AS_DAEMON is True:
    app_log.addHandler(fh_app)
else:
    app_log.addHandler(ch)
app_log.propagate = False

# set handler for urllib3 warning messages
if cfg.WEBAPP_AS_DAEMON is True:
    _py_warn.addHandler(fh_general)
else:
    _py_warn.addHandler(ch)
