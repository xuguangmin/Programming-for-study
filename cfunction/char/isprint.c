#include <stdio.h>
#include <ctype.h>

//测试字符是否为可打印字符，包含空格
int main()
{
	char str[] = "123 #0Dadf df";
	int i;
	for(i = 0; str[i] != '\0'; i++)
		if(isprint(str[i]))
			fprintf(stdout, "'%c' is a printable character\n", str[i]);
		else
			fprintf(stdout, "'%c' is not a printable character\n", str[i]);



	return 0;
}
