#include <stdio.h>
#include <unistd.h>

//返回一分页的大小

int main()
{

	printf("page size = %d\n", getpagesize());
	return 0;
}
