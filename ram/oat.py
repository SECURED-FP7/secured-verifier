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
import json
import requests
import db

# disable urllib3 warnings about certificate verification
import urllib3
urllib3.disable_warnings()


def issuePollAttestation(verifier, node, level):
    pollhost_url = (
        ("https://%s:8443/AttestationService/resources/PollHosts") %
        (verifier)
    )
    node_id = node
    integrity_level = level
    post_data = dict(hosts=[node_id],
                     analysisType=('load-time,%s' % integrity_level))
    r = requests.post(pollhost_url, verify=cfg.OAT_CERT,
                      data=json.dumps(post_data),
                      headers={'Content-Type': 'application/json'})
    return r.json()


def issuePollAttestationCheckCert(verifier, node, level):
    pollhost_url = (
        ("https://%s:8443/AttestationService/resources/PollHosts") %
        (verifier)
    )

    cert_digest = db.getHostCertDGST(node)['cert_digest']
    node_id = node
    integrity_level = level
    post_data = dict(hosts=[node_id],analysisType=('load-time+check-cert,%s,cert_digest=%s' % (integrity_level, cert_digest)))

    r = requests.post(pollhost_url, verify=cfg.OAT_CERT,
                      data=json.dumps(post_data),
                      headers={'Content-Type': 'application/json'})
    return r.json()




def issuePostAttestation(verifier, node, level, period=cfg.OAT_PERIOD,
                         expiration=cfg.OAT_EXPIRATION):
    posthost_url = (
        ("https://%s:8443/AttestationService/resources/PostHosts") %
        (verifier)
    )
    node_id = node
    integrity_level = level
    post_data = dict(hosts=[node_id],
                     analysisType=('load-time,%s' % integrity_level),
                     timeThreshold=period, expirationTime=expiration)
    r = requests.post(posthost_url, verify=cfg.OAT_CERT,
                      data=json.dumps(post_data),
                      headers={'Content-Type': 'application/json'})
    return r.json()


def issuePostAttestationResult(verifier, req_id):
    posthost_url = (
        ("https://%s:8443/AttestationService/resources/PostHosts") %
        (verifier)
    )
    post_data = dict(requestId=req_id, lastResult=False)
    r = requests.get(posthost_url, verify=cfg.OAT_CERT,
                     data=json.dumps(post_data),
                     headers={'Content-Type': 'application/json'})
    return r.json()
