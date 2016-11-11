/*
Copyright (c) 2012, Intel Corporation
All rights reserved.

Copyright (C) 2013 Politecnico di Torino, Italy
                   TORSEC group -- http://security.polito.it

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
* Neither the name of Intel Corporation nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

package com.intel.openAttestation.manifest.resource;

import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;

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
import com.intel.openAttestation.manifest.bean.OpenAttestationResponseFault;
import com.intel.openAttestation.manifest.hibernate.dao.AnalysisTypesDao;
import com.intel.openAttestation.manifest.hibernate.domain.AnalysisTypes;
import com.intel.openAttestation.manifest.hibernate.util.HibernateUtilHis;
import com.intel.openAttestation.manifest.bean.AnalysisTypesBean;

import java.io.File;

/**
* RESTful web service interface to work with OEM DB.
* @author xmei1
*
*/

@Path("resources/analysisTypes")
public class AnalysisTypesResource {
	static final int MAX_NAME_SIZE = 64;
	static final int MAX_MODULE_SIZE = 64;
	static final int MAX_URL_SIZE = 256;

	@POST
	@Consumes("application/json")
	@Produces("application/json")
	public Response addAnalysisRequest(@Context UriInfo uriInfo, AnalysisTypesBean analysisTypeBean,
		@Context javax.servlet.http.HttpServletRequest request) {
		
		UriBuilder b = uriInfo.getBaseUriBuilder();
		b = b.path(AnalysisTypesResource.class);
		Response.Status status = Response.Status.OK;

		try {
			AnalysisTypesDao dao = new AnalysisTypesDao();

			if (analysisTypeBean.getName() == null ||
			    analysisTypeBean.getModule() == null ||
			    analysisTypeBean.getVersion() == null ||
			    analysisTypeBean.getUrl() == null) {
			    throw new Exception("Missing parameter found.");
			}

			if (analysisTypeBean.getName().length() < 1 ||
			    analysisTypeBean.getModule().length() < 1 ||
			    analysisTypeBean.getUrl().length() < 1) {
			    throw new Exception("Too short parameter found");
			}

			if (analysisTypeBean.getName().length() > MAX_NAME_SIZE ||
			    analysisTypeBean.getModule().length() > MAX_MODULE_SIZE ||
			    analysisTypeBean.getUrl().length() > MAX_URL_SIZE) {
			    throw new Exception("Too long parameter found");
			}

			if (analysisTypeBean.getName().contains(" ")) {
				throw new Exception("Spaces not allowed in field \"name\"");
			}

			if (analysisTypeBean.getRequiredPcrMask() != null &&
			    !analysisTypeBean.getRequiredPcrMask().matches("[0-9A-Fa-f]{6}")) {
				throw new Exception("Wrong syntax for \"requiredPcrMask\", six hexadecimal numbers expected");
			}

			String analysisName = analysisTypeBean.getName();
			if (analysisName.equals("COMPARE_REPORT") || analysisName.equals("VALIDATE_PCR")) {
				throw new Exception("Analysis name '" + analysisName + "' not allowed; built-in analysis.");
			}

			String[] splittedURL = analysisTypeBean.getUrl().split(" ");
			if (!new File(splittedURL[0]).exists()) {
				throw new Exception("Specified script ('" + splittedURL[0] + "') doesn't exist.");
			}

			if (dao.getAnalysisTypeByName(analysisTypeBean.getName()) != null)
				throw new Exception("AnalysisType " + analysisTypeBean.getName() + " already exists in the database.");

			AnalysisTypes analysisType = new AnalysisTypes();
			analysisType.setName(analysisTypeBean.getName());
			analysisType.setModule(analysisTypeBean.getModule());
			analysisType.setVersion(analysisTypeBean.getVersion());
			analysisType.setURL(analysisTypeBean.getUrl());
			analysisType.setRequiredPcrMask((analysisTypeBean.getRequiredPcrMask() == null) ? "000000" : analysisTypeBean.getRequiredPcrMask());
			analysisType.setDeleted(false);

			dao.saveAnalysisType(analysisType);

			return Response.status(status).header("Location", b.build()).type(MediaType.TEXT_PLAIN).entity("True").build();
		} catch (Exception e) {
			status = Response.Status.INTERNAL_SERVER_ERROR;
			OpenAttestationResponseFault fault = new OpenAttestationResponseFault(OpenAttestationResponseFault.FaultCode.FAULT_500);
			fault.setError_message("Add AnalysisTypes entry failed. " + e.getMessage());
			return Response.status(status).header("Location", b.build()).entity(fault).build();
		}
	}

	@DELETE
	@Produces("application/json")
	public Response delAnalysisRequest(@QueryParam("name") String name,@Context UriInfo uriInfo) {
		UriBuilder b = uriInfo.getBaseUriBuilder();
		b = b.path(AnalysisTypesResource.class);
		Response.Status status = Response.Status.OK;
		boolean isValidKey = true;

		try {
			AnalysisTypesDao dao = new AnalysisTypesDao();
			
			if (name == null)
				throw new Exception("Missing parameter \"name\".");

			if (name.length() < 1)
				throw new Exception("Too short parameter \"name\".");

			if (name.length() > MAX_NAME_SIZE)
				throw new Exception("Too long parameter \"name\"");

			if (name.contains(" "))
				throw new Exception("Spaces not allowed in field \"name\"");

			if (name.equals("COMPARE_REPORT") || name.equals("VALIDATE_PCR"))
				throw new Exception("Analysis name '" + name + "' not allowed; built-in analysis.");

			AnalysisTypes analysisType = dao.getAnalysisTypeByName(name);
			if (analysisType == null)
				throw new Exception("AnalysisType " + name + " does not exist in the database.");

			dao.deleteAnalysisType(analysisType);
			return Response.status(status).type(MediaType.TEXT_PLAIN).entity("True").build();
		} catch (Exception e) {
			status = Response.Status.INTERNAL_SERVER_ERROR;
			OpenAttestationResponseFault fault = new OpenAttestationResponseFault(OpenAttestationResponseFault.FaultCode.FAULT_500);
			fault.setError_message("Edit AnalysisTypes entry failed. " + e.getMessage());
			return Response.status(status).header("Location", b.build()).entity(fault).build();
		}
	}

	@GET
	@Produces("application/json")
	public List<AnalysisTypes> getAnalysisTypeEntry() {
		AnalysisTypesDao dao = new AnalysisTypesDao();

		return dao.getAllAnalysisType();
	}
}
