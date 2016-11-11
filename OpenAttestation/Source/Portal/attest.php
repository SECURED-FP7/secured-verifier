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

	include("includes/wsutils.php");

	$headers = apache_request_headers();
	$handle = fopen("php://input", "rb");

	$http_raw_post_data = '';
	while (!feof($handle)) {
		$http_raw_post_data .= fread($handle, 443);
	}
	fclose($handle);

	$post_data = json_decode($http_raw_post_data,true);

	if (is_array($post_data) and (strcasecmp($headers["Content-Type"], "application/json") == 0)) {
		$response = array("status" => "success", "code" => 200);
		$analysis = explode(",", $post_data["analysisType"]);

		$cert = "";
		if (stristr($post_data["analysisType"],"check-cert")){
			$cert = explode("=", $analysis[2])[1];
		}

		$req_level = explode("|", explode("=l", $analysis[1])[1])[0];
		$result = doAnalysis($post_data["hosts"], $cert, $req_level);
		$response["results"] = $result;
	} else {
		$response = array("status" => "error", "code" => 400, "msg" => "malformed body");
	}

	echo json_encode($response);

?>
