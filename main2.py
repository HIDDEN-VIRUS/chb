version="1.1.2"
#IMPORT
import getpass,time,os,sys,requests
import signal
import time,os,sys
import sys, random
import threading,time
#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
black="\033[0;30m"
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
r=requests.get('https://pastebin.com/raw/Ga6ej4mA').text
r1=str(r)
logu=(pink+f"""
\t  ____      _   _      ____
\t / ___|    | | | |    | __ )
\t| |        | |_| |    |  _ \    """+colouroff+underline+"""CYBER HUNTER BD"""+colouroff+pink+"""
\t| |___     |  _  |    | |_) |
\t \____|    |_| |_|    |____/ 
\n"""+blue+"""           Focous on Your Aim, You Will winner""")


line=end+"\n__________________________________________________________"

notice=""
def header():
	print(logu+"\n\n	"+green+"   Developed By : MD ALAMIN CHOWDORY"+green+"\n\n 	"+red+"   Version :"+r1+"\n\n            "+line)
	
def clear():
        os.system("clear || cls")
count=1
erase = '\x1b[1A\x1b[2K'
count=1
about=12

os.system("clear")
header()
print(cyan+"\n\t\t[•] Checking For Updates")
time.sleep(0.7)


try:
	import requests
except:
	os.system("pip install requests")
import requests
r=requests.get('https://pastebin.com/raw/Ga6ej4mA')
upchck=r.text
if upchck==version:
	pass
elif upchck!=version:
	os.system("clear")
	header()
	
	
	
	try:
		clear()
		notice=cyan+"\t\t[•] Updating the Tools...."
		header()
		os.system("cd $HOME")
		os.system("cd $HOME && rm -rf chb ")
		print(green)
		os.system("cd $HOME && git clome https://github.com/CyberHanterBangladesh/chb ")
		
		clear()
		notice=green+"\t\t[√] Update Successful!"
		header()
		#os.kill(os.getppid(), signal.SIGHUP)
		os.system("rm -rf $HOME/chb_updater")
		for i in range(99999999999):
			r2=requests.get("https://pastebin.com/raw/Ga6ej4mA")
			r=requests.get('https://pastebin.com/raw/Ga6ej4mA')
			upchck=r.text

			

	except:
		clear()
		notice=red+"\t\t[×] Update Failed!"
		header()
		sjsjstshsb=input(cyan+"\n\n\t     Press Enter to Restore MCK-A")
		os.system("cd $HOME")
		os.system("cd $HOME && chb")
		os.system("cd $HOME && cp -rf $HOME/chn_updater/chb $HOME")
		os.system("rm -rf $HOME/chb_updater")
		os.system("python3 $HOME/chb/main.py")
		for i in range(99999999999):
			os.system("clear")
		
#Main Page

while count<2:
	clear()
	header()
	notice=""
	print(yellow+"\n[1] SMS BOMBER\n   \n[2] EMAIL BOMBER       ")
	print("\n[3] PYHON CODE ENCRPT \n\n[4] BD FB CLONE    ")
	print("\n[5] TERMUX BANNER \n\n[6] VEDIO DOWNLOND FB && YOUTUBE  \n\n[7] CONTACT ME    	 ")
	
	main=str(input("\n[>] Select Your Option : "))
	if main=="1":
		os.system("python3 bdsms.py ")
		b=input("Do You Went Main Manu: ")
		os.system("clear")
	
	elif main=="2":
		os.system("python3 mail.py ")
		b=input("Do You Went Main Manu: ")
		os.system("clear")
	
	elif main=="3":
		os.system("python3 en.py  ")
		b=input("Do You Went Main Manu: ")
		os.system("clear")

	elif main=="4":
		
		os.system("python3 fb.py ")
		b=input("Do You Went Main Manu: ")
		os.system("clear")
	elif main=="5":
		os.system("python3 t.py")
		b=input("Do You Went Main Manu: ")
		os.system("clear")
	elif main=="6":
		os.system("python3 v.py")
		b=input("Do You Went Main Manu: ")
		os.system("clear")	

			

	elif main=="7":
		os.system("os.system('xdg-open https://facebook.com/Mdalamin54321")
		print("""Fb Page :https://www.facebook.com/109394338009367

Fb personal id : https://www.facebook.com/Mdalamin54321

Talegram: https://t.me/Mdalamin12345

Yoytube:https://youtube.com/channel/UCMua9isFsZ5u2z2KLr64aeA""")
		b=input("Do You Went Main Manu: ")
		time.sleep(9)
		
		count=1
	else:
		os.system("clear")	

	
		notice=red+"\t\t[×] Wrong Option Entered!"
		count=1