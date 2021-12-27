"""
Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'Baruch'
Expected output: {'B': 1, 'a': 1, 'r': 1, 'u': 1, 'c': 1, 'h': 1}
"""
word = input("Enter your word : ")
tracker = {}
for char in word:
    if char in tracker.keys():
        tracker[char] += 1
    else:
        tracker[char] = 1
print(tracker)
