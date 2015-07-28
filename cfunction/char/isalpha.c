#include <stdio.h>
#include <ctype.h>

int main()
{
	char str[] = "123c@#FDsP[e?";
	int i;
	for(i = 0; str[i] != '\0'; i++)
		if(isalpha(str[i]))
			fprintf(stdout, "%c is an alphanumber character\n", str[i]);
		else
			fprintf(stdout, "%c is not an alphanumber character\n", str[i]);

	return 0;
}
