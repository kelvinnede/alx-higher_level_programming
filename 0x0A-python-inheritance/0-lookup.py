#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    obj (object): The object for which to retrieve attributes and methods.

    Returns:
    list: A list containing the names of attributes and methods of the object.
    """
    return dir(obj)


if __name__ == "__main__":
    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3

        def my_meth(self):
            pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
