"""
Write a Python program to calculate the sum of three given numbers, if
the values are equal then return three times of their sum.
"""
numbers = [int(input("Enter a number : ")), int(input("Enter a number : ")), int(input("Enter a number : "))]
if numbers[0] == numbers[1] == numbers[2]:
    print(sum(numbers))


def sum_and_check(x, y, z):
    summary = x + y + z
    if x == y == z:
        summary *= 3
    return summary


print(sum_and_check(2, 2, 2))
print(sum_and_check(1, 2, 3))



