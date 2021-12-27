"""
 Write a Python program to print a specified list after removing the 0th,
4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
"""
import time

sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(sample_list)
print("working on it")
time.sleep(3)
sample_list.pop(5)
sample_list.pop(4)
sample_list.pop(0)
print(sample_list)
