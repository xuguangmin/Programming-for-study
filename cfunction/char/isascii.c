#include <stdio.h>
#include <ctype.h>

//测试是否为ascii[0-127]

int main()
{
	int i;
	for(i = 125; i<130; i++)
		if(isascii(i))
			fprintf(stdout, "%d is an ascii character'%c'\n", i, i);
		else
			fprintf(stdout, "%d is not an ascii character\n", i);

	return 0;
}
