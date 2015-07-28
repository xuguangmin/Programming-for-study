#include<stdio.h>
#include<graphics.h>
int main()
{
	int gdriver=DETECT,gmode;
	registerbgidriver(EGAVGA_driver):  / *建立独立图形运行程序 */
	initgraph( gdriver, gmode,"c:\\tc");
	bar3d(50,50,250,150,20,1);
	getch();
	closegraph();
	return 0;
} 
