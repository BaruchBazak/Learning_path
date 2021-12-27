"""
Write a Python program which accepts the user's first and last name
and print them in reverse order with a space between them
"""
first_name = input("Enter your name : ")
last_name = input("Enter your last name : ")
full_name = first_name + " " + last_name
print(full_name)
print("Your full name in reverse :", full_name[::-1])
