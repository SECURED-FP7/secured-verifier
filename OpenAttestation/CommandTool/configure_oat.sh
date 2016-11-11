#! /bin/bash

OAT=$1
HOST=$2
HOSTIP=$3
HOSTPCR0=$4
HOSTDISTRO=$5
RAPATH=$6
DBIP=$7
HOSTCERTDGST=$8

if [ -z "$OAT" ] ||  [ -z "$HOST" ] || [ -z "$HOSTIP" ] || [ -z "$HOSTPCR0" ] || [ -z "$HOSTDISTRO" ] || [ -z "$RAPATH" ] || [ -z "$DBIP" ] || [ -z "$HOSTCERTDGST" ]; then
	echo "Missing parameters"
	exit 1
fi

set -x

#bash oat_cert -h $OAT
bash oat_oem -a -h $OAT '{"Name":"OEM1","Description":"Test id"}'
bash oat_os -a -h $OAT '{"Name":"'$HOSTDISTRO'","Version":"v1234","Description":"Test1"}'
bash oat_mle -a -h $OAT '{"Name":"'$HOST'-'$HOSTDISTRO'","Version":"123","OsName":"'$HOSTDISTRO'","OsVersion":"v1234","Attestation_Type": "PCR","MLE_Type":"VMM","Description":"Test ad"}'
bash oat_host -a -h $OAT '{"HostName":"'$HOST'","IPAddress":"'$HOSTIP'","Port":"9999","VMM_Name":"'$HOST'-'$HOSTDISTRO'","VMM_Version":"123","VMM_OSName":"'$HOSTDISTRO'","VMM_OSVersion":"v1234","Email":"","AddOn_Connection_String":"","Description":"'$HOSTCERTDGST'"}'
bash oat_pcrwhitelist -a -h $OAT '{"pcrName":"0","pcrDigest":"'$HOSTPCR0'","mleName":"'$HOST'-'$HOSTDISTRO'","mleVersion":"123", "osName":"'$HOSTDISTRO'", "osVersion":"v1234"}'
bash oat_analysisType -a -h $OAT '{"name":"load-time+check-cert","module":"RAVerifier","version":2,"url":"'$RAPATH' -H '$DBIP'"}'
bash oat_analysisType -a -h $OAT '{"name":"VALIDATE_PCR;load-time+check-cert","module":"RAVerifier","version":2,"url":"'$RAPATH' -H '$DBIP'"}'
bash oat_analysisType -a -h $OAT '{"name":"load-time","module":"RAVerifier","version":2,"url":"'$RAPATH' -H '$DBIP'"}'


set +x
