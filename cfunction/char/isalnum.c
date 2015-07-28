#include <stdio.h>
#include <ctype.h>

// int isalnum(int c)

//检查参数c是否为英文字母或阿拉伯数字，是则返回TRUE，否则返回NULL


int main()
{
	char str[] = "123c@#FDsP[e";
	int i;
	for (i = 0; str[i] != '\0'; i++)
		if (isalnum(str[i]))
			fprintf(stdout, "%c is an alphanumber character\n", str[i]);
		else
			fprintf(stdout, "%c is not an alphanumber character\n", str[i]);

	return 0;
}
