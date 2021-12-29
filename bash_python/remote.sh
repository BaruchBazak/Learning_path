#!/bin/bash

echo -e "Menu:\n1.Print 1-10\n2.print num ** 2\n"
read choice
if [ $choice == 1 ];
then 
	echo -e "\n[execute project.py]"
	python3 project.py
elif [ $choice == 2 ];
then
	echo -e "[Execute another python file]"
	python3 project2.py
else
	echo -e "dont know what do with your choice : $choice"
fi
echo -e "GoodBye.."
