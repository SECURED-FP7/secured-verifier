<?php
/*
 * (copyright) 2012 United States Government, as represented by the
 * Secretary of Defense.  All rights reserved.
 *
 * (copyright) 2013 Politecnico di Torino, Italy
 *                  TORSEC group -- http://security.polito.it
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 * - Redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer.
 *
 * - Redistributions in binary form must reproduce the above copyright
 * notice, this list of conditions and the following disclaimer in the
 * documentation and/or other materials provided with the distribution.
 *
 * - Neither the name of the U.S. Government nor the names of its
 * contributors may be used to endorse or promote products derived from
 * this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
 * OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
 * AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY
 * WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */


function getReport($id) {
	$server = 'localhost';

	$client = new SoapClient("https://$server:8443/HisWebServices/hisDownloadReportService?wsdl",
	                         array('cache_wsdl' => WSDL_CACHE_NONE));
	return $client->fetchReport(array('reportId' => $id, 'partial' => true));
}

function getUnknownDigests($id){
	$log_dir = '/var/www/html/OAT/unknown_log';
	$log_unknown = fopen($log_dir."/unknown_log_". $id, "r") or die("Unable to open file!");
	$unknow_dgsts=array();
	while (($line = fgets($log_unknown)) !== false) {
		if ((strpos($line,'Info: Digest ') !== false) or (strpos($line,'Info: load') !== false)) {
			array_push($unknow_dgsts,$line);
		}
	}
	fclose($log_unknown);
	return $unknow_dgsts;
}

function doAnalysis($hosts, $req_cert, $req_level){
	include("includes/dbconnect.php");
	date_default_timezone_set('Europe/Rome');

	// for each host in hosts
	$results=array();

	$count = 0;
	foreach( $hosts as $host ) {
		$result = mysql_query("select host_name, analysis_request, analysis_results, validate_time from attest_request where host_name='$host' ORDER BY validate_time DESC LIMIT 1;");
		$cert = mysql_query("select host_name, description from HOST where host_name='$host';");
		$reports = mysql_query("select id, machine_name from audit_log where machine_name='$host' ORDER BY id DESC LIMIT 1;");

		if (!$result or !$cert or !$reports) {
			die('Invalid query: ' . mysql_error());
		} else{
			//$results = array();
			$row = mysql_fetch_array($result);
			$cert = mysql_fetch_array($cert);
			$report = mysql_fetch_array($reports);

			if(empty($row['host_name']) or empty($cert['host_name']) or empty($report['machine_name'])){
				$_r = array(
					"host_name" => $host,
					"trust_lvl" => "unknown",
				);
			} else {
				$analysis_results = $row['analysis_results'];
				$validate_time = strtotime($row['validate_time']);
				$now = strtotime(date('Y-m-d H:i:s'));
				$diff = $now - $validate_time;

				$unknow_dgsts = getUnknownDigests($report["id"]);
				foreach ($unknow_dgsts as $line){
					$image = explode(" ", $line);
					if(stristr($image[1],"load)")){
						$res_level = $image[3];
					} else {
						$res_level = 4;
					}
				}
				$_r = array(
					"host_name" => $host,
				);
				if (strcmp($req_cert, $cert['description'])!=0) {
					$_r["trust_lvl"] = "cert-err";
				} else if ($diff > 30) {
					$_r["trust_lvl"] = "vtime-err";
				} else if (((stristr($row['analysis_results'], "|true|")) and (stristr($row['analysis_results'],"|ANALYSIS_COMPLETED|0|"))) or $LEVEL<=$res_level) {
					$_r["trust_lvl"] = "trusted";
				} else {
					$_r["trust_lvl"] = "untrusted";
				}
				$_r["validate_time"] = $row["validate_time"];

			}
		}
		$results[$count] = $_r;
		$count++;
	}
	include("includes/dbclose.php");

	return $results;
}


?>
