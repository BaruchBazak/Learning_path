"""
Write a python function that take a positive integer and
return the sum of the cube of all the positive integers smaller than the specified number
"""


def positive(num):
    num = num - 1
    total = 0
    while num > 0:
        total += num ** 3
        num -= 1
    return total


print(positive(-4))
