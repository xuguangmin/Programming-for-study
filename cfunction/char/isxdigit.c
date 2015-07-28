#include <stdio.h>
#include <ctype.h>

//测试是否为十六进制数字，0123456789ABCDEF

int main()
{
	char str[] = "123c@#FDsP[e?";
	int i;
	for(i = 0; str[i] != '\0'; i++)
		if(isxdigit(str[i]))
			fprintf(stdout, "'%c' is an xdigit\n", str[i]);
		else
			fprintf(stdout, "'%c' is not an xdigit\n", str[i]);


	return 0;
}
