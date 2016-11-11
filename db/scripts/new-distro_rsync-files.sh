#!/bin/sh

# new-distro_rsync-files.sh
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
	u ) input rsync file for 'updates' packages
	s ) input rsync file for 'security' packages
        n ) input rsync file for 'newpackage' packages
"
}

#
# Il file installed_pkg.txt contiene il nome di tutti i pacchetti installati della distribuzione che si vuole analizzare.
# Deve essere creato con il comando 
#	dpkg --get-selections | awk '{print $1}' 
#
PKGS=$(cat installed_pkg.txt)

# Il file seguente deve contenere tutte le "voci rsync" dei pacchetti di tipo "newpackage" presenti nel filesystem del server
# Può essere creato con il comando
#	cat /srv/ra/db/logs/rsync*newpackage* | grep "deb$" | awk '{print $5}' | sort | uniq | awk '{print "1999/01/01 00:00:00 [1986] >f+++++++++ "$1}' > rsync-Ubuntu-release-arch-newpackage-20130000_0000.log
RSYNC_NEWPKGS='/srv/ra/db/logs/rebuildDB/uniqueRsyncFile/rsync-Ubuntu-precise-all,amd64-newpackage-20130000_0000.log'

# E' il file rsync che contiene tutti pacchetti correttamente filtrati
OUTFILE_NEWPKGS='rsync-Ubuntu-precise-all,amd64-newpackage-10001010_0000.log'

TMP_NEWPKGS='tmp_NEWPKGS.txt'

RSYNC_UPDS='/srv/ra/db/logs/rebuildDB/uniqueRsyncFile/rsync-Ubuntu-precise-all,amd64-updates-20130000_0000.log'
OUTFILE_UPDS='rsync-Ubuntu-precise-all,amd64-updates-10001010_0000.log'
TMP_UPDS='tmp_UPDS.txt'

RSYNC_SEC='/srv/ra/db/logs/rebuildDB/uniqueRsyncFile/rsync-Ubuntu-precise-all,amd64-security-20130000_0000.log'
OUTFILE_SEC='rsync-Ubuntu-precise-all,amd64-security-10001010_0000.log'
TMP_SEC='tmp_SEC.txt'

while getopts "h?n:u:s:" opt; do
    case "$opt" in
	 h|\?)
        	show_help
	        exit 0
	        ;;
	n)  RSYNC_NEWPKGS=$OPTARG
        	;;
	u)  RSYNC_UPDS=$OPTARG
        	;;
	s) RSYNC_SEC=$OPTARG
		;;
    esac
done

for pkg in $PKGS
do
	cat $RSYNC_NEWPKGS | grep $pkg"_" | grep "deb$" >> $TMP_NEWPKGS
	cat $RSYNC_UPDS |  grep $pkg"_" | grep "deb$" >> $TMP_UPDS
	cat $RSYNC_SEC |  grep $pkg"_" | grep "deb$" >> $TMP_SEC
done

cat $TMP_NEWPKGS | sort | uniq > $OUTFILE_NEWPKGS && rm $TMP_NEWPKGS
echo "Done:\n\t" $RSYNC_NEWPKGS"\n\t\t (n. line: "$(wc -l $OUTFILE_NEWPKGS | awk '{print $1}')")"

cat $TMP_UPDS | sort | uniq > $OUTFILE_UPDS && rm $TMP_UPDS
echo "Done:\n\t" $RSYNC_UPDS"\n\t\t (n. line: "$(wc -l $OUTFILE_UPDS | awk '{print $1}')")"

cat $TMP_SEC | sort | uniq > $OUTFILE_SEC && rm $TMP_SEC
echo "Done:\n\t" $RSYNC_SEC"\n\t\t (n. line: "$(wc -l $OUTFILE_SEC | awk '{print $1}')")"
