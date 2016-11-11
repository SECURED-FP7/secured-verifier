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

$CN = $_GET['CN'];
$LEVEL = $_GET['LEVEL'];
$DGST = $_GET['DGST'];
date_default_timezone_set('Europe/Rome');

if(empty($CN) or empty($LEVEL) or empty($DGST)){
	echo "<h1> need all three paramters</h1>";
	exit (0);
}
?>

<?php
//CONNECT TO DATABASE
include("includes/dbconnect.php");
include("includes/wsutils.php");
?>

<?php
$result = mysql_query("select host_name, analysis_request, analysis_results, validate_time from attest_request where host_name='$CN' ORDER BY validate_time DESC LIMIT 1;");

$cert = mysql_query("select host_name, description from HOST where host_name='$CN';");
$reports = mysql_query("select id, machine_name from audit_log where machine_name='$CN' ORDER BY id DESC LIMIT 1;");

if (!$result or !$cert or !$reports) {
	die('Invalid query: ' . mysql_error());
} else{

	$row = mysql_fetch_array($result);
	$cert = mysql_fetch_array($cert);
	$report = mysql_fetch_array($reports);

	if(empty($row['host_name']) or empty($cert['host_name']) or empty($report['machine_name'])){
		echo "<h1> No record found for $CN </h1>";
	} else {
		$analysis_request = $row['analysis_request'];
		$host_name = $row['host_name'];
		$analysis_results = $row['analysis_results'];
		$validate_time = strtotime($row['validate_time']);
		$now = strtotime(date('Y-m-d H:i:s'));
		$diff = $now - $validate_time;

		$unknow_dgsts = getUnknownDigests($report["id"]);
		foreach ($unknow_dgsts as $line){
			$image = explode(" ", $line);
			if(stristr($image[1],"load)")){
				$res_level = $image[3];
			}
		}

		if (strcmp($DGST,$cert['description'])!=0) {
			echo "<h1 style='font-size:300%; color:red'> Certificates dismatch </h1>";
		} else if ($diff > 25 or empty($analysis_results)){
			echo "<h1 style='font-size:300%; color:red'> Stale result!</h1>";
			echo "<h1> Last validate on " . $row['validate_time'] . "</h1>";
		} else {
			if (((stristr($row['analysis_results'], "|true|")) and (stristr($row['analysis_results'],"|ANALYSIS_COMPLETED|0|"))) or $LEVEL<=$res_level){
				echo "<h1 style='font-size:200%; color:green'>" . $CN . " is TRUSTED!</h1>";
				echo "<h1> Last validate on " . $row['validate_time'] . "</h1>";
			} else {
				echo "<h1 style='font-size:300%; color:red'>" . $CN . " is UNTRUSTED!</h1>";
				echo "<h1> Last validate on " . $row['validate_time'] . "</h1>";
			}

			echo "<table>";
			echo "<tr>";
			echo "<td>" . $row['host_name'] . "</td>";
			echo "</tr>";

			echo "<tr>";
			echo "<td>" . $row['analysis_request'] . "</td>";
			echo "</tr>";

			echo "<tr>";
			echo "<td>" . $row['analysis_results'] . "</td>";
			echo "</tr>";

			echo "<tr>";
			echo "<td>" . $row['validate_time'] . "</td>";
			echo "</tr>";
			echo "</table>";
			echo "<a href=\"ir.php?id=" . $report["id"] . "\"> Integrity Report </a>";
		}
	}
}
?>

<?php
//CLOSE DATABASE CONNECTION
include("includes/dbclose.php");
?>
