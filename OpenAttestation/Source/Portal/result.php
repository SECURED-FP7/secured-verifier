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

if ($LEVEL > 4){
	echo "<h1> invalid level requirement, maximum trust level is 4";
	exit(0);
}
?>

<head>
<title>Attestation Result of <?php echo $CN; ?> </title>

</head>
<body>

<div class="general">
	<p style="float: right;">
		<img  style="width:500px;position:static;top=500px" src="images/secured_logo.png" alt="secured_logo" ></img>
	</p>
<p style="float: left;">
	<h1><span style="bold;"> NED name: <?php echo $CN?></span></h1>
      <br>
      <h1><span style="bold">Required trust level: L<?php echo $LEVEL?></span></h1>
      <br>
      <h1><span style="bold">Received certificate digest (SHA1): <br> <?php echo $DGST?></span></h1>
      <br>
</p>
</div>



<script>

			var showAlert = true;
      function getResult(cn, level, dgst) {
            var xhttp;
            if (window.XMLHttpRequest) {
                  // code for modern browsers
                  xhttp = new XMLHttpRequest();
            } else {
                  // code for IE6, IE5
                  xhttp = new ActiveXObject("Microsoft.XMLHTTP");
            }
            xhttp.onreadystatechange = function() {
                  if (xhttp.readyState == 4 && xhttp.status == 200) {
                        document.getElementById("status").innerHTML = xhttp.responseText;
                        if(((xhttp.responseText.search("is UNTRUSTED")>0) || (xhttp.responseText.search("Certificates dismatch")>0) || (xhttp.responseText.search("Stale result")>0)) && showAlert) {
																showAlert = false;
                              	alert("NED is compromised, suggest to disconnect!");
                        } else if (xhttp.responseText.search("is TRUSTED")>0) {
																showAlert = true;
												}
                  }
            }
            xhttp.open("GET", "ajax_load.php?CN="+cn+"&LEVEL="+level+"&DGST="+dgst, true);
            xhttp.send();
      }



      document.addEventListener("DOMContentLoaded",
            function() {
                  getResult("<?php echo $CN;?>", "<?php echo $LEVEL;?>", "<?php echo $DGST;?>");
                  setInterval(function() {
                        getResult("<?php echo $CN;?>", "<?php echo $LEVEL;?>", "<?php echo $DGST;?>");
            }, 5000);
      });
</script>


<div id='status'>

</div>
</body>
