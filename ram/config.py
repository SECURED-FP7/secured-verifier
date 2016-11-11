'''
The MIT License (MIT)

Copyright (c) 2015 Tao Su <tao.su@polito.it>
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

BASE_DIR = '/home/tao/ram'


STATIC_PATH= '%s/html/' % BASE_DIR
DB_PATH = '%s/data/mw.db' % BASE_DIR

DB_HOST = 'verifier'
DB_USER = 'secured'


WEBAPP_PORT = 8899
WEBAPP_ADDRESS = 'verifier'
WEBAPP_AS_DAEMON = False

OAT_CERT = '%s/data/certfile.cer' % BASE_DIR
OAT_PERIOD = 60000
OAT_NODE = ['ned1','ned2']
OAT_EXPIRATION = '1d'
OAT_VERIFIER = 'verifier'
OAT_LEVEL = 'l_req=l4_ima_all_ok|>='
OAT_WAITTIME = 8


# accepted values: debug, info, warn, err
LOG_LEVEL = 'debug'
LOG_DIR = '%s/logs' % BASE_DIR
