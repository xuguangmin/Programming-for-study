#include <stdio.h>
#include <ctype.h>

//测试字符是否为空格字符，包括 '', \t, \r \n, \v, \f

int main()
{
	char str[] = "123c @# FD\tsP[e\n";
	int i;
	for(i = 0; str[i] != '\0'; i++)
		if(isspace(str[i]))
			fprintf(stdout, "'%c' is a white-space character\n", str[i]);
		else
			fprintf(stdout, "'%c' not is a white-space character\n", str[i]);


	return 0;
}
