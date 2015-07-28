#include <stdio.h>
#include <ctype.h>

//检查是否为小写字母
int main()
{
	char str[] = "123@#FDsP[e?";
	int i;
	for(i = 0; str[i] != '\0'; i++)
		if(islower(str[i]))
			fprintf(stdout, "%c is a lower-case character \n", str[i]);
		else
			fprintf(stdout, "%c is not a lower-case character \n", str[i]);


	return 0;
}
