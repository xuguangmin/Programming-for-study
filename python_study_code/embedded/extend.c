#include <Python.h>

//Python扩展

//c接口
static PyObject* 
extend_system(PyObject * self, PyObject *args)
{
	const char * command;
	int sts;

	if (! PyArg_ParseTuple(args, "s", &command))
		return NULL;
	
	sts = system(command);
	
	return Py_BuildValue("i", sts);
}

//模块方法表
static PyMethodDef ExampleMethods[] = {
	//...
	{"system_test", (PyCFunction)extend_system, METH_VARARGS, "Ececute a shell command,"},
	//...
	{NULL, NULL, 0, NULL}
};

//初始化函数
PyMODINIT_FUNC
initextend(void)
{
	(void)Py_InitModule("extend", ExampleMethods);
}
