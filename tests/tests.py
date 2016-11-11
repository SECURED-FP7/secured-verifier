#!/usr/bin/env python
# -*- coding: utf-8 -*-

# /**
# * The MIT License (MIT)
# *
# * Copyright (c) 2015 Tao Su <tao.su@polito.it>
# *                    TORSEC Group (http://security.polito.it)
# *                    Politecnico di Torino
# *
# * Permission is hereby granted, free of charge, to any person obtaining a copy
# * of this software and associated documentation files (the "Software"), to deal
# * in the Software without restriction, including without limitation the rights
# * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# * copies of the Software, and to permit persons to whom the Software is
# * furnished to do so, subject to the following conditions:
# *
# * The above copyright notice and this permission notice shall be included in
# * all copies or substantial portions of the Software.
# *
# * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# * THE SOFTWARE.
# */


# File:		oat_middleware.py
#
# Description:
#		This middleware is used to facilitate the usage of remote attestation
#               feature provided by OpenAttestation Appraiser. This middleware is 
#               seated between the SMASH editor and the OpenAttestation Appraiser, and 
#               convert the attestation requests of certain nodes into the correct 
#               format, which can be understood by the appraiser. In the meantime, 
#               this middleware is stateless, that no addtional management efforts 
#               are needed.
#		However, the database of the OpenAttestation needs minor modifications
#               that allows the middleware to get the output in a dict format or json
#               format.
#
# Params:       
#               -n, --nodes:        the node list need to get the attestation result,
#                                   separated with comma ',' symbol;
#               -v, --verifier:     the OpenAttestation Appraiser, can be the hostname,
#                                   or the ip address;
#               -p, --period:       the attestation period to be set in the attestation
#                                   request, default is 1 min;
#               -e, --expiration:   the expiration time of the periodic attestation 
#                                   requests;
#
# Author:       Tao Su

import sys, getopt, os, time
import requests,json
import unittest,subprocess

verbose = False
cur_stdout = subprocess.PIPE
BASE_DIR='/home/tao/dev/secured/verifier/tests/'

if verbose:
    cur_stdout = None;

def log(message):
    if not verbose:
        return;
    print message;

def issuePollAttestation(verifier, node, level):
    POLLHOST_URL="https://%s:8443/AttestationService/resources/PollHosts"%(verifier);
    nodeID = node ;
    integrityLevel = level;
    postData = {"hosts":[nodeID],"analysisType":"load-time,"+integrityLevel};    
    postData = json.dumps(postData);
    certfile = BASE_DIR+'certfile.cer';
    r = requests.post(POLLHOST_URL, verify=certfile, data=postData, headers={'Content-Type':'application/json'});
    return r.json();


class VerifyVerifierTestCase( unittest.TestCase ): 

    def setUp(self): 
#        self.VERIFIER = '130.192.1.86'
        self.VERIFIER = 'verifier'
        self.INTEGRITYLEVEL1 =  'l_req=l1_ima_all_ok|>=';
        self.INTEGRITYLEVEL2 =  'l_req=l2_ima_all_ok|>=';
        self.NODE = 'test-ned';

    def runTest(self):
        attestResultL1 = issuePollAttestation(self.VERIFIER, self.NODE, self.INTEGRITYLEVEL1);
        attestResultL2 = issuePollAttestation(self.VERIFIER, self.NODE, self.INTEGRITYLEVEL2);

        attestResultL1 = attestResultL1['hosts'];
        attestResultL2 = attestResultL2['hosts'];

        self.assertEqual( attestResultL1[0]['trust_lvl'], 'trusted');
        self.assertEqual( attestResultL2[0]['trust_lvl'], 'untrusted');
        
unittest.main(verbosity=2)
