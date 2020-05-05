#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 *print_python_list_info - print python list info
 *@p: list type PyObject
 *
 *Return: Void
 */

void print_python_list_info(PyObject *p)
{
	PyObject *obj = p;
	size_t size, i, allocated;

	allocated = ((PyListObject *)p)->allocated;
	size = Py_SIZE(obj);
	printf("[*] Size of the Python List = %zu\n", size);
	printf("[*] Allocated = %zu\n", allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %zu: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
