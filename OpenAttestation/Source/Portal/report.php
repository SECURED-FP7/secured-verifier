<?php
/*2012, U.S. Government, National Security Agency, National Information Assurance Research Laboratory

This is a work of the UNITED STATES GOVERNMENT and is not subject to copyright protection in the United States. Foreign copyrights may apply.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

鈥�Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

鈥�Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

鈥�Neither the name of the NATIONAL SECURITY AGENCY/NATIONAL INFORMATION ASSURANCE RESEARCH LABORATORY nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.*/

//MAKE SURE THE ID IS SET AND IS A NUMBER
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
header ("Content-Type:text/xml");

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

//PRINT OUT ALL THE XML
foreach ($result as $key=>$value) {
	if ($key == 'reportString') {
		echo $value;
		break;
	}
}

?>
