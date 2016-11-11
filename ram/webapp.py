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

import argparse
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.template
import json
import sys
import datetime


import config as cfg
from analysis import do_analysis
from db import init_db as _init_db
from db import getAttestationResult
from logger import general_log as LOG

import os

VERSION = '0.3'

settings = {
    "debug": True,
    "static_path": os.path.join(cfg.STATIC_PATH, "static")
}
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header('content-type', 'application/json')
        res_body = dict(status='success', version=VERSION)
        self.write(json.dumps(res_body, separators=(',', ':')))


# For user to read attestation results
class UserHandler(tornado.web.RequestHandler):
    def get(self):
        result = False;

        level = int(self.get_argument("LEVEL", False))
        cn = self.get_argument("CN", False)
        dgst = self.get_argument("DGST", False)

        if not level or not cn or not dgst:
            self.render("html/templates/err.html", title="Error!!!", message="Need all three parameters in the url!", validate_time = datetime.datetime.now().time())
        else:

            hosts = [cn]
            results = do_analysis(hosts, dgst)

            if results[0]['trust_lvl'] == "cert-err":
                self.render("html/templates/err.html", title="Error!!!", message="Certificate dismatch!", validate_time = datetime.datetime.now().replace(microsecond=0))
            elif results[0]['trust_lvl'] == "vtime-err":
                self.render("html/templates/err.html", title="Error!!!", message="Stale result!", validate_time = datetime.datetime.now().replace(microsecond=0))
            elif results[0]['trust_lvl'] == "trusted":
                self.render("html/templates/base.html", title= "Attestation Result of "+cn, CN=cn, LEVEL=level, DGST=dgst, TRUST="The NED is trusted!", validate_time =results[0]['validate_time'], result=results[0])
            else:
                self.render("html/templates/err.html", title="Error!!!", message="The NED is not trusted!", validate_time = datetime.datetime.now().replace(microsecond=0))


class RAHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header('content-type', 'application/json')
        req = self.request
        if req.headers.get('Content-Type').lower() == 'application/json':
            try:
                req_body = json.loads(req.body)
                if 'hosts' in req_body:
                    hosts = req_body['hosts']
                    cert_req = req_body['analysisType'].split(",")[2].split("=")[1]
                    req_level = req_body['analysisType'].split(",")[1].split("=")[1].split("|")[0][1:]
                    r = do_analysis(hosts, cert_req, req_level);

                    newResult = dict(status='success', results=r, n_results=len(r))
                    self.write(
                        json.dumps(newResult, separators=(',', ':'))
                    )

                else:
                    self.set_status(400)
                    res_body = dict(status='error', msg='malformed body')
                    self.write(json.dumps(res_body, separators=(',', ':')))
            except Exception as E:
                self.set_status(400)
                LOG.error(E)
                res_body = dict(status='error', msg='malformed body')
                self.write(json.dumps(res_body, separators=(',', ':')))
        else:
            self.set_status(400)
            res_body = dict(status='error', msg='invalid content-type')
            self.write(json.dumps(res_body, separators=(',', ':')))

class VerifierHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header('content-type', 'application/json')
        req = self.request
        if req.headers.get('Content-Type').lower() == 'application/json':
            req_body = json.loads(req.body)
            if 'question' in req_body:
                if (req_body['question'] == 'verifiers'):
                    newResult={"verifiers":[{"name":"v1", "ip":"130.192.1.86"}]}
                else:
                    newResult={}

                self.write(
                    json.dumps(newResult, separators=(',', ':'))
                )

            else:
                self.set_status(400)
                res_body = dict(status='error', msg='malformed body')
                self.write(json.dumps(res_body, separators=(',', ':')))


application = tornado.web.Application(
[
    (r"/", MainHandler),
    (r"/mach/status", RAHandler),
    (r"/user/status", UserHandler),
    (r"/verifiers", VerifierHandler),
],
**settings
)


def run_webapp():
    LOG.info(("Staring webapp listening on https://%s:%d") %
             (cfg.WEBAPP_ADDRESS, cfg.WEBAPP_PORT))

    https_server = tornado.httpserver.HTTPServer(application, ssl_options = {
        "certfile": cfg.BASE_DIR +"/data/myserver.crt",
        "keyfile": cfg.BASE_DIR + "/data/myserver.key",
    })
    https_server.listen(cfg.WEBAPP_PORT, cfg.WEBAPP_ADDRESS)
    tornado.ioloop.IOLoop.instance().start()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--run-webapp', help='run webapp', action='store_true')

    if parser.parse_args().run_webapp is True:
        run_webapp()

if __name__ == "__main__":
    main()
