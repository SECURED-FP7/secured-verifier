# insert_deb_library.py: DEB library functions
#
# Copyright (C) 2013 Politecnico di Torino, Italy
#                    TORSEC group -- http://security.polito.it
#
# Author: Giuseppe Baglio <giuseppebag@gmail.com>
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

from subprocess import PIPE,Popen
import pycassa,os,re
import datetime
import string


def _get_dpkg_output(file_name_deb):
    # To extract the information about the package this function uses the "dpkg --info" shell command
    #
    # INPUT: pool/main/s/sudo/sudo_1.8.3p1-1ubuntu3.4_amd64.deb
    # OUTPUT: returns a tuple (stdout, stderr) of dpkg command
    p = Popen(['dpkg', '--info', file_name_deb], stdout=PIPE, stderr=PIPE)
    return p.communicate()

def getSrcAndArch(package_path):
        # INPUT: "libdevmapper1.02.1_1.02.48-4ubuntu7.3_amd64.deb"
        # OUTPUT: "lvm2_2.02.66-4ubuntu7.3", "amd64"

        output_dpkg, errors = _get_dpkg_output(package_path)
        if len(errors) > 0:
            return None, None, None, errors

        source_name = ""
        source_ver_and_rev = None
        if output_dpkg.find('Source: ') != -1:
            out_split = output_dpkg.split('Source: ')[1].split('\n')[0]
            # check if package and its source have different versions
            if out_split.find("(") != -1:
                source_ver_and_rev = out_split.split("(")[1].split(')')[0].strip()
                out_split = out_split.split("(")[0].strip()
            source_name = out_split
        else:
            out_split = output_dpkg.split('Package: ')
            if (len (out_split) > 1):
                source_name = out_split[1].split('\n')[0]

        # Epoch and version+revision (if not defined already)
        if source_ver_and_rev == None:
            source_ver_and_rev = output_dpkg.split('Version: ')[1].split('\n')[0]

        arch = output_dpkg.split('Architecture: ')[1].split('\n')[0].strip()
        return source_name, source_ver_and_rev, arch, None

def extract_package_files(package_path):
    p = Popen (['dpkg',  '-X', package_path, '.'], stdout=PIPE, stderr=PIPE)

    stdout, stderr = p.communicate()
    if len(stderr) > 0:
        return None, stderr

    stdout_split = stdout.split('\n')
    if len(stdout_split[-1]) == 0:
        stdout_split.pop(-1)
    return stdout_split, None
