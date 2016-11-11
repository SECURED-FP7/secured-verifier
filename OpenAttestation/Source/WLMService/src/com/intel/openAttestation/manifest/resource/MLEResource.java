/*
Copyright (c) 2012, Intel Corporation
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
    * Neither the name of Intel Corporation nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

package com.intel.openAttestation.manifest.resource;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import javax.ws.rs.Consumes;
import javax.ws.rs.DELETE;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.UriBuilder;
import javax.ws.rs.core.UriInfo;

import gov.niarl.hisAppraiser.util.HisUtil;

import com.intel.openAttestation.manifest.bean.MLEBean;
import com.intel.openAttestation.manifest.bean.MLE_Manifest;
import com.intel.openAttestation.manifest.bean.OpenAttestationResponseFault;
import com.intel.openAttestation.manifest.hibernate.dao.MLEDAO;
import com.intel.openAttestation.manifest.hibernate.dao.OEMDAO;
import com.intel.openAttestation.manifest.hibernate.dao.OSDAO;
import com.intel.openAttestation.manifest.hibernate.dao.PcrWhiteListDAO;
import com.intel.openAttestation.manifest.hibernate.domain.MLE;
import com.intel.openAttestation.manifest.hibernate.domain.OEM;
import com.intel.openAttestation.manifest.hibernate.domain.OS;
import com.intel.openAttestation.manifest.hibernate.domain.PcrWhiteList;
import com.intel.openAttestation.manifest.hibernate.util.HibernateUtilHis;
import com.intel.openAttestation.manifest.resource.MLEResource;


/**
 * RESTful web service interface to work with MLE DB.
 * @author 
 *
 */

@Path("resources/mles")
public class MLEResource {
	@POST
	@Consumes("application/json")
	@Produces("application/json")
	public Response addMLE(@Context UriInfo uriInfo, MLEBean mleBean,@Context javax.servlet.http.HttpServletRequest request){
        UriBuilder b = uriInfo.getBaseUriBuilder();
        b = b.path(MLEResource.class);
		Response.Status status = Response.Status.OK;
		boolean isValidKey = true;
		try{
		    MLEDAO dao = new MLEDAO();
		    PcrWhiteListDAO pcrDao = new PcrWhiteListDAO();
		    OSDAO osDao = new OSDAO();
		    OEMDAO oemDao = new OEMDAO();
		    MLE mle = new MLE();
		    OS os = new OS();
		    OEM oem = new OEM();
			HashMap parameters = new HashMap();
			
			if (mleBean.getName() != null && mleBean.getVersion() != null && mleBean.getAttestation_Type() != null &&  mleBean.getAttestation_Type().equals("PCR")){
				parameters.put(mleBean.getName(), 50);
				parameters.put(mleBean.getVersion(), 100);
				parameters.put(mleBean.getAttestation_Type(), 50);			
			} else {
				isValidKey = false;
			}

			if (mleBean.getOsName() != null){
				parameters.put(mleBean.getOsName(), 50);
			}
			
			if (mleBean.getOsVersion() != null){
				parameters.put(mleBean.getOsVersion(), 50);
			}
			
			if (mleBean.getOemName() != null){
				parameters.put(mleBean.getOemName(), 50);
			}
			
			if (mleBean.getMLE_Type() != null){
				parameters.put(mleBean.getMLE_Type(), 50);
			}

			if (mleBean.getDescription() != null){
				parameters.put(mleBean.getDescription(), 100);
			}
			
			if (mleBean.getMLE_Manifests() != null){
				List<MLE_Manifest> pcrList = mleBean.getMLE_Manifests();
				for (MLE_Manifest list : pcrList){
					if(list.getValue() == null  || list.getValue().length() == 0 || list.getName() == null 
					   ||  list.getName().length() == 0)
					{
						status = Response.Status.INTERNAL_SERVER_ERROR;
						OpenAttestationResponseFault fault = new OpenAttestationResponseFault(
								OpenAttestationResponseFault.FaultCode.FAULT_500);
						fault.setError_message("Invalid put for PCR value");
						return Response.status(status).header("Location", b.build()).entity(fault).build();		
					}
					parameters.put(list.getValue(), 100);
				}
			}
			
			parameters.put(mleBean.getDescription(), 100);
			if (!isValidKey || mleBean.getName().length() < 1 || mleBean.getVersion().length() < 1 || !HisUtil.validParas(parameters)){
				status = Response.Status.INTERNAL_SERVER_ERROR;
				OpenAttestationResponseFault fault = new OpenAttestationResponseFault(
						OpenAttestationResponseFault.FaultCode.FAULT_500);
				if (mleBean.getAttestation_Type() == null || !mleBean.getAttestation_Type().equals("PCR")){
					fault.setError_message("Invalid put for Attestation type");
				} else {
					fault.setError_message("Add MLE entry failed, please check the length for each parameters" +
							" and remove all of the unwanted characters belonged to [# & + : " + "\" \']");
				}
				return Response.status(status).header("Location", b.build()).entity(fault).build();
			}
			
		    if (mleBean.getMLE_Type().equals("VMM")){
		    	System.out.println("The OS Name exists:" + mleBean.getOsName());
		    	if ( (os = osDao.getOS(mleBean.getOsName(), mleBean.getOsVersion()))!= null){
		    		mle.setOs(os);
		    	}
		    	else{
					status = Response.Status.BAD_REQUEST;
					OpenAttestationResponseFault fault = new OpenAttestationResponseFault(1006);
					fault.setError_message("Data Error - OS[" + mleBean.getOsName() + 
							"] Version[" + mleBean.getOsVersion() +"] does not exist");
					return Response.status(status).header("Location", b.build()).entity(fault)
								.build();
		    	}
		    }
		    else if(mleBean.getMLE_Type().equals("BIOS")){
		    	if((oem = oemDao.getOEM(mleBean.getOemName())) != null){
		    		mle.setOem(oem);
		    	}
		    	else{
					status = Response.Status.BAD_REQUEST;
					OpenAttestationResponseFault fault = new OpenAttestationResponseFault(1006);
					fault.setError_message("Data Error - OEM[" + mleBean.getOemName() + "] does not exist");
					return Response.status(status).header("Location", b.build()).entity(fault)
								.build();
					
			    }
		    }
		    else{
		    	status = Response.Status.BAD_REQUEST;
				OpenAttestationResponseFault fault = new OpenAttestationResponseFault(1006);
				fault.setError_message("Data Error - MLE_Type is error:" + mleBean.getMLE_Type());
				return Response.status(status).header("Location", b.build()).entity(fault)
							.build();
		    }
		    if(dao.isMLEExisted(mleBean.getName(), mleBean.getVersion())){
		    	status = Response.Status.BAD_REQUEST;
				OpenAttestationResponseFault fault = new OpenAttestationResponseFault(1006);
				fault.setError_message("Data Error - MLE Name " + mleBean.getName()+ " Version "+mleBean.getVersion() + " already exists in the database");
				return Response.status(status).header("Location", b.build()).entity(fault).build();
		    }
		    
		    mle.setName(mleBean.getName());
		    mle.setVersion(mleBean.getVersion());
		    mle.setAttestation_Type(mleBean.getAttestation_Type());
		    mle.setDescription(mleBean.getDescription());
		    mle.setMLE_Type(mleBean.getMLE_Type());
			dao.addMLEEntry(mle);
			if (mleBean.getMLE_Manifests()!=null){
				for(MLE_Manifest mle_manifest:mleBean.getMLE_Manifests()){
					PcrWhiteList pcr = new PcrWhiteList();
					pcr.setPcrName(mle_manifest.getName());
					pcr.setPcrDigest(mle_manifest.getValue());
					pcr.setMle(mle);
					pcrDao.addPcrEntry(pcr);
				}			
			}
	        return Response.status(status).header("Location", b.build()).type(MediaType.TEXT_PLAIN).entity("True").build();
		}catch (Exception e){
			status = Response.Status.INTERNAL_SERVER_ERROR;
			OpenAttestationResponseFault fault = new OpenAttestationResponseFault(
					OpenAttestationResponseFault.FaultCode.FAULT_500);
			fault.setError_message("Add MLE entry failed." + "Exception:" + e.getMessage());
			return Response.status(status).header("Location", b.build()).entity(fault).build();
		}

	}
	
	@PUT
    @Consumes("application/json")
    @Produces("application/json")
	public Response updateMLE(@Context UriInfo uriInfo, MLEBean mleBean,
			@Context javax.servlet.http.HttpServletRequest request){
        UriBuilder b = uriInfo.getBaseUriBuilder();
        b = b.path(MLEResource.class);
		Response.Status status = Response.Status.OK;
		boolean isValidKey = true;
		try{
			MLEDAO mleDao = new MLEDAO();
			OSDAO osDao = new  OSDAO();
			OEMDAO oemDao = new OEMDAO();
			List<PcrWhiteList> pcrList = new ArrayList<PcrWhiteList>(); 
			PcrWhiteListDAO pcrDao = new PcrWhiteListDAO();
			HashMap parameters = new HashMap();
			if (mleBean.getName() != null) {
				parameters.put(mleBean.getName(), 50);
			} else {
				isValidKey = false;
			}
			
			if (mleBean.getVersion() != null){
				parameters.put(mleBean.getVersion(), 100);
			} else {
				isValidKey = false;
			}

			if (mleBean.getMLE_Type() != null){
				parameters.put(mleBean.getMLE_Type(), 50);
			}

			if (mleBean.getDescription() != null){
				parameters.put(mleBean.getDescription(), 100);
			}

			if (!isValidKey || mleBean.getVersion().length() < 1 ||  mleBean.getName().length() < 1 || !HisUtil.validParas(parameters)){
				status = Response.Status.INTERNAL_SERVER_ERROR;
				OpenAttestationResponseFault fault = new OpenAttestationResponseFault(
						OpenAttestationResponseFault.FaultCode.FAULT_500);
				fault.setError_message("Update MLE entry failed, please check the length for each parameters" +
						" and remove all of the unwanted characters belonged to [# & + : \" \']");
				return Response.status(status).header("Location", b.build()).entity(fault)
						.build();
			}
			
			if (mleBean.getMLE_Type().equals("BIOS") || mleBean.getMLE_Type().equals("VMM")){
				if (!mleDao.isMLEExisted(mleBean.getName(),mleBean.getVersion(),mleBean.getOsName(),mleBean.getOsVersion(),mleBean.getOemName())){
	        		status = Response.Status.BAD_REQUEST;
					OpenAttestationResponseFault fault = new OpenAttestationResponseFault(1007);
					fault.setError_message("WLM Service Error - MLE not found in attestation data to update");
					return Response.status(status).header("Location", b.build()).entity(fault)
								.build();
	        	}
				MLE mle = mleDao.getMLE(mleBean.getName(),mleBean.getVersion());
				if(mleBean.getDescription()!=null)    //update description
					mleDao.editMLEDesc(mleBean.getName(),mleBean.getVersion(), mleBean.getDescription());
				if (mleBean.getMLE_Manifests()!=null){  //update whitelist
					for (MLE_Manifest mleManifest: mleBean.getMLE_Manifests()){					
						parameters.clear();
						if (mleManifest.getName() != null && !mleManifest.getName().trim().equals("")){
							parameters.put(mleManifest.getName(), 10);
						} else {
							isValidKey = false;
						}
						
						if (mleManifest.getValue() != null && !mleManifest.getValue().trim().equals("")){
							parameters.put(mleManifest.getValue(), 100);	
						} else {
							isValidKey = false;
						}
						
						if (!HisUtil.validParas(parameters) || !isValidKey){
							status = Response.Status.INTERNAL_SERVER_ERROR;
							OpenAttestationResponseFault fault = new OpenAttestationResponseFault(
									OpenAttestationResponseFault.FaultCode.FAULT_500);
							fault.setError_message("Update MLE entry failed, please check the length for each parameters" +
									" and remove all of the unwanted characters belonged to [# & + : \" \']");
							return Response.status(status).header("Location", b.build()).entity(fault).build();
						}
						
						pcrDao.deletePcrByMleID(mle.getMLEID());
						PcrWhiteList pcr = new PcrWhiteList();
						pcr.setMle(mle);
						pcr.setPcrName(mleManifest.getName());
						pcr.setPcrDigest(mleManifest.getValue());
						pcrList.add(pcr);
					}
					pcrDao.addPcrList(pcrList);
				}
			} else {
				status = Response.Status.INTERNAL_SERVER_ERROR;
				OpenAttestationResponseFault fault = new OpenAttestationResponseFault(OpenAttestationResponseFault.FaultCode.FAULT_500);
				fault.setError_message("Update MLE entry failed, pleae check the type of MLE");
				return Response.status(status).header("Location", b.build()).entity(fault).build();
			}

			return Response.status(status).header("Location", b.build()).type(MediaType.TEXT_PLAIN).entity("True")
	        		.build();
		}catch (Exception e){
			status = Response.Status.INTERNAL_SERVER_ERROR;
			OpenAttestationResponseFault fault = new OpenAttestationResponseFault(
					OpenAttestationResponseFault.FaultCode.FAULT_500);
			fault.setError_message("Update MLE entry failed." + "Exception:" + e.getMessage());
			return Response.status(status).header("Location", b.build()).entity(fault)
					.build();
	}
  }
		
	@DELETE
	@Produces("application/json")
	public Response delMLEEntry(@QueryParam("mleName") String name, @QueryParam("mleVersion") String version, @QueryParam("osName") String osName, 
			@QueryParam("osVersion") String osVersion,@QueryParam("oemName") String oemName,@Context UriInfo uriInfo){
        UriBuilder b = uriInfo.getBaseUriBuilder();
        b = b.path(MLEResource.class);
		Response.Status status = Response.Status.OK;
		MLEDAO mleDao = new MLEDAO();
		PcrWhiteListDAO pcrDao = new PcrWhiteListDAO();
		boolean isValidKey = true;
		
        try{	
			HashMap parameters = new HashMap();
			if (name != null && version != null){
				parameters.put(name, 50);
				parameters.put(version, 100);
			} else {
				isValidKey = false;
			}

			if (!isValidKey || name.length() < 1 || version.length() < 1 || !HisUtil.validParas(parameters)){
				status = Response.Status.INTERNAL_SERVER_ERROR;
				OpenAttestationResponseFault fault = new OpenAttestationResponseFault(
						OpenAttestationResponseFault.FaultCode.FAULT_500);
				fault.setError_message("Delete MLE entry failed, please check the length for each parameters" +
						" and remove all of the unwanted characters belonged to [# & + : \" \']");
				return Response.status(status).header("Location", b.build()).entity(fault).build();
			}
			
        	if (!mleDao.isMLEExisted(name,version,osName, osVersion,oemName)){
        		status = Response.Status.BAD_REQUEST;
				OpenAttestationResponseFault fault = new OpenAttestationResponseFault(1007);
				fault.setError_message("WLM Service Error - MLE not found in attestation data to delete");
				return Response.status(status).header("Location", b.build()).entity(fault).build();
        	}
        	
        	MLE mle= mleDao.DeleteMLEEntry(name, version);
            System.out.println("##Check mle id:" + mle.getMLEID());
            pcrDao.deletePcrByMleID(mle.getMLEID());
        	return Response.status(status).header("Location", b.build()).type(MediaType.TEXT_PLAIN).entity("True").build();
		}catch (Exception e){
			status = Response.Status.INTERNAL_SERVER_ERROR;
			OpenAttestationResponseFault fault = new OpenAttestationResponseFault(OpenAttestationResponseFault.FaultCode.FAULT_500);
			fault.setError_message("Delete MLE entry failed." + "Exception:" + e.getMessage() + "    Possible solution: The specified MLE has a reference with HOST, solve this and try again."); 
			return Response.status(status).entity(fault).build();

		}
	}

	@GET
	@Produces("application/json")
	public List<MLEBean> searchMLE(@QueryParam("searchCriteria") String criteria){
		MLEDAO mleDao = new MLEDAO();
		List<MLE> mleList = new ArrayList<MLE>(); 
		List<MLEBean> mleBeanList = new ArrayList<MLEBean>();
		MLEBean mleBean = new MLEBean();
		ArrayList<PcrWhiteList> pcrList = new ArrayList<PcrWhiteList>();
		PcrWhiteListDAO pcrDao = new PcrWhiteListDAO();
		MLE mle = null;
		pcrList = new ArrayList<PcrWhiteList>();
		try {
			HibernateUtilHis.getSession();
			mleList = mleDao.getAllMLEEntries();
			for (int i=0; i<mleList.size(); i++){
				mleBean = new MLEBean();
				mle = mleDao.queryMLEByCriteria(criteria, mleList.get(i), mleList.get(i).getMLEID());
				if (criteria == null || criteria.trim().equalsIgnoreCase("") || mle != null){
			       	mleBean.setName(mle.getName());
			    	mleBean.setVersion(mle.getVersion());
				   	mleBean.setDescription(mle.getDescription());
				    mleBean.setAttestation_Type(mle.getAttestation_Type());
					if (mle.getOem() != null){
						mleBean.setOemName(mle.getOem().getName());
					   	mleBean.setOsName("null");
					   	mleBean.setOsVersion("null");		
					} else if (mle.getOs() != null){
					   	mleBean.setOsName(mle.getOs().getName());
					   	mleBean.setOsVersion(mle.getOs().getVersion());
					   	mleBean.setOemName("null");
					}
		       		//Get pcr white list;
					List<PcrWhiteList> tempList = pcrDao.queryPcrByMLEid(mleList.get(i).getMLEID().longValue());
					if (tempList != null){
						pcrList = new ArrayList<PcrWhiteList>(tempList);
					}
					else{
						pcrList = new ArrayList<PcrWhiteList>();
					}
			    	List<MLE_Manifest> mleManifest = new ArrayList<MLE_Manifest>();
			    	for (int j=0; j<pcrList.size(); j++){
			    		MLE_Manifest entry = new MLE_Manifest();
			    		entry.setName(pcrList.get(j).getPcrName());
			    		entry.setValue(pcrList.get(j).getPcrDigest());
			    		mleManifest.add(entry);
			    	}
			    	mleBean.setMLE_Manifests(mleManifest);
					mleBean.setMLE_Type(mle.getMLE_Type());
			    	mleBeanList.add(mleBean);
				}		
			}
		}catch (Exception e){
			System.out.println("Encountered an exception with detail message: " + e.getMessage());
		}finally {
			HibernateUtilHis.closeSession();
		}
		return mleBeanList;
	}
	
	@GET
	@Path("/manifest")
	@Produces("application/json")
	public MLEBean getMLEEntry(@QueryParam("mleName") String name, @QueryParam("mleVersion") String version, @QueryParam("osName") String osName, 
			@QueryParam("osVersion") String osVersion, @QueryParam("oemName") String oemName, @Context UriInfo uriInfo){	
		ArrayList<PcrWhiteList> pcrList = new ArrayList();
		MLEDAO mleDao = new MLEDAO();
		PcrWhiteListDAO pcrDao = new PcrWhiteListDAO();
		MLE mle = null;
		OEM oem = null;
		OS os = null;
		MLEBean mleBean = new MLEBean();
		pcrList = new ArrayList();
        try{
			HibernateUtilHis.getSession();
			if (oemName != null){
				mle = mleDao.queryMLEidByNameAndVersionAndOEMid(name, version, oemName);
				//query oem
				oem = mleDao.queryOEMByNameAndVersionAndOEMid(name, version, oemName);
				//oem = mle.getOem();
				
			} else if (osName != null && osVersion != null){
				mle = mleDao.queryMLEidByNameAndVersionAndOSid(name, version, osName, osVersion);
				//query os
				os = mleDao.queryOSByNameAndVersionAndOSid(name, version, osName, osVersion);
				//os = mle.getOs();
			} else {
				System.out.println("please check the input parameters and provide complete information");
				return mleBean;
			}
			
			if (mle != null){
				mleBean.setName(mle.getName());
				mleBean.setVersion(mle.getVersion());
				mleBean.setDescription(mle.getDescription());
				mleBean.setAttestation_Type(mle.getAttestation_Type());
				if (os != null){
					mleBean.setOsName(os.getName());
					mleBean.setOsVersion(os.getVersion());
				} else {
					mleBean.setOsName("null");
					mleBean.setOsVersion("null");
				}
				
				if (oem != null){
					mleBean.setOemName(oem.getName());
				} else {
					mleBean.setOemName("null");
				}
				
				//Get pcr white list;
				List tempList = pcrDao.queryPcrByMLEid(mle.getMLEID().longValue());
				if (tempList != null){
					pcrList = new ArrayList(tempList);
				}
				
				List<MLE_Manifest> mleManifest = new ArrayList();
				for (int i=0; i<pcrList.size(); i++){
					MLE_Manifest entry = new MLE_Manifest();
					entry.setName(pcrList.get(i).getPcrName());
					entry.setValue(pcrList.get(i).getPcrDigest());
					mleManifest.add(entry);
				}
				
				if (mleManifest.size() >0 ){
					mleBean.setMLE_Manifests(mleManifest);
				} else{
					mleBean.setMLE_Manifests(null);
				}

				mleBean.setMLE_Type(mle.getMLE_Type());
			}
		}catch (Exception e){
			System.out.println("Encountered an exception with detail message: " + e.getMessage());
		}finally{
			HibernateUtilHis.closeSession();
		}
        return mleBean;
	}
	
}
