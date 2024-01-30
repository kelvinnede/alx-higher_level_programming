#include <Python.h>
#include <stdio.h>

/**
 * * print_python_string - Prints information about Python strings.
 * * @p: A PyObject string object.
 * */
void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");

	if (PyUnicode_Check(p))
	{
		const char *type = "compact unicode object";
		Py_ssize_t length = PyUnicode_GET_SIZE(p);
		const wchar_t *value = PyUnicode_AsWideCharString(p, NULL);

		if (PyUnicode_IS_COMPACT_ASCII(p))
			type = "compact ascii";
		else if (PyUnicode_IS_COMPACT(p) && !PyUnicode_IS_ASCII(p))
			type = "compact unicode object";
		else
			type = "compact unicode object";

		printf("  type: %s\n", type);
		printf("  length: %ld\n", length);
		printf("  value: %ls\n", value);

		PyMem_Free((void *)value);
	}
	else
	{
		printf("  [ERROR] Invalid String Object\n");
	}
}
