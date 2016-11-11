# insert_rpm_library.py: RPM library functions
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

import os,rpm,string,pycassa
from subprocess import PIPE,Popen


def getSrcAndArch(package_path):
    try:
        fdno = os.open(package_path,os.O_RDONLY)
        ts = rpm.TransactionSet()
        ts.setVSFlags(rpm._RPMVSF_NOSIGNATURES)
        hdr = ts.hdrFromFdno(fdno)
        os.close(fdno)
    except Exception,ex:
        return None, None, None, ex

    #NOTE: always take the version and release extracted from the source RPM
#    source_ver_and_rev = '-'.join([hdr[rpm.RPMTAG_VERSION], hdr[rpm.RPMTAG_RELEASE]])
    source_ver_and_rev = '.'.join('-'.join(hdr[rpm.RPMTAG_SOURCERPM].split('-')[-2:]).split('.')[:-2])

    #TODO: at the moment, we assume that the epoch of the source package and the binary package are always the same
    #      to remove this assumption it is needed to fetch the epoch directly from the source package since it is not
    #      contained in the source package file name.
    if hdr[rpm.RPMTAG_EPOCH] is not None:
        source_ver_and_rev = ':'.join([str(hdr[rpm.RPMTAG_EPOCH]), source_ver_and_rev])

    return '-'.join(hdr[rpm.RPMTAG_SOURCERPM].split('-')[:-2]), source_ver_and_rev, hdr[rpm.RPMTAG_ARCH], None

def extract_package_files(package_path):
    p1 = Popen(['rpm2cpio',package_path],stdout=PIPE)
    p2 = Popen(['cpio','--quiet','--no-absolute-filenames','-idmuv','--no-preserve-owner'], stdin=p1.stdout, stdout=PIPE, stderr=PIPE)
    p1.stdout.close()

    # cpio sends the list of extracted files to stderr
    p2_stderr_split = [f for f in p2.communicate()[1].split('\n') if not f.startswith('cpio:') and len(f) > 0]
    return p2_stderr_split, None
