dns_dict = {"My site": "10.10.10.10", "Local": "127.0.0.1", "Main site": "192.168.0.1"}


def menu():
    while True:
        choice = input("Menu:\na. IP System?\nb. DNS System?\nYour choice : ")
        if choice == "a":
            choice_ip_system_menu = input("Menu IP System\n-------------\n"
                                          "1. Search for IP address from a list\n"
                                          "2. Add IP address to a list\n"
                                          "3. Delete IP address from a list\n"
                                          "4. Print all the IPs to the screen\n")
            if choice_ip_system_menu == "1":
                search_ip()
            elif choice_ip_system_menu == "2":
                add_ip()
            elif choice_ip_system_menu == "3":
                delete_ip()
            elif choice_ip_system_menu == "4":
                print_all_ip()
            else:
                print("You can choice only 1-4")
            exit_question = input("You want to exit ? y/n --> ")
            if exit_question == "y":
                print("Good bye :)")
                break
        elif choice == "b":
            choice_dns_system_menu = input("Menu Dns System\n-------------\n"
                                           "1. Search for URL from a dictionary\n"
                                           "2. Add URL + IP address to a dictionary\n"
                                           "3. Delete URL from a dictionary\n"
                                           "4. Update the IP address of specific URL\n"
                                           "5. Print all URL:IP address\n")

            if choice_dns_system_menu == "1":
                search_url()
            elif choice_dns_system_menu == "2":
                add_url()
            elif choice_dns_system_menu == "3":
                delete_url()
            elif choice_dns_system_menu == "4":
                update_url()
            elif choice_dns_system_menu == "5":
                print_all_urls()
            else:
                print("You can choice only 1-4")
                continue
            exit_question = input("You want to exit ? y/n --> ")
            if exit_question == "y":
                print("Good bye :)")
                break

        else:
            print("You need to choice 'a' option or 'b' option")


def search_ip():
    with open("IPs.txt", "r") as file:
        file = file.read()
        ip = input("Enter ip to search : ")
        if ip in file:
            print("{0} IP inside IPs.txt".format(ip), end="\n")
        else:
            print("{0} not exist inside IPs.txt".format(ip), end="\n")


def add_ip():
    new_ip = input("Enter new IP to IPs.txt : ")
    with open("IPs.txt", "r+") as file:
        content = file.read()
        if new_ip in content:
            print("{0} this address exist in IPs.txt".format(new_ip))
        else:
            file.write("\n" + new_ip)
            print("{0} this address added to IPs.txt".format(new_ip))


def delete_ip():
    counter = 1
    with open("IPs.txt", "r+") as file:
        content = file.readlines()
        for i in content:
            print("{0} ) {1}".format(counter, i))
            counter += 1
        ip_to_delete = int(input("enter locate IP to delete from IPs.txt : "))
        content.pop(ip_to_delete - 1)
    with open("IPs.txt", "w+") as file:
        for ip in content:
            file.write(ip)


def print_all_ip():
    with open("IPs.txt", "r") as file:
        file = file.read()
        print("This is all your IPs\n-------------------\n" + file)


def search_url():
    url = input("Enter URL : ")
    if url in dns_dict.keys():
        print("The IP address for {0} is : {1}".format(url, dns_dict[url]))
    else:
        print("I do not know {0}".format(url))


def add_url():
    url = input("Enter new URL : ")
    ip = input("Enter ip address for {0} : ".format(url))
    dns_dict.update({url: ip})
    print("Url: {0} with ip : {1} add to dns_dict".format(url, ip))


def delete_url():
    url = input("Enter URL you are want to delete : ")
    if url in dns_dict:
        dns_dict.pop(url)
    else:
        print("Not found {0} .. ".format(url))


def update_url():
    print(dns_dict)
    url = input("Enter URL you are want to update : ")
    if url in dns_dict.keys():
        ip = input("Enter new IP for {0} : ".format(url))
        dns_dict[url] = ip
        print(dns_dict)
    else:
        print("{0} not found ..".format(url))


def print_all_urls():
    for url in dns_dict.keys():
        print("URL --> {0} --> IP --> {1}".format(url, dns_dict[url]))



