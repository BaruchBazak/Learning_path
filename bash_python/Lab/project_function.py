
#!/bin/python3

import os
from time import sleep
import random


def get_details():
    NAME = input("Enter your full name : ")
    AGE = int(input("Enter your age : "))
    PHONE = input("Enter your Phone number : ")
    os.system('echo "Full name : {0}\nage : {1}\nPhone number : {2}" > {0}.txt'.format(NAME, AGE, PHONE))


def counts():
    for i in range(1, 201):
        print(i)
        sleep(1)


def cubes():
    cube_one = random.randint(1,10)
    cube_two = random.randint(1,10)
    print("Cube1 = {0}\nCube2 = {1}".format(cube_one, cube_two))
    if cube_one == cube_two:
        print("The cubes equals")
    else:
        print("The cubes isn't equals")


def new_ten_files():
    for i in range(1, 11):
        print(i)
        sleep(0.5)
        os.system('touch {0}.txt'.format(i))
    os.system('tar -zcvf file.tgz 1.txt 2.txt 3.txt 4.txt 5.txt 6.txt 7.txt 8.txt 9.txt 10.txt')


def new_users():
    USER1 = input("Enter first user : ")
    USER2 = input("Enter second user : ")
    os.system('sudo useradd {0}; sudo useradd {1}; sudo usermod -a -G {0} {1}'.format(USER1, USER2))
    print("done")


new_users()
