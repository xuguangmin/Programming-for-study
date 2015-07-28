#include <Python.h>

int 
main(int argc, char **argv)
{
	PyObject *pName, *pModule, *pDict, *pFunc;
	PyObject *pArgs, *pValue;
	int i;

	//判断参数个数
	if(argc < 3) {
		fprintf(stderr, "Usage:call python_file function_name [args]\n");
		return 1;
	}
	//初始化python解释环境
	Py_Initialize();
	pName = PyString_FromString("ari.py");//将模块名字转化为Python的string对象
	/*Error checking of pName left out*/

	pModule = PyImport_Import(pName);//将此模块加载
	
	Py_DECREF(pName);//手工对参考计数进行管理，实现Python解释器对Python对象的内存回收
	if (pModule != NULL) {
		//获取函数
		pFunc = PyObject_GetAttrString(pModule, argv[2]);
		/*pFunc is a new reference*/
		if (pFunc && PyCallable_Check(pFunc)) {
			//对参数进行处理
			pArgs = PyTuple_New(argc-3);
			for (i = 0; i < argc-3; i++) {
				pValue = PyInt_FromLong(atoi(argv[i + 3]));
				if (! pValue) {
					Py_DECREF(pArgs);
					Py_DECREF(pModule);
					fprintf(stderr, "Cannot convert argument\n");
					return 1;
				}
				/*pValue reference stolen here*/
				PyTuple_SetItem(pArgs, i, pValue);
			}
			//调用Python中的函数
			pValue = PyObject_CallObject(pFunc, pArgs);
			Py_DECREF(pArgs);
			if(pValue != NULL) {
				printf("Result of call:%ld\n", PyInt_AsLong(pValue));
				Py_DECREF(pValue);
			}
			else {
				Py_DECREF(pFunc);
				Py_DECREF(pModule);
				PyErr_Print();
				fprintf(stderr, "Call failed\n");//调用函数失败
				return 1;
			}
		}
		else {
			if (PyErr_Occurred())
				PyErr_Print();
				fprintf(stderr, "Cannot find function \"%s\"\n", argv[2]);//函数查找失败
		}
		Py_XDECREF(pFunc);
		Py_DECREF(pModule);
	}
	else {
		PyErr_Print();
		fprintf(stderr, "Failed to load \"%s\"\n", argv[1]);//Python模块加载失败
		return 1;
	}

	Py_Finalize();
	return 0;
}
