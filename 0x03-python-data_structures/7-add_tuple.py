def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure the tuples have at least 2 elements using 0 for missing integers
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Add corresponding elements of the tuples
    result = (a[0] + b[0], a[1] + b[1])

    return result


# Example usage
if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)

    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1,)))
    print(add_tuple(tuple_a, ()))
