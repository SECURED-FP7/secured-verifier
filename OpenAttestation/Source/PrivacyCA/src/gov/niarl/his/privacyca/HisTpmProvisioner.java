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

package gov.niarl.his.privacyca;

import gov.niarl.his.privacyca.TpmModule.TpmModuleException;
import gov.niarl.his.webservices.hisPrivacyCAWebService2.IHisPrivacyCAWebService2;
import gov.niarl.his.webservices.hisPrivacyCAWebService2.client.HisPrivacyCAWebServices2ClientInvoker;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.File;
import java.io.FileOutputStream;

import java.security.NoSuchAlgorithmException;
import java.security.Security;
import java.security.PublicKey;
import java.security.cert.CertificateEncodingException;
import java.security.cert.X509Certificate;
import java.util.Properties;

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.security.cert.CertificateException;
import java.security.interfaces.RSAPublicKey;  

import org.bouncycastle.jce.provider.BouncyCastleProvider;

/**
 * <p>This is part 1 of 3 for fully provisioning HIS on a Windows client. This class does the initial provisioning of the TPM.</p>
 * This provisioning includes:
 * <ul>
 * <li>Taking ownership of the TPM</li>
 * <li>Creating an Endorsement Certificate</li>
 * <li>Storing the Endorsement Certificate in the TPM's NVRAM</li>
 * </ul>
 * 
 * <p>This class utilizes a properties file. It looks for a file by the name of "HISprovisioner.properties" in the directory from which Java was invoked.</p>
 * The following values must be in the properties file:<br>
 * <ul>
 * <li><b>TpmEndorsmentP12</b></li>
 * <li><b>EndorsementP12Pass</b></li>
 * <li><b>EcValidityDays</b></li>
 * <li><b>TpmOwnerAuth</b> This must be a 40 digit (20 byte) hex code representing the owner auth data to be assigned.</li>
 * </ul>
 * 
 * @author schawki
 *
 */
public class HisTpmProvisioner {

	/**
	 * Entry point into the program
	 */
	public static void main(String[] args){// throws InvalidKeyException, CertificateEncodingException, UnrecoverableKeyException, NoSuchAlgorithmException, InvalidKeySpecException, SignatureException, NoSuchProviderException, KeyStoreException, CertificateException, IOException, javax.security.cert.CertificateException {
		//get properties file info
		final String EC_VALIDITY = "EcValidityDays";
		final String OWNER_AUTH = "TpmOwnerAuth";
		final String PRIVACY_CA_URL = "PrivacyCaUrl";
		final String TRUST_STORE = "TrustStore";
		final String EC_STORAGE = "ecStorage";
		final String PRIVACY_CA_CERT = "PrivacyCaCertFile";
		final String propertiesFileName = "OATprovisioner.properties";
		final String ecStorageFileName = "EC.cer";
		int EcValidityDays = 0;
		byte [] TpmOwnerAuth = null;
		byte [] encryptCert = null;
		byte [] pubEkMod = null;
		String TrustStore = "";
		String ecStorage = "";
		String PrivacyCaCertFile = "";
		String PrivacyCaUrl = "";
		X509Certificate pcaCert = null;
		PublicKey publicKey = null;
		FileInputStream PropertyFile = null;
		
		try {
			PropertyFile = new FileInputStream(System.getProperty("user.dir") + System.getProperty("file.separator") + propertiesFileName);
			Properties HisProvisionerProperties = new Properties();
			HisProvisionerProperties.load(PropertyFile);		
			EcValidityDays = Integer.parseInt(HisProvisionerProperties.getProperty(EC_VALIDITY, ""));
			TpmOwnerAuth = TpmUtils.hexStringToByteArray(HisProvisionerProperties.getProperty(OWNER_AUTH, ""));
			PrivacyCaUrl = HisProvisionerProperties.getProperty(PRIVACY_CA_URL, "");
			PrivacyCaCertFile = HisProvisionerProperties.getProperty(PRIVACY_CA_CERT, "");
			TrustStore = HisProvisionerProperties.getProperty(TRUST_STORE, "TrustStore.jks");
			ecStorage = HisProvisionerProperties.getProperty(EC_STORAGE, "NVRAM");
			//TODO, it not a good manner to always print out the message into console
			//keep here as it will help user get some direct message
            System.out.println("### ecStorage = "  + ecStorage + "###");
		} catch (FileNotFoundException e) {
			System.out.println("Error finding HIS Provisioner properties file (OATprovisioner.properties)");
		} catch (IOException e) {
			System.out.println("Error loading HIS Provisioner properties file (OATprovisioner.properties)");
		}
		catch (NumberFormatException e) {
			e.printStackTrace();
		} finally{
			if (PropertyFile != null){
				try {
					PropertyFile.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
		String errorString = "Properties file \"" + propertiesFileName + "\" contains errors:\n";
		boolean hasErrors = false;
		if(EcValidityDays == 0){
			errorString += " - \"EcValidityDays\" value must be the number of validity days for the Endorsement Credential\n";
			hasErrors = true;
		}
		if(TpmOwnerAuth ==null || TpmOwnerAuth.length != 20){
			errorString += " - \"TpmOwnerAuth\" value must be a 40 hexidecimal digit (20 byte) value representing the TPM owner auth\n";
			hasErrors = true;
		}
		if(PrivacyCaCertFile.length() == 0){
			errorString += "There is a improper configuration within properties file, please check the file first\n";
			hasErrors = true;
		}
		if(hasErrors){
			System.out.println(errorString);
			System.exit(99);
			return;
		}
		
		//Provision the TPM
		System.out.print("Performing TPM provisioning...");
		
		/*
		 * The following actions must be performed during the TPM Provisioning process:
		 * 1. Take ownership of the TPM
		 * 		- owner auth
		 * 2. Create an Endorsement Certificate (EC)
		 * 		- public EK
		 * 			- owner auth (should already have from above)
		 * 		- private key and cert for CA to create new cert
		 * 		- validity period of EC cert 
		 * 3. Store the newly created EC in the TPM's NV-RAM
		 */
		SecretKey deskey = null;
		KeyGenerator keygen;
		Security.addProvider(new BouncyCastleProvider());
		// Take Ownership
		byte [] nonce = null;
		try {
			nonce = TpmUtils.createRandomBytes(20);
			TpmModule.takeOwnership(TpmOwnerAuth, nonce);
		} catch (TpmModuleException e){
		    if(e.toString().contains(".takeOwnership returned nonzero error: 4")){
		        System.out.println("Ownership is already taken");
		        } else {
		            System.out.println("Error while taking ownership: " + e.toString());
		            System.exit(1);
		            }
		} catch (IOException e) {
			e.printStackTrace();
			System.exit(1);
		}
		
		// Generate security key via 3DES algorithm
		try {
			keygen = KeyGenerator.getInstance("DESede"); 
			deskey = keygen.generateKey();
		} catch (NoSuchAlgorithmException e) {
		    System.out.println("Error while generating 3DES key" + e.toString());
		    e.printStackTrace();
		    System.exit(1);
		} 
		
		// Create Endorsement Certificate
		try {
			nonce = TpmUtils.createRandomBytes(20);
			pubEkMod = TpmModule.getEndorsementKeyModulus(TpmOwnerAuth, nonce);
		} catch (TpmModuleException e){
			System.out.println("Error while getting PubEK: " + e.toString());
			System.exit(1);
		} catch (Exception e){
			System.out.println("Error while getting PubEK: " + e.toString());
			System.exit(1);
		}
		
		try {
			pcaCert = TpmUtils.certFromFile(PrivacyCaCertFile);
			if (pcaCert != null){
			publicKey = (RSAPublicKey)pcaCert.getPublicKey();
			}
		} catch (Exception e){
			System.out.println("Error while getting PCA public key: " + e.toString());
			System.exit(1);
		}
	
		
		System.setProperty("javax.net.ssl.trustStore", "./" + TrustStore);
		try {					
			IHisPrivacyCAWebService2 hisPrivacyCAWebService2 = HisPrivacyCAWebServices2ClientInvoker.getHisPrivacyCAWebService2(PrivacyCaUrl);
			encryptCert = hisPrivacyCAWebService2.requestGetEC(encryptDES(pubEkMod, deskey), encryptRSA(deskey.getEncoded(), publicKey), EcValidityDays);	
		} catch (Exception e){
			System.out.println("Failed to sign EC on PCA, error message is: " + e.getMessage());
			System.exit(1);
		}
		
		//Decrypt and generate endorsement certificate 
		X509Certificate ekCert = null;		
		try {
			if (encryptCert != null){
				ekCert = TpmUtils.certFromBytes(decryptDES(encryptCert, deskey));
			}
		} catch (java.security.cert.CertificateException e) {
		    System.out.println("Error while decrypting endorsement certificate, error message is: " + e.getMessage());
			System.exit(1);
		} catch (CertificateException e) {
			e.printStackTrace();
			System.exit(1);
		} catch (Exception e) {
			e.printStackTrace();
			System.exit(1);
		}
			
		// Store the new EC in NV-RAM
       if (ecStorage.equalsIgnoreCase("file")) {
    	   System.out.println("\n--store EC in file--");
    	   try{
                File ecFile = new File(System.getProperty("user.dir") + System.getProperty("file.separator") + ecStorageFileName);
                FileOutputStream ecFileOut = new FileOutputStream(ecFile);
                ecFileOut.write(ekCert.getEncoded());
                ecFileOut.flush();
                ecFileOut.close();
                } catch(Exception e) {
                   System.out.println("Failed to write EC into file, error message is: " + e.getMessage());
                   e.printStackTrace();
                   System.exit(1);
                }
       } else {
     		try{
     			TpmModule.setCredential(TpmOwnerAuth, "EC", ekCert.getEncoded());
     			System.out.println("The size of endorsement certificate: " + ekCert.getEncoded().length);
     		} catch (TpmModuleException e){
     			System.out.println("Error while seting credential: " + e.toString());
     			System.exit(1);
     		} catch (CertificateEncodingException e) {
                //TODO we'd better reduce the frequency of printing stack trace;
     		    e.printStackTrace();
     		    System.exit(1);
     		} catch (IOException e) {
     			e.printStackTrace();
     			System.exit(1);
     		}
        }
		System.out.println("DONE");
		return;
	}
	
	//we cannot always rely on JDK itself, specify the provide as "BC" to compatible with server side;
    private static byte[] encryptDES(byte[] text, SecretKey key) throws Exception {
    	Cipher c = Cipher.getInstance("DESede/ECB/PKCS7Padding", "BC");  
		c.init(Cipher.ENCRYPT_MODE, key);  
		return c.doFinal(text);
    }
    
    private static byte[] encryptRSA(byte[] text, PublicKey pubRSA) throws Exception {
    	Cipher cipher = Cipher.getInstance("RSA", "BC");
        cipher.init(Cipher.ENCRYPT_MODE, pubRSA);
        return cipher.doFinal(text);
    }
    
    private static byte[] decryptDES(byte[] text, SecretKey key) throws Exception {
    	Cipher cipher = Cipher.getInstance("DESede/ECB/PKCS7Padding", "BC");
        cipher.init(Cipher.DECRYPT_MODE, key);
        return cipher.doFinal(text);
    }
}
