/*
 * (copyright) 2012 United States Government, as represented by the 
 * Secretary of Defense.  All rights reserved.
 * 
 * Copyright (C) 2013 Politecnico di Torino, Italy
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
package com.intel.openAttestation.manifest.hibernate.dao;

import com.intel.openAttestation.manifest.hibernate.util.HibernateUtilHis;
import com.intel.openAttestation.manifest.hibernate.domain.AnalysisTypes;

import java.util.List;
import java.util.Iterator;

import org.hibernate.Query;
import org.hibernate.Session;


/**
 * This class serves as a central location for updates and queries against 
 * the measures_log table
 * @author Nicola Barresi
 * @version Crossbow
 *
 */
public class AnalysisTypesDao {

	public AnalysisTypesDao() {
	}

	/**
	 * Saves an AnalysisTypes
	 * @param analysisType AnalysisTypes entry to be saved
	 */
	public void saveAnalysisType(AnalysisTypes analysisType) {
		try {
			HibernateUtilHis.beginTransaction();
			HibernateUtilHis.getSession().save(analysisType);
			HibernateUtilHis.commitTransaction();
		} catch (Exception e) {
			HibernateUtilHis.rollbackTransaction();
			e.printStackTrace();
			throw new RuntimeException(e);
		} finally {
			HibernateUtilHis.closeSession();
		}
	}

	/**
	 * Retrieves an AnalysisTypes entry based on the primary key
	 * @param id The id or primary key of the needed AnalysisTypes entry
	 * @return The AnalysisTypes entry retrieved from the database
	 */
	public AnalysisTypes getAnalysisType(Long id) {
		AnalysisTypes result = null;
		try {
			HibernateUtilHis.beginTransaction();
			Query query = HibernateUtilHis.getSession().createQuery("from AnalysisTypes a where a.id = :id");
			query.setLong("id", id);
			List list = query.list();
			if (list.size() >= 1) {
				result = (AnalysisTypes) list.iterator().next();
			}
			HibernateUtilHis.commitTransaction();
			return result;
		} catch (Exception e) {
			HibernateUtilHis.rollbackTransaction();
			e.printStackTrace();
			throw new RuntimeException(e);
		} finally {
			HibernateUtilHis.closeSession();
		}
	}

	/**
	 * Retrieves a not deleted AnalysisTypes entry based on its name
	 * @param name The name of the needed AnalysisTypes entry
	 * @return The AnalysisTypes entry retrieved from the database
	 */
	public AnalysisTypes getAnalysisTypeByName(String name) {
		AnalysisTypes result = null;
		try {
			HibernateUtilHis.beginTransaction();
			Query query = HibernateUtilHis.getSession().createQuery("from AnalysisTypes a where a.name = :name and a.deleted=0");
			query.setString("name", name);
			List list = query.list();
			if (list.size() >= 1) {
				result = (AnalysisTypes) list.iterator().next();
			}
			HibernateUtilHis.commitTransaction();
			return result;
		} catch (Exception e) {
			HibernateUtilHis.rollbackTransaction();
			e.printStackTrace();
			throw new RuntimeException(e);
		} finally {
			HibernateUtilHis.closeSession();
		}
	}

	/**
	 * Retrieves all the AnalysisTypes entries from the database
	 * @return The list of AnalysisTypes entries retrieved from
	 * the database
	 */	
	public List<AnalysisTypes> getAllAnalysisType() {
		List<AnalysisTypes> result = null;
		try {
			HibernateUtilHis.beginTransaction();
			Query query = HibernateUtilHis.getSession().createQuery("from AnalysisTypes a");
			List list = query.list();
			if (list.size() >= 1) {
				result = (List<AnalysisTypes>) list;
			}
			HibernateUtilHis.commitTransaction();
			return result;
		} catch (Exception e) {
			HibernateUtilHis.rollbackTransaction();
			e.printStackTrace();
			throw new RuntimeException(e);
		} finally {
			HibernateUtilHis.closeSession();
		}
	}

	/**
	 * Deletes the AnalysisTypes entry received
	 * @param analysisType The AnalysisTypes to be deleted
	 */
	public void deleteAnalysisType (AnalysisTypes analysisType) {
		try {
			HibernateUtilHis.beginTransaction();
			Query query = HibernateUtilHis.getSession().createQuery("from AnalysisTypes a where a.id = :id");
			
			query.setLong("id", analysisType.getId());
			List list = query.list();
			if (list.size() < 1) {
				HibernateUtilHis.rollbackTransaction();
				throw new Exception("Object not found");
			}
			AnalysisTypes AnalysisTypesEntry = (AnalysisTypes)list.get(0);
			AnalysisTypesEntry.setDeleted(true);
			HibernateUtilHis.commitTransaction();
		} catch (Exception e) {
			HibernateUtilHis.rollbackTransaction();
			e.printStackTrace();
			throw new RuntimeException(e);
		} finally {
			HibernateUtilHis.closeSession();
		}
	}

}
