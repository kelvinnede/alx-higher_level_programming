#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
status = ""

print("Last digit of", number, "is", last_digit, end=" ")

if last_digit > 5:
    status = "and is greater than 5"
elif last_digit == 0:
    status = "and is 0"
else:
    status = "and is less than 6 and not 0"

print(status)
