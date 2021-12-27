from time import sleep
choice = input("Menu:\n1.Insert number and ** it by 3\n2.Insert 4 IPs to a list and print it\n"
               "3.Insert 4 entries to DNS_dictionary and print it\n"
               "4.Check if a string is Palindrome\nYour choice ")

if choice == "1":
    print("The new number is :", str(int(input("Enter a number: ")) ** 3))
elif choice == "2":
    IPs = [input("Enter new IP : "), input("Enter new IP : "), input("Enter new IP : "), input("Enter new IP : ")]
    print("The new list : ", IPs)
elif choice == "3":
    dns_dict = {}
    dns_dict.update({input("Enter a URL : "): input("Enter IP : ")})
    dns_dict.update({input("Enter a URL : "): input("Enter IP : ")})
    dns_dict.update({input("Enter a URL : "): input("Enter IP : ")})
    dns_dict.update({input("Enter a URL : "): input("Enter IP : ")})
    print("The new DNS dict is\n----------------", str(dns_dict))
elif choice == "4":
    word = input("Enter a word : ")
    if word == word[::-1]:
        print(word, "is palindrome")
    else:
        print(word, "isn't palindrome")
    print()
else:
    print("Enter 1-4 only !")
