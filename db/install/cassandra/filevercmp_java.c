/*
 * filevercmp_java.c
 *
 * Copyright (C) 2013 Politecnico di Torino, Italy
 *                    TORSEC group -- http://security.polito.it
 *
 * Author: Roberto Sassu <roberto.sassu@polito.it>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library.  If not, see
 * <http://www.gnu.org/licenses/>.
 *
 */

#include <stdio.h>
#include "torsec_ra_cassandra_db_PackagesVersionType.h"

extern int filevercmp (const char *a, const char *b);

JNIEXPORT jint JNICALL Java_torsec_ra_cassandra_db_PackagesVersionType_filevercmp (JNIEnv *env, jobject obj, jstring o1, jstring o2)
{
	const char *a, *b;
	jint res = 0;

	a = (*env)->GetStringUTFChars(env, o1, 0);
	b = (*env)->GetStringUTFChars(env, o2, 0);
	res = filevercmp(a, b);

	(*env)->ReleaseStringUTFChars(env, o1, a);
	(*env)->ReleaseStringUTFChars(env, o2, b);
	if(res == 0)
		return 0;
	else if(res < 0)
		return -1;
	else
		return 1;
//	return res;
}
