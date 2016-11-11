#! /bin/bash

OAT=$1
HOST=$2
HOSTIP=$3
HOSTPCR0=$4
HOSTDISTRO=$5
HOSTCERTDGST=$6

if [ -z "$OAT" ] ||  [ -z "$HOST" ] || [ -z "$HOSTIP" ] || [ -z "$HOSTPCR0" ] || [ -z "$HOSTDISTRO" ] || [ -z "$HOSTCERTDGST" ]; then
	echo "Missing parameters"
	exit 1
fi

set -x

bash oat_mle -a -h $OAT '{"Name":"'$HOST'-'$HOSTDISTRO'","Version":"123","OsName":"'$HOSTDISTRO'","OsVersion":"v1234","Attestation_Type": "PCR","MLE_Type":"VMM","Description":"Test ad"}'
bash oat_host -a -h $OAT '{"HostName":"'$HOST'","IPAddress":"'$HOSTIP'","Port":"9999","VMM_Name":"'$HOST'-'$HOSTDISTRO'","VMM_Version":"123","VMM_OSName":"'$HOSTDISTRO'","VMM_OSVersion":"v1234","Email":"","AddOn_Connection_String":"","Description":"'$HOSTCERTDGST'"}'
bash oat_pcrwhitelist -a -h $OAT '{"pcrName":"0","pcrDigest":"'$HOSTPCR0'","mleName":"'$HOST'-'$HOSTDISTRO'","mleVersion":"123", "osName":"'$HOSTDISTRO'", "osVersion":"v1234"}'


set +x
