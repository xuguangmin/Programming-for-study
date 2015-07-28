#include <stdio.h>
#include <ctype.h>

//测试字符是否为标点符号或特殊符号,非空格，非数字，非英文字母

int main()
{
	char str[] = "123@ #FDsP[e?";
	int i;
	for(i = 0; str[i] != '\0'; i++)
		if(ispunct(str[i]))
			fprintf(stdout, "'%c' true\n", str[i]);
		else
			fprintf(stdout, "'%c' false\n", str[i]);

	return 0;
}
