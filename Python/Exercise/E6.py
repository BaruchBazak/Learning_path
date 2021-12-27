"""
Write a Python program to find whether a given number (accept from
the user) is even or odd, print out an appropriate message to the user
"""
number = int(input("Enter a number : "))
if number % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")
