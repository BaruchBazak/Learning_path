"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""
import datetime
date = datetime.datetime.now()
print("Current date and time :\n{0}".format(date.strftime("%Y-%m-%d %X")))
