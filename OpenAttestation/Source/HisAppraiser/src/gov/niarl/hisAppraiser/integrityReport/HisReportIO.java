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
package gov.niarl.hisAppraiser.integrityReport;

import gov.niarl.hisAppraiser.Constants;
import gov.niarl.hisAppraiser.util.HisUtil;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.InputMismatchException; 

import org.apache.log4j.Logger;

/**
 * This class manages the IO of the integrity report.
 * @author Nicola Barresi
 *
 */
public class HisReportIO {
	private static Logger logger = Logger.getLogger(HisReportIO.class);
	private static final String IRprefix = "report_log_";

	public static String readIR(long reportId, String reportString) {
		if (reportString == null)
			return "";

		/*
		 * For compatibility reason, the function checks if
		 * reportString contains report XML instead of the
		 * new syntax:
		 *     report_digest:<digest_method>:<digest_value>
		 */
		if (!reportString.startsWith("report_digest"))
			return reportString;

		String returnValue = null;
		try {
			String[] reportStringParts = reportString.split(":");
			if (reportStringParts.length != 3) {
				throw new Exception("readReportFromFile(): unexpected format of field 'report'");
			}
			String digestMethod = reportStringParts[1];
			String digestValue = reportStringParts[2];

			StringBuilder result = new StringBuilder();
			BufferedReader reader = null;
			MessageDigest md = MessageDigest.getInstance(digestMethod);

			String IRdir = Constants.IR_DIR;

			File file = new File(IRdir + IRprefix + reportId + ".xml");
			reader = new BufferedReader(new FileReader(file));

			String tmpString = null;
			while ((tmpString = reader.readLine()) != null) {
				result.append(tmpString);
				md.update(tmpString.getBytes(), 0, tmpString.length());
			}
			reader.close();

			if (!digestValue.equals(HisUtil.hexString(md.digest()))) {
				throw new InputMismatchException();
			}
			returnValue = result.toString();
		} catch (FileNotFoundException exception) {
			logger.error("readReportFromFile(): cannot find report file");
		} catch (IOException exception) {
			logger.error("readReportFromFile(): cannot read report file");
		} catch (NoSuchAlgorithmException exception) {
			logger.error("readReportFromFile(): cannot find requested digest method");
		} catch (InputMismatchException exception) {
			logger.error("readReportFromFile(): report digest does not match the expected one");
		} catch (Exception exception) {
			logger.error(exception.getMessage());
		}
		return returnValue;
	}

	public static String writeIR(long reportId, String reportString) {
		String returnValue = null;
		try {
			BufferedWriter IRBufferedWriter = null;
			MessageDigest md = null;

			String IRdir = Constants.IR_DIR;
			String digestMethod = Constants.IR_DIGEST_METHOD;

			if (IRdir == null)
				return reportString;

			if (!new File(IRdir).isDirectory())
				throw new FileNotFoundException("writeReportToFile(): cannot find directory " + IRdir);

			File IRfile = new File(IRdir + IRprefix + reportId + ".xml");
			IRBufferedWriter = new BufferedWriter(new FileWriter(IRfile));
			IRBufferedWriter.write(reportString);
			IRBufferedWriter.close();

			try {
				md = MessageDigest.getInstance(digestMethod);
			} catch (NoSuchAlgorithmException ex) {
				logger.info("writeReportToFile(): requested digest method (" + digestMethod + ") does not exist");
				digestMethod = "SHA-256";
				md = MessageDigest.getInstance(digestMethod);
			}
			md.update(reportString.getBytes(), 0, reportString.length());
			returnValue = "report_digest:" + digestMethod + ":" + HisUtil.hexString(md.digest());
		} catch (FileNotFoundException exception) {
			logger.error(exception.getMessage());
		} catch (Exception exception) {
			logger.error("writeReportToFile(): a problem occurred writing report to file");
		}
		return returnValue;
	}
}
