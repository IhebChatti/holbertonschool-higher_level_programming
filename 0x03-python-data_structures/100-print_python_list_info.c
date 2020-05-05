#include <python3.8/Python.h>

/**
 * 
 * 
 * 
 * 
 */

void print_python_list_info(PyObject *p)
{
	PyObject *obj = p;
	PyVarObject ob_base;
	size_t size, i;

	size = Py_SIZE(obj);

	for (i = 0; i < size; i++)
	{
		printf("Element %zu: \n", i);
	}
}