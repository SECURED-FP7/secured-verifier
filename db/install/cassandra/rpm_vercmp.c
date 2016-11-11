#include <stdio.h>
#include <string.h>
#include <malloc.h>


static int compare_values(const char *str1, const char *str2)
{
	if (!str1 && !str2)
		return 0;
	else if (str1 && !str2)
		return 1;
	else if (!str1 && str2)
		return -1;
	return rpmvercmp(str1, str2);
}

int filevercmp(const char *a, const char *b)
{
	const char *v1, *r1, *v2, *r2;
	const char *e1 = "0", *e2 = "0";
	char *a_copy, *b_copy, *ptr;
	int rc;

	if (strcmp(a, b) == 0)
		return 0;

	a_copy = strdup(a);
	if (a_copy == NULL) {
		printf("allocation error\n");
		return 0;
	}

	b_copy = strdup(b);
	if (b_copy == NULL) {
		printf("allocation error\n");
		free(a_copy);
		return 0;
	}

	v1 = a_copy;
	v2 = b_copy;

	ptr = strchr(a_copy, ':');
	if (ptr != NULL) {
		*ptr = '\0';
		e1 = a_copy;
		v1 = ptr + 1;
	}

	ptr = strchr(b_copy, ':');
	if (ptr != NULL) {
		*ptr = '\0';
		e2 = b_copy;
		v2 = ptr + 1;
	}

	ptr = strchr(v1, '-');
	*ptr = '\0';
	r1 = ptr + 1;

	ptr = strchr(v2, '-');
	*ptr = '\0';
	r2 = ptr + 1;

	rc = compare_values(e1, e2);
	if (!rc) {
		rc = compare_values(v1, v2);
		if (!rc)
			rc = compare_values(r1, r2);
	}

	free(a_copy);
	free(b_copy);
	return rc;
}

int main(int argc, char *argv[])
{
	printf("%d\n", filevercmp(argv[1], argv[2]));
	return 0;
}
