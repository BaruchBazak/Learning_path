"""
Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
"""
Sample_Dictionary = {0: 10, 1: 20}
Sample_Dictionary.update({int(input("Enter key : ")): int(input("Enter value : "))})
print(Sample_Dictionary)