/*
 * PackagesVersionType.java
 *
 * Copyright (C) 2013 Politecnico di Torino, Italy
 *                    TORSEC group -- http://security.polito.it
 *
 * Author: Roberto Sassu <roberto.sassu@polito.it>
 *
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package torsec.ra.cassandra.db;

import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;
import java.util.Arrays;
import java.nio.ByteBuffer;
import java.sql.Types;
import org.apache.cassandra.utils.ByteBufferUtil;
import org.apache.cassandra.db.marshal.AbstractType;
import org.apache.cassandra.db.marshal.MarshalException;
import java.nio.charset.CharacterCodingException;

import org.apache.cassandra.utils.Hex;

public class PackagesVersionType extends AbstractType<ByteBuffer> {
	private native int filevercmp(String o1, String o2);
	public static final PackagesVersionType instance = new PackagesVersionType();

	PackagesVersionType() {}

	public ByteBuffer compose(ByteBuffer bytes)
	{
	    return bytes.duplicate();
	}

	public ByteBuffer decompose(ByteBuffer value)
	{
	    return value;
	}

	public int compare(ByteBuffer o1, ByteBuffer o2) {
		try {
			return filevercmp(ByteBufferUtil.string(o1), ByteBufferUtil.string(o2));
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}

	public String getString(ByteBuffer bytes) {
		try {
			return ByteBufferUtil.string(bytes);
		} catch (CharacterCodingException e) {
			throw new MarshalException("invalid UTF8 bytes " + ByteBufferUtil.bytesToHex(bytes));
		}
	}

	public String toString(ByteBuffer byteBuffer)
	{
	    return getString(byteBuffer);
	}

	public void validate(ByteBuffer bytes) {
	        // all bytes are legal.
	}

	public Class<ByteBuffer> getType()
	{
	    return ByteBuffer.class;
	}

	public boolean isSigned()
	{
	    return false;
	}

	public boolean isCaseSensitive()
	{
	    return false;
	}

	public boolean isCurrency()
	{
	    return false;
	}

	public int getPrecision(ByteBuffer obj)
	{
	    return -1;
	}

	public int getScale(ByteBuffer obj)
	{
	    return -1;
	}

	public int getJdbcType()
	{
	    return Types.BINARY;
	}

	public boolean needsQuotes()
	{
	    return true;
	}

	public ByteBuffer fromString(String source)
        {
		try
		{
		    return ByteBuffer.wrap(Hex.hexToBytes(source));
		}
		catch (NumberFormatException e)
		{
		    throw new MarshalException(String.format("cannot parse '%s' as hex bytes", source), e);
		}
       }

	static {
		System.loadLibrary("filevercmp");
	}

}
