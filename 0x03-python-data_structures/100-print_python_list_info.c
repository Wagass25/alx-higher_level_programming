#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid argument: object is not a list\n");
        return;
    }

    int size = PyList_Size(p);
    int i;
    PyObject *item;
    PyListObject *list = (PyListObject *) p;
    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", (int) list->allocated);
    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
