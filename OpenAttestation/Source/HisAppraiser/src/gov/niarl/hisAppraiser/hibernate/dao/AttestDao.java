/*
Copyright (c) 2012, Intel Corporation
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
    * Neither the name of Intel Corporation nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

package gov.niarl.hisAppraiser.hibernate.dao;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Iterator;

import org.hibernate.Query;
import org.hibernate.Session;




import gov.niarl.hisAppraiser.Constants;
import gov.niarl.hisAppraiser.hibernate.domain.AttestRequest;
import gov.niarl.hisAppraiser.hibernate.domain.MLE;
//import gov.niarl.hisAppraiser.hibernate.domain.
import gov.niarl.hisAppraiser.hibernate.domain.HOST_MLE;
import gov.niarl.hisAppraiser.hibernate.domain.PcrWhiteList;
import gov.niarl.hisAppraiser.hibernate.util.AttestUtil;
import gov.niarl.hisAppraiser.hibernate.util.HibernateUtilHis;
import gov.niarl.hisAppraiser.hibernate.util.ResultConverter;
import gov.niarl.hisAppraiser.hibernate.domain.HOST;

public class AttestDao {
	
	public AttestDao(){
		HibernateUtilHis.beginTransaction();
	}

	/*
	 * update the request row for a given request
	 * @Param req of the request of interest.
	 * 
	 */
	public AttestRequest updateRequest(AttestRequest req){
		try {
			Session session = HibernateUtilHis.getSession();
			session.update(req);
			session.flush();
			return  (AttestRequest)session.get(AttestRequest.class, req.getId());
		} catch (Exception e) {
			HibernateUtilHis.rollbackTransaction();
			throw new RuntimeException(e);
		}
	}

	
	/*
	 * obtain the first attestRequest row for a given host name.
	 * @Param hostName Name of the machine of interest.
	 * @Return The AttestRequest entry
	 */
	public AttestRequest getLatestPolledRequest(String hostName){
		hostName = hostName.toLowerCase();
		Query query = HibernateUtilHis.getSession().createQuery("from AttestRequest a where a.hostName = :hostName and" +
				                " a.isConsumedByPollingWS = :isConsumedByPollingWS and a.auditLog is null and a.result is null order by a.requestTime asc");
		query.setString("hostName", hostName);
		query.setBoolean("isConsumedByPollingWS", true);
		List list = query.list();
		if (list.size() < 1) {
			return new AttestRequest();
		} else {
			return (AttestRequest) list.iterator().next();
		}
	}

	/**
	 * Disables requests where:
	 *  - lastReadTime is older than configured maxIdleTime
	 *  - expirationTime is up
	 *  - result is UN_TRUSTED 
	 * @param hostName Name of the machine of interest.
	 */
	public void disableUnusedRequests(String hostName) {
		AttestUtil.loadProp();

		String queryString = "from AttestRequest a where a.hostName = :hostName " + 
		    "and a.threshold is not null and a.threshold >= 0 and a.expirationTime is not null";
		Query query = HibernateUtilHis.getSession().createQuery(queryString);
		query.setString("hostName", hostName.toLowerCase());

		List list = query.list();
		AttestRequest tmpRequest = null;
		Iterator iter = list.iterator();
		while (iter.hasNext()) {
			tmpRequest = (AttestRequest) iter.next();

			Long currentTime = new Date().getTime();
			Long maxIdleTime = AttestUtil.getMaxIdleTime() * 1000 * 60 * 60 * 24;
			boolean IDLE_EXPIRED = currentTime - tmpRequest.getLastReadTime().getTime() > maxIdleTime;
			boolean TIME_EXPIRED = currentTime > tmpRequest.getExpirationTime().getTime();
			boolean UN_TRUSTED = tmpRequest.getResult() != null &&
			    tmpRequest.getResult() == ResultConverter.getIntFromResult(ResultConverter.AttestResult.UN_TRUSTED);

			if (IDLE_EXPIRED || TIME_EXPIRED || UN_TRUSTED) {
				queryString = "from AttestRequest a where a.requestId = :requestId";
				query = HibernateUtilHis.getSession().createQuery(queryString);
				query.setString("requestId", tmpRequest.getRequestId());

				for (AttestRequest request : (List<AttestRequest>)query.list()) {
					if (IDLE_EXPIRED)
						request.setThreshold(Constants.PERIODIC_IDLE_EXPIRED);
					else if (TIME_EXPIRED)
						request.setThreshold(Constants.PERIODIC_TIME_EXPIRED);
					else if (UN_TRUSTED)
						request.setThreshold(Constants.PERIODIC_HOST_UNTRUSTED);
					updateRequest(request);
				}
			}
		}
	}

	/**
	 * Obtains a list of attestRequests to be served.
	 * @param hostName Name of the machine of interest.
	 * @param isConsumed The desired value for field isConsumedByPollingWS
	 * @return A list of AttestRequest entries to be served
	 */
	public List<AttestRequest> getPendingRequests(String hostName, boolean isConsumed) {
		List<AttestRequest> requestList = new ArrayList<AttestRequest>();
		AttestUtil.loadProp();

		String queryString = "from AttestRequest a where a.hostName = :hostName and " +
		                     "((a.isConsumedByPollingWS = :isConsumedByPollingWS and a.auditLog is null and a.result is null) " +
		                     "or (a.threshold is not null and a.threshold >= 0)) order by a.validateTime asc";
		Query query = HibernateUtilHis.getSession().createQuery(queryString);
		query.setString("hostName", hostName.toLowerCase());
		query.setBoolean("isConsumedByPollingWS", isConsumed);

		List list = query.list();
		AttestRequest tmpRequest = null;
		Iterator iter = list.iterator();
		while (iter.hasNext()) {
			tmpRequest = (AttestRequest) iter.next();

			if (tmpRequest.getThreshold() == null || tmpRequest.getValidateTime() == null ||
			    tmpRequest.getCurrentProcessingTime() == null) {
				requestList.add(tmpRequest);
				continue;
			}

			Long currentTime = new Date().getTime();
			Long lastValidateTime = tmpRequest.getValidateTime().getTime();

			/*
			 * If requestTime is greater than validateTime the
			 * request is currently being processed by the
			 * Appraiser. Then if isConsumed is true, the request
			 * can be directly added to the requestList; otherwise
			 * it has to be skipped
			 */
			if (lastValidateTime < tmpRequest.getRequestTime().getTime()) {
				if (isConsumed)
					requestList.add(tmpRequest);
				continue;
			}

			if ((currentTime - lastValidateTime) > AttestUtil.getMinAttestInterval() &&
			    (currentTime - lastValidateTime) > tmpRequest.getThreshold() - tmpRequest.getCurrentProcessingTime() * AttestUtil.getAnticipationFactor()) {
				requestList.add(tmpRequest);
			}
		}

		if (requestList.size() == 0)
			requestList.add(new AttestRequest());

		return requestList;
	}
	
	/**
	 * get the earliest request attest for given host  
	 * @param hostName
	 * @return
	 */
	public AttestRequest getFirstRequest(String hostName){
		hostName = hostName.toLowerCase();
		Query query = HibernateUtilHis.getSession().createQuery("from AttestRequest a where a.hostName = :hostName " +
				"and a.isConsumedByPollingWS = :isConsumedByPollingWS and a.auditLog is null and a.result is null order by a.requestTime asc");
		query.setString("hostName", hostName);
		query.setBoolean("isConsumedByPollingWS", false);
		List list = query.list();
		if (list.size() < 1) {
			return new AttestRequest();
		} else {
			return (AttestRequest) list.iterator().next();
		}
	}
	
	/**
	 * get pcr_name, pcr_digest from table prc_white_list, mle, host
	 * @param hostName
	 * @return
	 */
	public List<PcrWhiteList> getPcrValue(String hostName){
		hostName = hostName.toLowerCase();
		List<PcrWhiteList> pcrs = new ArrayList<PcrWhiteList>();
		Long mleId =0L;
		
		
		
		
//		Query query = HibernateUtilHis.getSession().createQuery("select a from MLE a inner join a.host b where b.HostName = :hostName");
//		query.setString("hostName", hostName);
//		List list = query.list();
//		List prcList;
		
		Query query = HibernateUtilHis.getSession().createQuery("select a from HOST_MLE a inner join a.host b where b.HostName = :hostName");
		query.setString("hostName", hostName);
		List list = query.list();
		List prcList;
		
		if (list.size()>0) {
			Iterator iterator  = list.iterator();  
			while (iterator.hasNext()){
				mleId = ((HOST_MLE)iterator.next()).getMle().getMLEID();
				query = HibernateUtilHis.getSession().createQuery("select a from PcrWhiteList a inner join a.mle b where b.MLEID = :mleId");
				query.setLong("mleId", mleId);
				prcList = query.list();
				pcrs.addAll((List<PcrWhiteList>)prcList);
			}
		}
		
		return pcrs;
	}
	
	/**
	 * Obtains the pcrIMLMask from the host name reading
	 * information stored on DB.
	 * @param hostName The host name to look for
	 * @return The validationMask associated with the host name received
	 */
	public String getPcrIMLMask(String hostName) {
		String pcrLogMask = null;
		try {
			HibernateUtilHis.beginTransaction();
			Query query = HibernateUtilHis.getSession().createQuery("select h from HOST h where h.HostName = :hostName");
			query.setString("hostName", hostName);
			
			List list = query.list();

			if (list.size() > 0) {
				pcrLogMask = ((HOST)list.get(0)).getPcrIMLMask();
			}
			return pcrLogMask;
		} catch (Exception e) {
			HibernateUtilHis.rollbackTransaction();
			e.printStackTrace();
			throw new RuntimeException(e);
		}
	}
}
