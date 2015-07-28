#include <stdio.h>
#include <ctype.h>

//是否为可打印字符

int main()
{
	char str[] = "1#23SD kd k ";
	int i;
	for(i = 0; str[i] != '\0'; i++)
		if(isgraph(str[i]))
			fprintf(stdout, "str[%d] is an printable charater '%c'\n", i, str[i]);
		else
			fprintf(stdout, "str[%d] is not an printable charater '%c'\n", i, str[i]);

	return 0;
}
