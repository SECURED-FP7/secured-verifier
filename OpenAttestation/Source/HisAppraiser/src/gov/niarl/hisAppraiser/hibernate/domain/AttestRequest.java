/*
Copyright (c) 2012, Intel Corporation
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
    * Neither the name of Intel Corporation nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

package gov.niarl.hisAppraiser.hibernate.domain;

import gov.niarl.hisAppraiser.hibernate.domain.AuditLog;
import gov.niarl.hisAppraiser.hibernate.domain.MachineCert;
import java.util.Date;
import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement
public class AttestRequest {
	
	private Long id;
	
	private String requestId;
	
	private String hostName;
	
	private Date requestTime;
	
	private Integer nextAction;
	
	private Boolean isConsumedByPollingWS;
	
	private AuditLog auditLog;
	
	private MachineCert machineCert;
	
	private String requestHost;
	
	private Long count;
	
	private String PCRMask;
	
	private Boolean isSync;
	
	private Integer result;
	
	private Date validateTime; 
	
	private String analysisRequest;

	private String analysisResults;

	private Long threshold;

	private Date expirationTime; 

	private Date lastReadTime; 

	private Long currentProcessingTime; 

	public Date getValidateTime() {
		return validateTime;
	}

	public void setValidateTime(Date validateTime) {
		this.validateTime = validateTime;
	}

	public AttestRequest(){
		
	}
	
	public Boolean getIsSync() {
		return isSync;
	}


	public void setIsSync(Boolean isSync) {
		this.isSync = isSync;
	}

	public Long getCount() {
		return count;
	}

	public void setCount(Long count) {
		this.count = count;
	}


	public String getPCRMask() {
		return PCRMask;
	}

	public void setPCRMask(String pCRMask) {
		PCRMask = pCRMask;
	}

	public Integer getResult() {
		return result;
	}

	public void setResult(Integer result) {
		this.result = result;
	}

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getRequestId() {
		return requestId;
	}

	public void setRequestId(String requestId) {
		this.requestId = requestId;
	}

	
	
	public String getHostName() {
		return hostName;
	}

	public void setHostName(String hostName) {
		this.hostName = hostName;
	}

	public Date getRequestTime() {
		return requestTime;
	}

	public void setRequestTime(Date requestTime) {
		this.requestTime = requestTime;
	}

	

	public Integer getNextAction() {
		return nextAction;
	}

	public void setNextAction(Integer nextAction) {
		this.nextAction = nextAction;
	}

	public Boolean getIsConsumedByPollingWS() {
		return isConsumedByPollingWS;
	}

	public void setIsConsumedByPollingWS(Boolean isConsumedByPollingWS) {
		this.isConsumedByPollingWS = isConsumedByPollingWS;
	}

	public AuditLog getAuditLog() {
		return auditLog;
	}

	public void setAuditLog(AuditLog auditLog) {
		this.auditLog = auditLog;
	}

	public MachineCert getMachineCert() {
		return machineCert;
	}

	public void setMachineCert(MachineCert machineCert) {
		this.machineCert = machineCert;
	}

	public String getRequestHost() {
		return requestHost;
	}

	public void setRequestHost(String requestHost) {
		this.requestHost = requestHost;
	}

	public String getAnalysisRequest() {
		return analysisRequest;
	}

	public void setAnalysisRequest(String analysisRequest) {
		this.analysisRequest = analysisRequest;
	}

	public String getAnalysisResults() {
		return analysisResults;
	}

	public void setAnalysisResults(String analysisResults) {
		this.analysisResults = analysisResults;
	}

	public Long getThreshold() {
		return threshold;
	}

	public void setThreshold(Long threshold) {
		this.threshold = threshold;
	}

	public Date getExpirationTime() {
		return expirationTime;
	}

	public void setExpirationTime(Date expirationTime) {
		this.expirationTime = expirationTime;
	}

	public Date getLastReadTime() {
		return lastReadTime;
	}

	public void setLastReadTime(Date lastReadTime) {
		this.lastReadTime = lastReadTime;
	}

	public Long getCurrentProcessingTime() {
		return currentProcessingTime;
	}

	public void setCurrentProcessingTime(Long currentProcessingTime) {
		this.currentProcessingTime = currentProcessingTime;
	}
}
