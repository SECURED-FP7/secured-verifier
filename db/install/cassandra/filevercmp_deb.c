/*
 * filevercmp_deb.c: compare DEB versions
 *
 * Copyright © 1994,1995 Ian Jackson <ian@chiark.greenend.org.uk>
 * Copyright © 2000,2001 Wichert Akkerman
 * Copyright © 2006-2014 Guillem Jover <guillem@debian.org>
 * Copyright (C) 2013 Politecnico di Torino, Italy
 *                    TORSEC group -- http://security.polito.it
 *
 * Author: Roberto Sassu <roberto.sassu@polito.it>
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 *
 */

#include <ctype.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>


struct versionrevision {
	/*
	 * taken from file "dpkg-db.h"
	 */
	unsigned long epoch;
	char *version;
	char *revision;
};

/*
 * My functions
 */
int filevercmp_deb(char* version, char* refversion);
struct versionrevision* create_struct_versionrevision(char* str);

/*
 * Implementations
 */

int cisdigit(int c) {
	/*
	 * Taken from file "utils.c"
	 */
	return (c >= '0') && (c <= '9');
}

int cisalpha(int c) {
	return ((c >= 'a') && (c <= 'z')) || ((c >= 'A') && (c <= 'Z'));
}

/**
 * Give a weight to the character to order in the version comparison.
 *
 * @param c An ASCII character.
 */
static int order(int c) {
	if (cisdigit(c))
		return 0;
	else if (cisalpha(c))
		return c;
	else if (c == '~')
		return -1;
	else if (c)
		return c + 256;
	else
		return 0;
}

static int verrevcmp(const char *val, const char *ref) {
	if (!val)
		val = "";
	if (!ref)
		ref = "";

	while (*val || *ref) {
		int first_diff = 0;

		while ((*val && !cisdigit(*val)) || (*ref && !cisdigit(*ref))) {
			int vc = order(*val), rc = order(*ref);
			if (vc != rc)
				return vc - rc;
			val++;
			ref++;
		}

		while (*val == '0')
			val++;
		while (*ref == '0')
			ref++;
		while (cisdigit(*val) && cisdigit(*ref)) {
			if (!first_diff)
				first_diff = *val - *ref;
			val++;
			ref++;
		}
		if (cisdigit(*val))
			return 1;
		if (cisdigit(*ref))
			return -1;
		if (first_diff)
			return first_diff;
	}
	return 0;
}


/**
 * Parse a version string and check for invalid syntax.
 *
 * Distinguish between lax (warnings) and strict (error) parsing.
 *
 * @param rversion The parsed version.
 * @param string The version string to parse.
 *
 * @retval  0 On success.
 * @retval -1 On failure
 */
int
parseversion(struct versionrevision *rversion, const char *string)
{
  char *hyphen, *colon, *eepochcolon;
  const char *end, *ptr;
  unsigned long epoch;

  if (!*string) {
    printf("version string is empty\n");
    return -1;
  }

  /* Trim leading and trailing space. */
  while (*string && isblank(*string))
    string++;
  /* String now points to the first non-whitespace char. */
  end = string;
  /* Find either the end of the string, or a whitespace char. */
  while (*end && !isblank(*end))
    end++;
  /* Check for extra chars after trailing space. */
  ptr = end;
  while (*ptr && isblank(*ptr))
    ptr++;
  if (*ptr) {
    printf("version string has embedded spaces\n");
    return -1;
  }

  colon= strchr(string,':');
  if (colon) {
    epoch= strtoul(string,&eepochcolon,10);
    if (colon != eepochcolon) {
      printf("epoch in version is not number\n");
      return -1;
    }
    if (!*++colon) {
      printf("nothing after colon in version number\n");
      return -1;
    }
    string= colon;
    rversion->epoch= epoch;
  } else {
    rversion->epoch= 0;
  }
//  rversion->version= nfstrnsave(string,end-string);
// Replaced by POL
  rversion->version= calloc(end-string+1, sizeof(char));
  if (rversion->version == NULL) {
    printf("out of memory\n");
    return -1;
  }
  strncpy(rversion->version, string, end-string);
  hyphen= strrchr(rversion->version,'-');
  if (hyphen)
    *hyphen++ = '\0';
  rversion->revision= hyphen ? hyphen : "";

  /* XXX: Would be faster to use something like cisversion and cisrevision. */
  ptr = rversion->version;
  if (*ptr && !cisdigit(*ptr++)) {
    printf("version number does not start with digit\n");
    return -1;
  }
  for (; *ptr; ptr++) {
    if (!cisdigit(*ptr) && !cisalpha(*ptr) && strchr(".-+~:", *ptr) == NULL) {
      printf("invalid character in version number\n");
      return -1;
    }
  }
  for (ptr = rversion->revision; *ptr; ptr++) {
    if (!cisdigit(*ptr) && !cisalpha(*ptr) && strchr(".+~", *ptr) == NULL) {
      printf("invalid character in revision number\n");
      return -1;
    }
  }

  return 0;
}

struct versionrevision* create_struct_versionrevision(char* str) {	
	struct versionrevision* vr = calloc(1, sizeof(struct versionrevision));
	if (vr == NULL) {
		printf("versionrevision: out of memory\n");
		return vr;
	}
	parseversion(vr, str);
	return vr;
}

void free_struct_versionrevision(struct versionrevision *vr) {
	if (vr == NULL)
		return;
	if (vr->version != NULL)
		free(vr->version);
	free(vr);
}

int versioncompare(const struct versionrevision *version,
                   const struct versionrevision *refversion) {
  int r;

  if (version->epoch > refversion->epoch) return 1;
  if (version->epoch < refversion->epoch) return -1;
  r= verrevcmp(version->version,refversion->version);  if (r) return r;
  return verrevcmp(version->revision,refversion->revision);
}

int filevercmp_deb(char* version, char* refversion) {
	/*
	 * This function it's a wrapper to use the ubuntu implementation of the version comparison
	 */
	int result;
	struct versionrevision *vr1 = create_struct_versionrevision(version);
	struct versionrevision *vr2 = create_struct_versionrevision(refversion);
	if (vr1 == NULL || vr2 == NULL) {
		result = -2;
		goto out;
	}
	
	result = versioncompare(vr1, vr2);
out:
	free_struct_versionrevision(vr1);
	free_struct_versionrevision(vr2);
	return result;	
}
