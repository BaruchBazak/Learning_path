"""
# Create list with 4 details about you : name, mail, phone, age and print it to the screen
Then create another list with 2 IPs, then add 3 more IPs, pop the 3rd IP and print how many
IPs do we have and print them.
"""

my_details = ["Baruch", 26, "05555555555", "FakeMail@gmailil.com"]

print("My name is {0}\nMy age is : {1}\nPhone number : {2}\nMail : {3}".format(my_details[0],
                                                                               my_details[1],
                                                                               my_details[2],
                                                                               my_details[3]))
# create IPs list
IPs = ["0.0.0.0", "192.168.1.0"]
print(IPs)
# append 3 address to IPS
IPs.append("255.255.255.255")
IPs.append("8.8.8.8")
IPs.append("10.10.10.0")
print(IPs)
# pop 3rd ip from IPSs
IPs.pop(2)
print(IPs)