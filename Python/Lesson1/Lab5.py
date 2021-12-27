"""
Create a dictionary with 5 name & money
then sun the money of the first & last names and print it to screen
after, adda new name with the same of the money you calculated before
in the end, print the number of entries and check if "idan" is inside
"""

dict_names = {"Dudu": 25000, "Eti": 20050, "Shimon": 35000, "Michael": 18000, "ido": 110000}
print(dict_names)

total_amount = dict_names["Dudu"] + dict_names["ido"]
print("The total amount of money of Dudu and Ido is :", total_amount)

# dict_names["Yoel"] = total_amount
dict_names.update({"Yoel": total_amount})
print(dict_names)
print("The number entries : {}".format(len(dict_names)))
print("Idan" in dict_names)
