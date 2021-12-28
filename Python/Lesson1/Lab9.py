"""
Menu:
1.Dogs details
2.Friends list
3.N azzeret
"""


def dogs():
    dog_name = input("Enter dog's name : ")
    dog_age = int(input("Enter dog's age : "))
    print("Dog's name is {0}\nDog's age is {1}\n".format(dog_name, dog_age))


def friends():
    list_friends = []
    for i in range(5):
        list_friends.append(input("Enter a friend name: "))
    name = input("Enter new name: ")
    if name in list_friends:
        print(name, "inside list friends\n")
    else:
        print(name, "isn't inside list friends\n")


def azzeret():
    num = int(input("Enter a number: "))
    sum = 1
    for i in range(1, num + 1):
        sum *= i
    print("{0} azzeret is {1}\n".format(num, sum))


def main():
    while True:
        choice = input("Menu:\n--------\n1.Dogs details\n2.Friends list\n3.N azzeret\nYour choice: ")
        if choice == "1":
            dogs()
        elif choice == "2":
            friends()
        elif choice == "3":
            azzeret()
        else:
            print("Enter 1-3 only!\n")
            continue
        exit_question = input("Do you want to exit ? y/n --> ")
        if exit_question == "y":
            break
        else:
            print("Welcome back\n")


if __name__ == "__main__":
    main()
