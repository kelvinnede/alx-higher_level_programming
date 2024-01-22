#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(str(e)), file=sys.stderr)
        return False

# Uncomment the next nine lines if you want to run this script independently
# import sys
# value = 89
# has_been_print = safe_print_integer_err(value)
# if not has_been_print:
#     print("{} is not an integer".format(value))
#
# value = -89
# has_been_print = safe_print_integer_err(value)
# if not has_been_print:
#     print("{} is not an integer".format(value))
#
# value = "School"
# has_been_print = safe_print_integer_err(value)
# if not has_been_print:
#     print("{} is not an integer".format(value))
