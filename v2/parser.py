#!/usr/bin/env python
# -*- coding: utf-8 -*-

# parser.py: parse an integrity report
#
# Copyright (C) 2014 Politecnico di Torino, Italy
#                    TORSEC group -- http://security.polito.it
#
# Author: Roberto Sassu <roberto.sassu@polito.it>
#         Tao Su <tao.su@polito.it>
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

import base64
import struct
from structs import IMARecord
#import xml_parser.ir_parser
#import xml_parser.ir_simple_parser
import xml.sax


def parse_IMA_Image(hash_str, type_str, image_blob):
    offset = 0

    line = '10 %s %s' %(hash_str.encode('hex'), type_str)
    if type_str == 'ima':
        line += ' ' + image_blob[offset:20].encode('hex')
        offset += 20
        namelen = struct.unpack("<L", image_blob[offset:offset + 4])[0]
        line += ' ' + image_blob[offset:namelen]
    else:
	if type_str == 'ima-ng':
            type_str = 'd-ng|n-ng'
        i = 0
        while offset < len(image_blob):
            field_len = struct.unpack("<L", image_blob[offset:offset + 4])[0]
            offset += 4
            if field_len == 0:
                line += ' '
                i += 1
                continue

            field = image_blob[offset:offset + field_len]
            offset += field_len
            field_id = type_str.split('|')[i]
            if field_id == 'd-ng':
                algo = field.split('\0')[0]
                digest = field[len(algo) + 1:].encode('hex')
                line += ' ' + algo + digest
            else:
                if field_id in ['hook-id', 'hook-mask']:
                    field = struct.unpack("<L", field)[0]
                elif field_id == 'lw':
                    field = struct.unpack("<Q", field)[0]
                elif field_id in ['n-ng', 'n']:
                    field = field[:-1]
                elif field_id in ['subj', 'obj', 'bprm-subj']:
                    field = field[:-2]
                line += ' ' + str(field)
            i += 1

    IMARecord(line)


class IMAMeasureHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.type_str = ''
        self.image_blob = ''
        self.content = ''
        self.capture = False

    def startElement(self, name, attrs):
        if "Objects" in name:
            self.type_str = attrs.getValue('Type')
            self.image_blob = attrs.getValue('Image')
        if "ns4:Hash" in name and attrs.getValue('Id').startswith('PCR_10_'):
            self.capture = True

    def endElement(self, name):
        if "ns4:Hash" in name:
            self.capture = False

    def characters(self, content):
        if not self.capture:
            return

        self.content += content
        if len(self.content) != 28:
            return

        line = parse_IMA_Image(base64.decodestring(self.content), self.type_str,
                               base64.decodestring(self.image_blob))
        self.content = ''


class XMLParser(object):
    def parse_report_pyxb(self, report_xml):
        report = xml_parser.ir_simple_parser.CreateFromDocument(report_xml)

        ima_snap = [snap for snap in report.SnapshotCollection
                    if snap.ComponentID.Id.split('_')[1] == '10'][0]

        for v in ima_snap.Values:
            item = v.orderedContent()[0].value.Objects[0]
            line = parse_IMA_Image(item.Hash[0].value(), item.Type, item.Image)

    def __init__(self, report_xml):
        xml.sax.parseString(report_xml, IMAMeasureHandler())


class ASCIIParser(object):
    def __init__(self, report_ascii):
        for file_line in report_ascii.split('\n'):
            if len(file_line) == 0:
                continue
            IMARecord(file_line)


class IRParser(object):
    def __init__(self, report_str):
        if report_str.startswith('<?xml'):
            XMLParser(report_str)
        else:
            ASCIIParser(report_str)
