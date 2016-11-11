# Introduction

The scripts in this directory is to create a external reference database used by the external analysis tool of OpenAttestion framework, they are developed by TorSec Group in Politecnico di Torino. The external analysis tool relies on this database to verify the digests of the executable running in the attested platform. The database chosen is Cassandra-1.2.19. These scripts are capable to download the update packages from pre-defined repositories, de-compile them, compute the SHA1 values of the binraies and meanwhile find its update type, and insert them into the reference database. Then when challenger is attesting the target, it can know what software is running in the attestor and whether it is up-to-date, and if it has security vulnerability.

Only packages of CentOS7 is considered here.

# Dependencies

```bash
root@verifier# yum install rpm-devel java-1.7-0-openjdk.x86_64 java-1.7-0-openjdk-devel.x86_64 python-pip
root@verifier# pip install pycassa pygraphviz
```

# Installation steps
0. It is assumed all files are cloned as they are in the repository. The base directory is $BASEDIR/verifier;

1. go to install directory, un-compress the cassandra database;
```bash
root@verifier# cd BASEDIR/verifier/db/install
root@verifier# tar -xvzf apache-cassandra-1.2.19-bin.tar.gz
```

2. install cassandra database;
```bash
root@verifier# ./install_cassandra_libs.sh BASEDIR/verifier/db/install/apache-cassandra-1.2.19
```

3. initialise the database with the schema used to store the information;
```bash
root@verifier# cd BASEDIR/verifier/db/install/apache-cassandra-1.2.19/bin
root@verifier# ./cassandra > /dev/null
root@verifier# ./cassandra-cli -h localhost -f BASEDIR/verifier/db/install/cassandra/schema/cassandra-schema-common.txt
root@verifier# ./cassandra-cli -h localhost -f BASEDIR/verifier/db/install/cassandra/schema/cassandra-schema-rpm.txt
```

4. copy configuration files into `/etc/ra`;
```bash
root@verifier# mkdir /etc/ra
root@verifier# cp BASEDIR/verifier/db/conf/pkgs_download_list.conf.sample /etc/ra/pkgs_download_list.conf
root@verifier# cp BASEDIR/verifier/db/conf/ra.conf.sample /etc/ra/ra.conf
```
RABASEDIR attribute in ra.conf needs to be changed to `BASEDIR/verifier`

5. create Packages directory, go to `scripts` directory and run `update_pkgs.sh`;
```bash
root@verifier# mkdir BASEDIR/verifier/Packages
root@verifier# cd BASEDIR/verifier/db/scripts
root@verifier# bash update_pkgs.sh
```
6. when the database is created, please use the `ra_verifier.py` script to test it;
```bash
root@verifier# cd BASEDIR/verifier/v2
root@verifier# ./ra_verifier.py -i BASEDIR/verifier/db/measurements/ascii_runtime_measurements -q CentOS7 -a "load-time,l_req=l4|>=" -v -H localhost
```

Should see information:
```bash
Info: 0 (0/0)
0 (0/0)
0
0

Info: 0.00266
0.24042
0.07041
0.11005
0
0.42355
```
