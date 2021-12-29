#!/bin/bash

while true
do 	
echo -e "Menu:\n1.Create a new fileon Ubuntu's Desktop & Insert your full details
2.Run a foor loop that counts to 200 seconds
3.Random 2 cubes and check if are equal or not
4.Run a loop from 1-10 that created files in Desktop and tgz them
5.Create 2 Users and put them in SUDO group\n"
	read -p "your choice : " choice

	if [ $choice == 1 ];
	then
		echo 1
	elif [ $choice == 2 ];
	then
		echo 2
	elif [ $choice == 3 ];
	then
		echo 3
	elif [ $choice == 4 ];
	then
		echo 4
	elif [ $choice == 5 ];
	then
		echo 5
	else
		echo you can choose only 1-5
		continue
	fi
	read -p "Do you want to exit ? y/n -> " EXIT
	if  [ $EXIT == "y" ] || [ $EXIT == "Y"]
	then
		echo "GoodBye"
		break
	else
		echo "Back to menu..\n"
	fi
done
