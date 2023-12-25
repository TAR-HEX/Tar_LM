#!/bin/bash

clear

# Banner
printf " _____          _   _ \n"
printf "|_   _|_ _ _ __| | | | _____  __\n"
printf "  | |/ _\` | '__| |_| |/ _ \ \/ /\n"
printf "  | | (_| | |  |  _  |  __/>  <\n"
printf "  |_|\__,_|_|  |_| |_|\___/_/\_\n\n"

# Sleep for 1 second
sleep 1

# Update and upgrade Termux packages
pkg update
pkg upgrade -y


pkg install python -y
pip install re
pip install requests
pip install bs4
clear

python3 linkphish.py
