"""
Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""
first_string = input("Enter your string : ")
second_string = input("Enter your string : ")
print(second_string[0:2] + first_string[2:], first_string[0:2] + second_string[2:])
