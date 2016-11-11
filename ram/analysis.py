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
from logger import general_log as LOG
import db
import datetime
import json

def _get_new_req_id(host):
    r = oat.issuePostAttestation(cfg.OAT_VERIFIER, host, cfg.OAT_LEVEL)
    LOG.debug('issuePostAttestation:' + json.dumps(r))
    new_id = r['requestId']
    if new_id is None:
        LOG.warning("Something goes wrong id requesting "
                    "new requestId for host '%s'" % host)
    else:
        LOG.info("Saving new requestId (%s) for host '%s'" % (new_id, host))
        db.save_req_id(host, new_id)


def _get_attestation_result(host, req_id):
    r = oat.issuePostAttestationResult(cfg.OAT_VERIFIER, req_id)
    LOG.debug('issuePostAttestationResult:' + json.dumps(r))
    if 'hosts' in r:
        LOG.info("Found valid attestation result for host '%s'" % host)
        return r['hosts']
    else:
        LOG.info(("Valid attestation result not available for  host '%s'") %
                 (host))
        return None

def _get_result_level(host):
    unknown_log_dir = "/var/www/html/OAT/unknown_log";
    reportID = db.getReportID(host);
    logName = "%s/unknown_log_%s" % (unknown_log_dir,reportID['id']);
    logFile = open(logName, 'r');
    res_level = 4;

    for line in logFile:
        if 'Info: load) level' in line:
            image = line.split(' ');
            res_level = image[3];
            break;
    return res_level;

def do_analysis(hosts=[], cert="", req_level=1):
    results = []
    for host in hosts:
        LOG.info("Trying to get valid attestation result for host '%s'" % host)

        result = db.getAttestationResult(host)
        if not result :
            LOG.info("No information of for host '%s'" %(host))
            _r = dict(
                host_name=host,
                trust_lvl='unknown'
            )
        else:
            LOG.info("Found result for '%s'" %(host))
            _r = dict(
                host_name=result['host_name'],
            )
            res_level = _get_result_level(host);
            if cert != result['analysis_request'].split(",")[2].split("=")[1]:
                _r['trust_lvl'] = "cert-err"
            elif datetime.datetime.now() - result['validate_time'] > datetime.timedelta(seconds=30):
                _r['trust_lvl'] = "vtime-err"
            elif (result['analysis_results'] != None and '|true|' in result['analysis_results'] and "|ANALYSIS_COMPLETED|0|" in result['analysis_results']) or (req_level<=res_level) :
                _r['trust_lvl'] = "trusted"
            else:
                _r['trust_lvl'] = 'untrusted'
            _r['validate_time'] = str(result['validate_time'])
            _r['analysis_request'] = result['analysis_request']

        results.append(_r)

    return results
