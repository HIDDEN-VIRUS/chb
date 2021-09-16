import os 
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

import requests
os.system("pip install termux-banner ")
os.system('clear')
r=requests.get('https://pastebin.com/raw/Ga6ej4mA').text
logu=(pink+f"""
\t  ____      _   _      ____
\t / ___|    | | | |    | __ )
\t| |        | |_| |    |  _ \    """+colouroff+underline+"""CYBER HUNTER BD"""+colouroff+pink+"""
\t| |___     |  _  |    | |_) |
\t \____|    |_| |_|    |____/ 
\n"""+blue+"""           Focous on Your Aim, You Will winner""")


line=end+"\n__________________________________________________________"
def a():
	print(logu+"\n\n	"+green+"   Developed By : MD ALAMIN CHOWDORY"+green+"\n\n 	"+red+"   Version :"+r+"\n\n           Mail Bomber "+line)

a()
os.system("banner")


i=input(yellow+"/nEnter Your Banner Option :")


os.system((i))




