#! /bin/bash

OAT=$1
HOST=$2
HOSTIP=$3
HOSTDISTRO=$4
HOSTCERTDGST=$5

if [ -z "$OAT" ] ||  [ -z "$HOST" ] || [ -z "$HOSTIP" ] || [ -z "$HOSTDISTRO" ] || [ -z "$HOSTCERTDGST" ]; then
	echo "Missing parameters"
	exit 1
fi

set -x

bash oat_host -e -h $OAT '{"HostName":"'$HOST'","IPAddress":"'$HOSTIP'","Port":"9999","VMM_Name":"'$HOST'-'$HOSTDISTRO'","VMM_Version":"123","VMM_OSName":"'$HOSTDISTRO'","VMM_OSVersion":"v1234","Email":"","AddOn_Connection_String":"","Description":"'$HOSTCERTDGST'"}'


set +x
