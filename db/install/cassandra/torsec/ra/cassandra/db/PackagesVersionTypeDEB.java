/*
 * PackagesVersionTypeDEB.java
 *
 * Copyright (C) 2013 Politecnico di Torino, Italy
 *                    TORSEC group -- http://security.polito.it
 *
 * Author: Giuseppe Baglio <giuseppebag@gmail.com>
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
import java.io.BufferedWriter;
import java.io.FileWriter;

import org.apache.cassandra.utils.ByteBufferUtil;
import org.apache.cassandra.db.marshal.AbstractType;
import org.apache.cassandra.db.marshal.MarshalException;
import java.nio.charset.CharacterCodingException;
import org.apache.cassandra.utils.Hex;

public class PackagesVersionTypeDEB extends AbstractType<ByteBuffer> {
	private native int filevercmp_deb(String o1, String o2);
	public static final PackagesVersionTypeDEB instance = new PackagesVersionTypeDEB();

	PackagesVersionTypeDEB() {}

	public ByteBuffer compose(ByteBuffer bytes)
	{
	    return bytes.duplicate();
	}

	public ByteBuffer decompose(ByteBuffer value)
	{
	    return value;
	}

	public int compare(ByteBuffer o1, ByteBuffer o2) {
		String val1, val2;
		try {
			val1 = ByteBufferUtil.string(o1);
		} catch ( CharacterCodingException cce){
			writeToFile("CharacterCodingException per valore 1");
			System.err.println("Error: " + cce.getMessage());
                        throw new RuntimeException(cce);
		} 
		try {
			val2 = ByteBufferUtil.string(o2);
                } catch ( CharacterCodingException cce){
                        writeToFile("CharacterCodingException per valore 2");
                        System.err.println("Error: " + cce.getMessage());
                        throw new RuntimeException(cce);
                }

		try {			
			int retval;
			if ( val1.compareTo(val2) == 0 )
				retval = 0;
			else
				retval = filevercmp_deb( val1, val2 );
			String logStr = val1 + " " + val2 + " " + String.valueOf(retval);
	                writeToFile(logStr);
			return retval;
		} catch (Exception e) {
			writeToFile("Error: " + e.getMessage());
			System.err.println("Error: " + e.getMessage());
			throw new RuntimeException(e);
		}
	}

	public String getString(ByteBuffer bytes) {
		try {
			return ByteBufferUtil.string(bytes);
		} catch (CharacterCodingException e) {
			writeToFile("invalid UTF8 bytes " + ByteBufferUtil.bytesToHex(bytes));
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

	static {
		System.loadLibrary("filevercmp");
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

	void writeToFile(String str){
		try{
			  FileWriter fstream = new FileWriter("/var/log/cassandra/comparisons.log");
			  BufferedWriter out = new BufferedWriter(fstream);
			  out.write(str);
			  out.close();
			  fstream.close();
		  }catch (Exception e){
			System.err.println("Error: " + e.getMessage());
		  }
	}
}
