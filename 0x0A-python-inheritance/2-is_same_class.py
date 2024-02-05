def is_same_class(obj, a_class):
    """
    Check if obj is an instance of a_class.

    Args:
    - obj: object to check
    - a_class: class to check against

    Returns:
    - True if obj is an instance of a_class, False otherwise
    """
    return type(obj) == a_class


# Test cases
if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
