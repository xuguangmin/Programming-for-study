#include <stdio.h>
#include <ctype.h>

int main()
{
	char str[] = "123#@FDsP[?";
	int i;
	for(i = 0; str[i] != '\0'; i++)
		if(isdigit(str[i]))
			fprintf(stdout, "%d is an digit character\n", str[i]);
		else
			fprintf(stdout, "%d is not an digit character\n", str[i]);


	return 0;
}
