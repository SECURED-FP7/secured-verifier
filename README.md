# Introduction

The code in this repository is used to create a Third-Party Verifier, which is able to perform TCG compliant remote attestation operation on the NED(s) pre-registered to it.

The verifier hosts four services, remote attestation server, IMA reference database, periodic attestation tasks, web service publishes the attestation result.

The remote attestation server is using [OpenAttestation v1.7](https://github.com/OpenAttestation/OpenAttestation/tree/v1.7) with additional tools to find the IMA measurements in the integrity report sent from the NED to the verifier in the reference database.

The reference database is hosted using [apache-cassandra-1.2.19](http://cassandra.apache.org/), with customised modules to compare the package's versions, and store them in order in the reference database.

The periodic attestation is created using [Celery](http://www.celeryproject.org/), and the message broker is [rabbitmq](https://www.rabbitmq.com/).

The verifier is a computing intensive entity, the minimum spec is 2 CPU cores @ 2.66Ghz + 4GB memory + 4GB swap, the recommended spec is 4 cores @ 3392.142MHz + 4GB memory + 4GB swap.


# Dependencies for CentOS7 mininal installation:

~~~bash
root@verifier# yum install epel-release
root@verifier# yum install ant trousers trousers-devel php-soap mariadb mariadb-server python-networkx python-suds python-matplotlib graphviz-devel patch java-1.7.0-openjdk java-1.7.0-openjdk-devel zip unzip gcc gcc-c++ rpm-build python-pip git httpd php php-mysql rpm-devel rabbitmq-server mod_ssl mysql-connector-python firewalld
root@verifier# pip install pycassa pygraphviz Celery urllib3 requests tornado
~~~

# Installation steps:
0.	it is assumed that the initial directory is `BASEDIR/verifier` and all files are cloned to this directory;

1.	map the verifier's ip address into `/etc/hosts` and change the local host name
	to 'verifier', to simplify the future setup;

	```bash
	root@verifier# echo -e 'xxx.xxx.xxx.xxx \t verifier' >> /etc/hosts
	root@verifier# echo 'verifier' > /etc/hostname
	```

	attestation requests are sent to the host named verifier.

2. 	go to `BASEDIR/verifier/OpenAttestation/Source` directory, run
	`distribute_jar_packages.sh`;

	```bash
	root@verifier# cd BASEDIR/verifier/OpenAttestation/Source
	root@verifier# bash distribute_jar_packages.sh
	```

3. 	go to `BASEDIR/verifier/OpenAttestation/Installer` directory, run `rpm.sh` to
	compile the OAT-appraiser package;

	```bash
	root@verifier# cd BASEDIR/verifier/OpenAttestation/Installer
	root@verifier# sh rpm.sh -s BASEDIR/verifier/OpenAttestation/Source
	```
	exactly from this directory, otherwise it does not work.

4.	install the package of `/root/rpmbuild/RPMS/x86_64/OAT-Appraiser-Base-OATapp-1.0.0-2.el7.centos.x86_64.rpm`;

	``` bash
	root@verifier# systemctl start mariadb
	root@verifier# systemctl enable mariadb
	root@verifier# cd /root/rpmbuild/RPMS/x86_64/
	root@verifier# yum localinstall OAT-Appraiser-Base-OATapp-1.0.0-2.el7.centos.x86_64.rpm
	root@verifier# systemctl daemon-reload
	```
	run this step only when mariadb service is running, because during installation phase, OAT will create database `oat_db` in mariadb.

5.	go to `BASEDIR/verifier/OpenAttestation/CommandTool` directory, and generate the CA certificate which will be used to access the OpenAttestation's services;

	```bash
	user@verifier$ cd BASEDIR/verifier/OpenAttestation/CommandTool
	user@verifier$ bash oat_cert -h verifier
	```

6.	and configure OpenAttestation with the `configure_oat.sh` following this format;

	``` bash
	user@verifier$ bash configure_oat.sh $selfname $attestorname $attestorIP $PCR0value $OSdistname $RApath $DBIP $CERTDGST
	```

	example:

	```bash
	bash configure_oat.sh verifier ned xxx.xxx.xxx.xxx 7D94A15BE0295A3743FC259B07202FF42550B369 CentOS7 /root/ratools-tclouds/verifier/v2/ra_verifier.py xxx.xxx.xxx.xxx 8b71648e9c52a24cfe259305c611483ea56ca4dc
	```

	$selfname is 'verifier' by default, it is the host accepting the attestation requests

	$attestorname is the attestor's hostname, which will be used in the attestation requests

	$attestorIP is the IP address of the attestor, which will be linked the $attestorname

	$PCR0value is the value in the PCR0 slot in the TPM, which is used as a golden value with VALIDATE_PCR command

	$OSdistname is the distribution of the OS running in the attestor, which will be used in the attestation analysis

	$RApath is the path to the ra_verifier.py script, which is used to analyse the IMA measurements

	$DBIP is the ip of the reference database, if the database is running inside the same machine, please just put `localhost`

	$CERTDGST is the SHA1 digest of the file containing the strongSwan certificate used for NED to authenticate itself (i.e. peerCert.der)

7. 	open ports for receiving/sending integrity reports, default ports are 80 and 8443

	``` bash
	root@verifier# firewall-cmd --permanent --add-port=80/tcp
	root@verifier# firewall-cmd --add-port=80/tcp
	root@verifier# firewall-cmd --permanent --add-port=8443/tcp
	root@verifier# firewall-cmd --add-port=8443/tcp
	```

8. 	change `/etc/oat-appraiser/OAT.properties` to store integrity reports in files, receive delta reports and discard identical integrity reports;

	uncomment IR_DIR, IR_DIGEST_METHOD, SCALABILITY, DISCARD_IDENTICAL_IR

9. 	to check if the verifier is working, use a browser to access the verifier's reference portal in the following link address:

	`http://verifier/OAT/alerts.php`

	In case of 403 Forbidden error, needs to change the permission of `/var/www/html/OAT`.

10. in this step, ned need to be configured;

	read guidelines in ned repo.

11. install cassandra reference database;

	```bash
	root@verifier# cd BASEDIR/verifier/db/install
	root@verifier# tar -xvzf apache-cassandra-1.2.19-bin.tar.gz
	root@verifier# ./install_cassandra_libs.sh BASEDIR/verifier/db/install/apache-cassandra-1.2.19
	```

12. initialise the reference database with the schema used to store the information;

	```bash
	root@verifier# cd BASEDIR/verifier/db/install/apache-cassandra-1.2.19/bin
	root@verifier# ./cassandra > /dev/null
	root@verifier# ./cassandra-cli -h localhost -f BASEDIR/verifier/db/install/cassandra/schema/cassandra-schema-common.txt
	root@verifier# ./cassandra-cli -h localhost -f BASEDIR/verifier/db/install/cassandra/schema/cassandra-schema-rpm.txt
	```

13. copy configuration files into `/etc/ra`;

	```bash
	root@verifier# mkdir /etc/ra
	root@verifier# cp BASEDIR/verifier/db/conf/pkgs_download_list.conf.sample /etc/ra/pkgs_download_list.conf
	root@verifier# cp BASEDIR/verifier/db/conf/ra.conf.sample /etc/ra/ra.conf
	```
RABASEDIR in ra.conf needs to be changed to `BASEDIR/verifier`

14. create `Packages` directory, go to `scripts` directory and run `update_pkgs.sh`;

	```bash
	root@verifier# mkdir BASEDIR/verifier/Packages
	root@verifier# cd BASEDIR/verifier/db/scripts
	root@verifier# bash update_pkgs.sh
	```
15. when the database is created, please use the `ra_verifier.py` script to test it;

	```bash
	root@verifier# cd BASEDIR/verifier/v2
	root@verifier# ./ra_verifier.py -i BASEDIR/verifier/db/measurements/ascii_runtime_measurements -q CentOS7 -a "load-time,l_req=l4|>=" -v -H localhost
	```
Should see information like following:
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

16. start the command in CommandTool to poll the integrity reports and verify it as defined in the configure.sh script;

	``` bash
	root@verifier# bash oat_pollhosts -h verifier '{"hosts":["ned"],"analysisType":"load-time+check-cert,l_req=l4_ima_all_ok|==,cert_digest=095b7792c076d65a9c45f4f484d06cd1fa29a9ba"}'
	```

17. if returned result is 'untrusted', which means the attestation feature is actually working, but there are some unknown digests in the IMA measurement list. In order to see which are unknown digests, run the following command:

	```python
	URL=https://verifier:8443/HisWebServices/hisDownloadReportService?wsdl IR=177 OS=CentOS7 /BASEDIR/verifier/v2/ra_verifier.py -H localhost -a "load-time+check-cert,l_req=l4_ima_all_ok|==,cert_digest=095b7792c076d65a9c45f4f484d06cd1fa29a9ba" -v
	```
You need to change the IR to the id received in the previous command (i.e. pollhosts) and also the cert_digest to the one measured in the NED.
For unknown digests, two possible solutions. First, insert unknown digests in the whilelist, which is stored in ``/BASEDIR/verifier/v2/structs.py`, called known_digests. If multiple unknown digests are from a same package, which is not installed from the official repository, then you can insert the package manually as a 'testing' package with following command:
	```bash
	user@verifier$ bash /BASEDIR/verifier/db/scripts/update_pkgs.sh -d temp/ -t testing -n CentOS -q 7 -c x86_64
	```
Where `temp` directory is used for storing the testing packages.

18. to update the certificate used by strongSwan in the NED, the information of this NED needs to be updated;

	```bash
	root@verifier:# bash update_cert.sh $selfname $attestorname $attestorIP $OSdistname $CERTDGST
	```
example: 
    ```bash 
	user@verifier$ update_cert.sh verifier ned xxx.xxx.xxx.xxx CentOS7 8b71648e9c52a24cfe259305c611483ea56ca4dc
    ```

19. to configure periodic attestation task; first need to configure `rabbitmq-server`

	```bash
	root@verifier:# rabbitmqctl add_user user secured
	root@verifier:# rabbitmqctl add_vhost uservhost
	root@verifier:# rabbitmqctl set_permissions -p uservhost user ".*" ".*" ".*"
	root@verifier:# systemctl enable rabbitmq-server
	root@verifier:# systemctl start rabbitmq-server
	```
If you start the `rabbitmq-server`, your rabbit node should now be rabbit@myhost, as verified by _rabbitmqctl_:
	```bash
	root@verifier:# rabbitmqctl status
	```
If you need to stop the rabbitmq server, just run:
	```bash
	root@verifier:# rabbitmqctl stop
	```

20. after `rabbitmq-server` is running, you can configure Celery in `/BASEDIR/verifier/ram/config.py` and `/BASEDIR/verifier/ram/celeryconfig.py`.
In `celeryconfig.py`, you can change the periodic attestation frequency. In `config.py`, you can change the OpenAttestation related parameters, especially `OAT_NODE`, `OAT_VERIFIER` and `OAT_LEVEL`. Also, the new certificate generated by OpenAttestation (i.e. certfile.cer) needs to be copied from the `BASEDIR/verifier/OpenAttestation/CommandTool` into `data` directory to replace the old one.
Then copy `/BASEDIR/verifier/ram` to `/home/user/ram` and start the periodic task with user account.

	```bash
	root@verifier:# cp /BASEDIR/verifier/OpenAttestation/CommandTool/certfile.cer /BASEDIR/verifier/ram/data/certfile.cer
	root@verifier:# cp -r /BASEDIR/verifier/ram /home/user/ram
	root@verifier:# su user
	user@verifier:$ cd /home/user/ram
	user@verifier:$ celery -A tasks worker --beat &
	```
In order for OpenAttestation to know the certificate used by strongswan in the NED to authenticate itself, when the NED is registering to the verifier, it also needs to input the digest of the file containing his certificate (i.e. [`peerCert.der`](https://gitlab.secured-fp7.eu/secured/ned/tree/strongswan/strongswan) step 6 in NED repository) along with it, see [step 7](https://gitlab.secured-fp7.eu/secured/verifier/blob/devel/README.md) in verifier repository.
When NED revokes its certificate, it needs to be re-registered again, with the digest of the certificate, with the _update_cert.sh_ script in `/BASEDIR/verifier/OpenAttestation/CommandTool` directory.
	
21. The web service created by OpenAttestation, running by _httpd_, the configuration files are in `/etc/httpd/conf.d`, need to change `ssl.conf` by adding new ServerName attribute `ServerName verifier:443`, and need to copy `tossl.conf` to the same `/etc/httpd/conf.d` directory. And the web page for user to read the attestation result changes to _https://verifier/OAT/result.php?CN=ned2&LEVEL=4&DGST=8b71648e9c52a24cfe259305c611483ea56ca4dc_, it will provide the same result as it was. 
The REST API has also changed from `http` to `https`, the new URL to the REST API is `https://verifier/OAT/attest.php`.

22. if OpenAttestation has been installed and running correctly, just need to copy the new php files in the `/BASEDIR/verifier/OpenAttestation/Source/Portal` directory into `/var/www/html/OAT` directory.

23. in order to register multiple NEDs into this verifier, need to run the steps defined in `NED setup` in the NED README. Afterward, need to run `add_NED.sh` in the `/BASEDIR/verifier/OpenAttestation/CommandTool` directory as following.

	``` bash
	user@verifier$ bash add_NED.sh $selfname $attestorname $attestorIP $PCR0value $OSdistname $CERTDGST
	```
example: 
    ```bash 
    add_NED.sh verifier ned2 xxx.xxx.xxx.xxx 7D94A15BE0295A3743FC259B07202FF42550B369 CentOS7 8b71648e9c52a24cfe259305c611483ea56ca4dc
    ```	
Then the new NED's name needs to be inserted into the `OAT_NODE` variable in `BASEDIR/verifier/ram/config.py` file.

## Example
You need to change the ned's cert_digest.

Open _https://verifier/OAT/result.php?CN=ned2&LEVEL=4&DGST=8b71648e9c52a24cfe259305c611483ea56ca4dc_ with a browser to see the attestation result.

* CN is the common name of the NED
* LEVEL is the trust level of the requirement
* DGST is the digest of the strongSwan certificate used by the NED

Or send POST requests to `https://verifier/OAT/attest.php`:

	```bash
	user@verifier:$ PDATA='{"hosts":["ned"],"analysisType":"load-time+check-cert,l_req=l4_ima_all_ok|>=,cert_digest=efae492da504edea2c2358dea1fb1e6770780b6e"}'
	user@verifier:$ curl -XPOST -H "Content-Type:application/json" -d "$PDATA" https://verifier/OAT/attest.php
	```
You need to change the ned's cert_digest.
Response is a JSON message structed as following:
Responses will be a JSON message structured as follow:

```json
{
	"status": "success",
	"n_results": 1,
	"results":[
		{
			"trust_lvl": "trusted",
			"host_name": "ned"
		},
	]
}
```
## License 

    The MIT License (MIT)

    Copyright (c) 2015 TORSEC Group (http://security.polito.it)
                       Politecnico di Torino

    author:   Tao Su <tao.su@polito.it>

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
