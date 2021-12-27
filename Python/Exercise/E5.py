"""
Write a Python program that accepts an integer (n) and computes the
value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""
number = input("Enter integer : ")
results = int(number) + int(number * 2) + int(number * 3)
print(results)
