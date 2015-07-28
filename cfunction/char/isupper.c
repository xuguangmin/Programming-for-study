#include <stdio.h>
#include <ctype.h>

int main()
{
	char str[] = "123c@3#FDsP[e?";
	int i;
	for(i = 0; str[i] != '\0'; i++)
		if(isupper(str[i]))
			fprintf(stdout, "'%c' is an uppercase\n", str[i]);
		else
			fprintf(stdout, "'%c' is an uppercase\n", str[i]);



	return 0;
}
