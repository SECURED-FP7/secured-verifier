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

if(isset($_GET["id"]) && is_numeric($_GET["id"]))
{
$id = $_GET["id"];
}
else
{
//STOP EXECUTION IF THERE IS A PROBLEM
die("Error: Invalid ID.");
}

//REPORTS ARE IN XML FORMAT SO MAKE SURE THE USER'S BROWSER KNOWS THAT
//header ("Content-Type:text/xml");

//INCLUDE FUNCTION getReport() FOR READING REPORT FROM WEB SERVICE
include("includes/wsutils.php");

//GET THE REPORT FROM THE WEB SERVICE
try {
	$result = getReport($id);
} catch(SoapFault $fault) {
	header("Content-Type:text");

	if ($fault->faultstring == "Not Found") {
		echo "<h1>" . $fault->faultstring . "</h1>";
		header('HTTP/1.0 404 Not Found');
		echo "<p>The requested report (" . $id . ") does not exist.</p>";
	} else if ($fault->faultstring == "Internal Server Error") {
		echo "<h1>" . $fault->faultstring . "</h1>";
		header('HTTP/1.0 500 Internal Server Error');
		echo "<p>An error occurred while retrieving requested report (" . $id . ").</p>";
	} else {
		echo "<h1>SOAP Exception</h1>";
		echo "<p>" . $fault->faultstring . "</p>";
	}
	echo "<hr><address>Apache Server at " . $_SERVER['HTTP_HOST'] . " Port " . $_SERVER['SERVER_PORT'] . "</address>";
	exit();
}

foreach ($result as $key=>$value) {
	if ($key == 'reportString') {
		$xml = simplexml_load_string("$value");
		$values = $xml->xpath("/*[local-name()='Report']/*[local-name()='SnapshotCollection']/*[local-name()='Values']");

		echo "<h1>Integrity Report </h1>";
		foreach ( $values as $value_list ) {
			$type = $value_list->xpath("//*[local-name()='SimpleObject']/*[local-name()='Objects']/@Type");
			$image = $value_list->xpath("//*[local-name()='SimpleObject']/*[local-name()='Objects']/@Image");
			#$dgst = $value_list->xpath("//*[local-name()='SimpleObject']/*[local-name()='Objects']/*[local-name()='Hash']/text()");

			for($x = 0; $x < count($image); $x++) {
				if ($type[$x] == "ima"){
					$binary = base64_decode($image[$x]);
					#$imageDgst = base64_decode($imageDgst64[$x]);
					# hex data seems correct, but it look like unrelevant.
					#$hex = bin2hex($imageDgst);
					$dgst = substr($binary, 0, 20);
					$dgsthex = bin2hex($dgst);
					$name=substr($binary, 20);
					echo "<h2>" . $name . "</h2>";
					echo "<h3> ". $dgsthex . "</h3><br><br>";
				}
			}
			break;
		}
		break;
	}
}

# here to find the id of the file and write it in the web page.
$unknow_dgsts = getUnknownDigests($id);
if (count($unknow_dgsts) > 0)
	echo "<h1>unknown digests</h1>";
foreach ($unknow_dgsts as $line){
	$image = explode(" ", $line);
	if(stristr($image[1],"Digest")) {
		$binary_name = rtrim(ltrim($image[3],'('),')');
		$hex = $image[2];
		echo "<h2 style='color:red'>" . $binary_name . "</h2>";
		echo "<h3 style='color:red'>" . $hex . "</h3>";
	}
}
?>
