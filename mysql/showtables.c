#include <mysql/mysql.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
	MYSQL *conn;
	MYSQL_RES *res;
	MYSQL_ROW row;
	
	char server[] = "localhost";
	char user[] = "root";
	char password[] = "mima";
	char database[] = "mysql";

	conn = mysql_init(NULL);


	return 0;
}
