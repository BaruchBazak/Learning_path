"""
Write a Python program to accept a filename from the user and print
the extension of that.
Sample filename : abc.java
Output : java
"""
file_name = input("Enter your filename : ")
extension = file_name.split(".")
print(extension[1])