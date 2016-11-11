#! /bin/bash

if [ -z $1 ]; then
	echo "Usage: $0 <cassandra-dir>"
	exit 1
fi

CASSANDRADIR=$1;
echo $CASSANDRADIR | grep '/$' > /dev/null
if [ $? -eq 0 ]; then
        CASSANDRADIR=$(echo "${CASSANDRADIR%?}")
fi
export CASSANDRADIR

JNI_H=$(find /usr/lib/jvm -name "jni.h")
if [ -z $JNI_H ]; then
	echo "Java headers not found. Please install the java-1.6.0-openjdk-devel package"
	exit 1
fi

JAVAHEADERS=$(dirname $JNI_H); export JAVAHEADERS
CASSANDRACLASSPATH=$(find $CASSANDRADIR -type f -name "apache-cassandra-[0-9]*"); export CASSANDRACLASSPATH

LIBDIR="/usr/lib64"
if [ ! -d $LIBDIR ]; then
	LIBDIR="/usr/lib"
fi

export LIBDIR
pushd cassandra

make clean
make all
make install

popd
