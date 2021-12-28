"""
Getting as input how much money we have to play
The cost of a game is 3 shekels
If there is a surplus we will return it to the customer
In each Negril turn, 2 dice, if they are identical, we won NIS 100, if they are identical, and a garden equal to 6,
we won NIS 1,000.
If they are not identical but Cube 2 is equal to 2, we won NIS 40.
If they are not identical but cube 1 is equal to 1, we won NIS 20.
"""
import random
import time

print("Welcome to our Cube game ")
print("Each turn cost 3 ILS")
Money_from_the_customer = int(input("How much money you have ?\n"))
turns = Money_from_the_customer // 3
print("You have: {0} turn(s)".format(turns))
if Money_from_the_customer % 3 != 0:
    print("Your change: {0} ILS".format(Money_from_the_customer % 3))
Customer_balance = 0

for i in range(1, turns + 1):
    print("Rolling cubes for round number {0} :\n---------------\n".format(i))
    time.sleep(2)
    cube1 = random.randint(1, 6)
    cube2 = random.randint(1, 6)
    print("Cube1: {0}\nCube2: {1}\n".format(cube1, cube2))
    if cube1 == cube2 and cube1 + cube2 == 6:
        Customer_balance += 1000
        print("You win 1000 Shekels in this round\n")
    elif cube1 == cube2:
        Customer_balance += 100
        print("You win 100 Shekels in this round\n")
    elif cube1 != cube2 and cube2 == 2:
        Customer_balance += 40
        print("You win 40 shekels in this round\n")
    elif cube1 != cube2 and cube1 == 1:
        Customer_balance += 20
        print("You win 20 shekels in this round\n")

print("Calculating you prize...")
time.sleep(3)
print("You prize : {0}".format(Customer_balance))
