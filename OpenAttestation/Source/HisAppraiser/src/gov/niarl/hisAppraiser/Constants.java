/*
 * (copyright) 2012 United States Government, as represented by the 
 * Secretary of Defense.  All rights reserved.
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
package gov.niarl.hisAppraiser;

import gov.niarl.hisAppraiser.util.AlertConfiguration;
import gov.niarl.hisAppraiser.util.Emailer;

import java.io.IOException;
import java.util.Properties;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import javax.mail.internet.InternetAddress;

import org.apache.log4j.Logger;
import org.hibernate.util.ConfigHelper;

public class Constants {
	private static Logger logger = Logger.getLogger(Constants.class);
	/**
	 * Create properties object using location of properties file.
	 */
	private static Properties properties = loadProperties("/etc/oat-appraiser/OAT.properties");

	/**
	 * Determines where to place integrity reports
	 */
	public static final String IR_DIR = (getProperty("IR_DIR") == null) ? null : (getProperty("IR_DIR") + "/").replace("//", "/");

	/**
	 * Get the digest algorithm to use to check the integrity of reports 
	 */
	public static final String IR_DIGEST_METHOD = (getProperty("IR_DIGEST_METHOD") == null) ? "SHA-256" : getProperty("IR_DIGEST_METHOD");

	/** 
	 * Returns true if the SCALABILITY property is set to "on";
	 * returns false otherwise.
	 */
	public static final boolean SCALABILITY = (getProperty("SCALABILITY") != null && getProperty("SCALABILITY").equals("on")) ? true : false;

	/** 
	 * Returns true if the DISCARD_IDENTICAL_IR property is set to "on";
	 * returns false otherwise.
	 */
	public static final boolean DISCARD_IDENTICAL_IR = (getProperty("DISCARD_IDENTICAL_IR") != null && getProperty("DISCARD_IDENTICAL_IR").equals("on")) ? true : false;

	/**
	 * Determines which alerts to generate. 
	 */
	static String ALERT_MASK_CSV = getProperty("ALERT_MASK_CSV");
	public static final AlertConfiguration ALERT_CONFIGURATION = new AlertConfiguration(ALERT_MASK_CSV == null ? "0":ALERT_MASK_CSV);
	/**
	 * Determines the PCR select for integrity reports. 
	 */
	public static final String PCR_SELECT = getProperty("PCR_SELECT");
	/**
	 * JavaMail API Mail Properties
	 */
	public static final Properties MAIL_SERVER_PROPERTIES = Emailer.parseMailServerProperties(getProperties());
	/**
	 * List of addresses to which to send administrative email.
	 */
	public static final InternetAddress[] ALERT_MESSAGE_TO = Emailer.parseDefaultAlertMessageTo(getProperty("alert.message.to"));
	/**
	 * Subject of the default email.
	 */
	public static final String ALERT_MESSAGE_SUBJECT = getProperty("alert.message.subject");
	/**
	 * Body of the default email.
	 */
	public static final String ALERT_MESSAGE_BODY = getProperty("alert.message.body");

	public static final long PERIODIC_TIME_EXPIRED = -1;
	public static final long PERIODIC_IDLE_EXPIRED = -2;
	public static final long PERIODIC_DELETED_BY_USER = -3;
	public static final long PERIODIC_HOST_UNTRUSTED = -4;
	public static final long PERIODIC_HOST_UNREACHABLE = -5;

	/**
	 * Creates properties object from file name.
	 */
	private static Properties loadProperties(String file) {
                try {
		        FileInputStream  PropertyFile = new FileInputStream(file);
                        Properties SetupProperties = new Properties();
                        SetupProperties.load(PropertyFile);
                        return SetupProperties;
		} catch (IOException e) {
			logger.fatal(e, e);
			throw new RuntimeException(e);
		}
	}

	/**
	 * Return the entire properties object created above.
	 * @return
	 */
	private static Properties getProperties() {
		return properties;
	}

	/**
	 * Retrieve a property using the property name.
	 * @param key Property name.
	 * @return property value.
	 */
	private static String getProperty(String key) {
		return properties.getProperty(key);
	}
}
