/*
 * 2012, U.S. Government, National Security Agency, National Information Assurance Research Laboratory
 * 
 * This is a work of the UNITED STATES GOVERNMENT and is not subject to copyright protection in the United States. Foreign copyrights may apply.
 * 
 * Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
 * �Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. 
 * �Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. 
 * �Neither the name of the NATIONAL SECURITY AGENCY/NATIONAL INFORMATION ASSURANCE RESEARCH LABORATORY nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

package gov.niarl.his.webservices.hisPrivacyCAWebService2.server;

import gov.niarl.his.webservices.hisPrivacyCAWebService2.IHisPrivacyCAWebService2;

import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebResult;
import javax.jws.WebService;
import javax.xml.ws.soap.Addressing;

import com.sun.xml.ws.developer.Stateful;
import com.sun.xml.ws.developer.StatefulWebServiceManager;

@Stateful
@WebService
@Addressing
public class HisPrivacyCAWebService2 {
	/**
	 * Needed for stateful web services. StatefulWebServiceManager javadoc
	 */
	public static StatefulWebServiceManager<HisPrivacyCAWebService2> manager;

	IHisPrivacyCAWebService2 hisPrivacyCAWebService2 = new HisPrivacyCAWebService2Impl();

	@WebResult(name = "identityRequestChallenge")
	public ByteArray identityRequestGetChallenge(@WebParam(name = "identityRequest") ByteArray identityRequest, @WebParam(name = "endorsementCertificate") ByteArray endorsementCertificate) {
		return new ByteArray(hisPrivacyCAWebService2.identityRequestGetChallenge(identityRequest.getBytes(), endorsementCertificate.getBytes()));
	}

	@WebResult(name = "encryptedCertificate")
	public ByteArray identityRequestSubmitResponse(@WebParam(name = "identityRequestResponseToChallenge") ByteArray identityRequestResponseToChallenge) {
		try {
			return new ByteArray(hisPrivacyCAWebService2.identityRequestSubmitResponse(identityRequestResponseToChallenge.getBytes()));
		} finally {
			manager.unexport(this);
		}
	}

	@WebMethod(exclude = true)
	public static StatefulWebServiceManager<HisPrivacyCAWebService2> getManager() {
		return manager;
	}

	@WebMethod(exclude = true)
	public static void setManager(StatefulWebServiceManager<HisPrivacyCAWebService2> manager) {
		HisPrivacyCAWebService2.manager = manager;
	}
	
	@WebResult(name = "requestGetEC")
	public ByteArray requestGetEC(@WebParam(name = "encryptedEkMod") ByteArray encryptedEkMod, ByteArray encryptedSessionKey, int ecValidDays) {
		return new ByteArray(hisPrivacyCAWebService2.requestGetEC(encryptedEkMod.getBytes(), encryptedSessionKey.getBytes(), ecValidDays));}

}