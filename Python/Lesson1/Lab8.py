"""
Menu:
1) printing 100 numbers
2) check fibo
3) randint numbers until we get 20 or we count 10 times
"""
from random import randint
while True:
    print("""
    Menu:
    1) printing 100 numbers
    2) check fibo
    3) randint numbers until we get 20 or we count 10 times
    """)
    user_choice = input("Enter your choice : ")
    if user_choice == "1":
        [print(x) for x in range(1, 101)]
    elif user_choice == "2":
        fibo = []
        for i in range(7):
            fibo.append(int(input("Enter number : ")))
        boolean = "True"
        for i in range(2, len(fibo)):
            print(fibo[i])
            print(fibo[i-1])
            print(fibo[i-2])
            print("\n")
            if fibo[i] != fibo[i-1] + fibo[i-2]:
                boolean = "False"
                break
        if boolean == "True":
            print("{0} Is it Fibo series".format(fibo))
        else:
            print("{0} Isn't Fibo series".format(fibo))
    elif user_choice == "3":
        attempts = 0
        while attempts < 10:
            attempts += 1
            random_number = randint(1, 20)
            if random_number == 20:
                print("We get 20 in {0} tries".format(attempts))
                break
            else:
                print("No have lucky in this time..")
    else:
        print("Enter 1-3 only !\n")
    exit_question = input("Do ou want to exit? y/n --> ")
    if exit_question == "y":
        print("Thank you and bye bye")
        break
