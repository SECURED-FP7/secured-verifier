#! /bin/bash

# create_Db_with_rsync-files.sh
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

show_help(){
echo "Usage:
        h | ? ) show this help message
	d ) DB packages directory
        u ) input rsync file for 'updates' packages
        s ) input rsync file for 'security' packages
        n ) input rsync file for 'newpackage' packages
	o ) standard output file for this script 
	e ) standard error file for inner command
	i ) standard output file for inner command
	f ) update script to insert packages in the DB
"
}

PKGS_DIR='/srv/ra/Packages/precise'
SCRIPT_OUTPUT=$0"_execution.output"
SCRIPT_STDERR=$0"_inner.stderr"
SCRIPT_SDTOUT=$0"_inner.stdout"
SYNC_NEWPKGS='rsync-Ubuntu-precise-all,amd64-newpackage-10001010_0000.log'
RSYNC_UPDS='rsync-Ubuntu-precise-all,amd64-updates-10001010_0000.log'
RSYNC_SEC='rsync-Ubuntu-precise-all,amd64-security-10001010_0000.log'
UPDATE_SCRIPT='/srv/ra/update_pkgs.sh'

while getopts "h?dnusoeif:" opt; do
    case "$opt" in
         h|\?)
                show_help
                exit 0
                ;;
	d) PKGS_DIR=$OPTAR
		;;
        n) RSYNC_NEWPKGS=$OPTARG
                ;;
        u) RSYNC_UPDS=$OPTARG
                ;;
        s) RSYNC_SEC=$OPTARG
                ;;
	o) SCRIPT_OUTPUT=$OPTARG
		;;
	e) SCRIPT_STDERR=$OPTARG
		;;
	i) SCRIPT_SDTOUT=$OPTARG
		;;
	f) UPDATE_SCRIPT=$OPTARG
		;;
    esac
done

echo "Newpackage pkgs: " > $SCRIPT_OUTPUT
date >> $SCRIPT_OUTPUT
$UPDATE_SCRIPT -r $RSYNC_NEWPKGS -d $PKGS_DIR 1>$SCRIPT_SDTOUT 2>$SCRIPT_STDERR
date >> $SCRIPT_OUTPUT

echo "Security pkgs: " >> $SCRIPT_OUTPUT
date >> $SCRIPT_OUTPUT
$UPDATE_SCRIPT -r $RSYNC_SEC -d $PKGS_DIR 1>$SCRIPT_SDTOUT 2>$SCRIPT_STDERR
date >> $SCRIPT_OUTPUT

echo "Updates pkgs: " >> $SCRIPT_OUTPUT
date >> $SCRIPT_OUTPUT
$UPDATE_SCRIPT -r $RSYNC_UPDS -d $PKGS_DIR 1>$SCRIPT_SDTOUT 2>$SCRIPT_STDERR
date >> $SCRIPT_OUTPUT
