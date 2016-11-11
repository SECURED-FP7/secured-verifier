'''
The MIT License (MIT)

Copyright (c) 2015 Tao Su <tao.su@polito.it>
                   Paolo Smiraglia <paolo.smiraglia@polito.it>
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
import mysql.connector as mariadb


from logger import general_log as LOG


def __db_connect():
    try:
        mariadb_connection = mariadb.connect(host=cfg.DB_HOST, user=cfg.DB_USER, password='secured', database= 'oat_db');
    except Exception, ex:
        errMessage = 'error, connection to the database error - %s\n' % (ex);
        LOG.info(errMessage)
    return mariadb_connection


def _c_req_id(host, id):
    conn = __db_connect()
    c = conn.cursor()
    q = "INSERT INTO req_id VALUES (?,?)"
    c.execute(q, (host, id,))
    conn.commit()
    conn.close()


def _r_req_id(host):
    conn = __db_connect()
    c = conn.cursor()
    q = "SELECT * FROM req_id WHERE host==?"
    c.execute(q, (host,))
    row = c.fetchone()
    conn.close()
    return row


def _u_req_id(host, id):
    conn = __db_connect()
    c = conn.cursor()
    q = "UPDATE req_id SET req_id=? WHERE host=?"
    c.execute(q, (id, host,))
    conn.commit()
    conn.close()


def _d_req_id(host):
    conn = __db_connect()
    c = conn.cursor()
    q = "DELETE FROM req_id WHERE host=?"
    c.execute(q, (host,))
    conn.commit()
    conn.close()


def init_db():
    conn = __db_connect()
    c = conn.cursor()
    # dropping existing table
    q = 'DROP TABLE IF EXISTS req_id'
    c.execute(q)
    LOG.info("dropping table 'req_id'")
    conn.commit()
    # creating a new table
    q = '''CREATE TABLE IF NOT EXISTS req_id
           (host TEXT PRIMARY KEY, req_id TEXT)'''
    c.execute(q)
    LOG.info("creating table 'req_id'")
    conn.commit()
    conn.close()


def save_req_id(host, id):
    r = _r_req_id(host)
    if r is None:
        _c_req_id(host, id)
    else:
        _u_req_id(host, id)


def load_req_id(host):
    r = _r_req_id(host)
    if r is None:
        return None
    else:
        return r[1]


def getHostCertDGST(host):
    conn = __db_connect()
    cursor = conn.cursor()

    getCertDGSTCommand= "select HOST_NAME, DESCRIPTION from HOST where HOST_NAME='%s';" % (host);

    try :
        cursor.execute(getCertDGSTCommand);
    except Exception as e:
        message = "error - noresultavailableinDB - %s \n" %(e);
        print message;
        LOG.info(message);
        sys.exit(1)

    certDigest = {};
    for HOST_NAME, DESCRIPTION in cursor:
        certDigest['host_name'] = HOST_NAME;
        certDigest['cert_digest'] = DESCRIPTION;
    return certDigest

def getReportID(host):
    # this is the right approach, need to check the ned's id before giving back the result
    conn = __db_connect()
    cursor = conn.cursor()
    reportID = {};

    getReportIDCommand= "select id, machine_name from audit_log where machine_name='%s' ORDER BY id DESC LIMIT 1;" % (host);
    try :
        cursor.execute(getReportIDCommand);
    except Exception as e:
        message = "error - noresultavailableinDB - %s \n" %(e);
        print message;
        LOG.info(message);
        sys.exit(1)

    for id, machine_name in cursor:
        reportID['id'] = id;
        reportID['host_name'] = machine_name;

    return reportID


def getAttestationResult(host):
    conn = __db_connect()
    cursor = conn.cursor()

    getResultCommand= "select host_name, analysis_request, analysis_results, validate_time, expiration_time from attest_request where host_name='%s' ORDER BY validate_time DESC LIMIT 1;" % (host);

    try :
        cursor.execute(getResultCommand);
    except Exception as e:
        message = "error - noresultavailableinDB - %s \n" %(e);
        print message;
        LOG.info(message);
        sys.exit(1)

    attestResult = {}
    for host_name, analysis_request, analysis_results, validate_time, expiration_time in cursor:
        attestResult['host_name'] = host_name;
        attestResult['analysis_request'] = analysis_request;
        attestResult['analysis_results'] = analysis_results;
        attestResult['validate_time'] = validate_time;
        attestResult['expiration_time'] = expiration_time;

    return attestResult
