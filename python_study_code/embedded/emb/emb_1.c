#include <Python.h>

int main()
{
	Py_Initialize();
	//解释执行参数中的语句
	PyRun_SimpleString("from time import sleep\n"
		"print 'sleep ls'\n"
		"sleep(3)\n");

	Py_Finalize();
	return 0;
}
