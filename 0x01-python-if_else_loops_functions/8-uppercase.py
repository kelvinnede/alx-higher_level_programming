#!/usr/bin/python3

def uppercase(str):
    for char in str:
        uppercase_char = char
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        print("{}".format(uppercase_char), end="")
    print()
