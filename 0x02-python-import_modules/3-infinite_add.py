#!/usr/bin/python3
from sys import argv

args = argv[1:]
result = sum(map(int, args))

print(result)
