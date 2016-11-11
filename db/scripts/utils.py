# utils.py: some useful functions
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

import os
import rpm
from subprocess import Popen, PIPE
from datetime import datetime, timedelta, date


def get_rpm_header(rpm_file):
    fdno = os.open(rpm_file, os.O_RDONLY)
    ts = rpm.TransactionSet()
    ts.setVSFlags(rpm._RPMVSF_NOSIGNATURES)
    hdr = ts.hdrFromFdno(fdno)
    os.close(fdno)
    return hdr


def get_pkg_list(pkg_base_dir, pkgs_list):
    result = []
    fd = open(pkgs_list, 'r')
    for package in fd.readlines():
        if len(package) == 0:
                continue

        package = package.strip()
        if len(pkg_base_dir) != 0:
            package_path = "%s/%s" %(pkg_base_dir, package)
        else:
            package_path = package

        result.append(package_path)

    return result


def get_epoch_dict(pkg_base_dir, pkgs_list):
    epoch_dict = {}
    for pkg in get_pkg_list(pkg_base_dir, pkgs_list):
        rpm_hdr = get_rpm_header(pkg)
        srpm = rpm_hdr[rpm.RPMTAG_SOURCERPM]
        srpm_key = '.'.join(srpm.split('.')[:-2])
        pkg_key = '.'.join(os.path.basename(pkg).split('.')[:-2])

        epoch_str = ''
        if rpm_hdr[rpm.RPMTAG_EPOCH] is not None:
            epoch_str = str(rpm_hdr[rpm.RPMTAG_EPOCH])

        if srpm_key not in epoch_dict or srpm_key == pkg_key:
            epoch_dict[srpm_key] = epoch_str

    return epoch_dict


def get_date_pushed_interval(pkg_base_dir, pkgs_list):
    last_date_submitted = None
    first_date_submitted = None

    for pkg in get_pkg_list(pkg_base_dir, pkgs_list):
        timestamp = os.path.getmtime(pkg)
        pkg_mtime = datetime.fromtimestamp(timestamp)
        if last_date_submitted is None or pkg_mtime > last_date_submitted:
            last_date_submitted = pkg_mtime
        if first_date_submitted is None or pkg_mtime < first_date_submitted:
            first_date_submitted = pkg_mtime

    # usually updates are announced 1 day after a pkg is uploaded
    delta = timedelta(days=3)
    last_date_submitted += delta
    first_date_submitted -= delta

    return (datetime.strftime(last_date_submitted, '%Y-%m-%d %H:%M:%S'),
            datetime.strftime(first_date_submitted, '%Y-%m-%d %H:%M:%S'))


def date_is_older(date_a, date_b):
    a = datetime.strptime(date_a, '%Y-%m-%d %H:%M:%S')
    b = datetime.strptime(date_b, '%Y-%m-%d %H:%M:%S')
    return a <= b


def get_pkg_datetime(pkg_base_dir, pkgs_list, requested_pkg):
    for pkg in get_pkg_list(pkg_base_dir, pkgs_list):
        rpm_hdr = get_rpm_header(pkg)
        srpm = rpm_hdr[rpm.RPMTAG_SOURCERPM]
        if srpm != requested_pkg:
            continue

        return datetime.fromtimestamp(os.path.getmtime(pkg))

    return None
