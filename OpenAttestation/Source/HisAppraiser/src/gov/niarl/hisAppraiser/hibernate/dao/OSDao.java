/*
 * (copyright) 2012 United States Government, as represented by the 
 * Secretary of Defense.  All rights reserved.
 * 
 * Copyright (C) 2014 Politecnico di Torino, Italy
 *                    TORSEC group -- http://security.polito.it
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

package gov.niarl.hisAppraiser.hibernate.dao;

import gov.niarl.hisAppraiser.hibernate.domain.OS;
import gov.niarl.hisAppraiser.hibernate.util.HibernateUtilHis;

import java.util.List;

import org.hibernate.Query;

public class OSDao {
	public OSDao() {
	}

	/**
	 * Obtains the OS from the host name reading
	 * information stored on DB.
	 * @param hostName The host name to look for
	 * @return The OS associated with the host name received
	 */
	public String findHostOS(String hostName) {
		String os_name = null;
		try {
			HibernateUtilHis.beginTransaction();
			Query query = HibernateUtilHis.getSession().createQuery("select c from OS c where ID in " + 
				"(select a.os from MLE a where ID in (select b.mle from HOST_MLE b where HOST_ID in " + 
				"(select h.ID from HOST h where HOST_NAME = :host_name)))");
			query.setString("host_name", hostName);

			List list = query.list();

			if (list.size() > 0) {
				os_name = ((OS)list.get(0)).getName();
			}
			return os_name;
		} catch (Exception e) {
			HibernateUtilHis.rollbackTransaction();
			e.printStackTrace();
			throw new RuntimeException(e);
		}
	}
}
