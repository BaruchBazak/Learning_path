#!/bin/bash

echo -e "Hello\nI will run ps command and after that, execute project.py"
ps aux | grep "tcp"
echo -e "\n[execute project.py]"
python3 project.py
echo -e "GoodBye.."
