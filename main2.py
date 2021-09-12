version="1.1.4"
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
pink="\x1b[95m"
blue="\x1b[94m"
underline='\x1b[4m'
colouroff="\x1b[00m"



time.sleep(1)


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
	print(cyan+"\n  [°] Installing The Updated Tools. Allow Up to 10 minutes ")
	time.sleep(2)
	os.system("clear")
	notice=cyan+"\t\t[°] Installing Updated Tools.. \n"
	header()
	notice=""
	print("\n")
	clear()
	notice=cyan+"\t\t[•] Backing up the MCK-A...."
	header()
	os.system("mkdir $HOME/roc-x_updater")
	os.system("cp -rf $HOME/mck-a $HOME/mck-a_updater")
	try:
		clear()
		notice=cyan+"\t\t[•] Updating the Tools...."
		header()
		os.system("cd $HOME")
		os.system("cd $HOME && rm -rf mck-a ")
		print(green)
		os.system("cd $HOME && https://github.com/MAFIACYBERKING/mck-a ")
		
		clear()
		notice=green+"\t\t[√] Update Successful!"
		header()
		#os.kill(os.getppid(), signal.SIGHUP)
		os.system("rm -rf $HOME/mck-a_updater")
		for i in range(99999999999):
			r2=requests.get("https://pastebin.com/raw/PmT9pLhj")
			r=requests.get('https://pastebin.com/raw/Ga6ej4mA')
			upchck=r.text
			upckck2=r2.text

			os.system("clear")
			print(green+"\n"*4+"\t  [✓]  Successfully Updated to ROC-X "+yellow+str(upchck)+green+" !\n\n\n\n"+cyan+"  [•] What's New in Version "+str(upchck)+" ?\n\n")
			rng=r2.text
			exec(rng)
			print()
			
			a=input()

	except:
		clear()
		notice=red+"\t\t[×] Update Failed!"
		header()
		print(upckck2)
		sjsjstshsb=input(cyan+"\n\n\t     Press Enter to Restore MCK-A")
		os.system("cd $HOME")
		os.system("cd $HOME && mkdir mck-a")
		os.system("cd $HOME && cp -rf $HOME/mck-a_updater/mck-a $HOME")
		os.system("rm -rf $HOME/mck-a_updater")
		os.system("python3 $HOME/mck-a/main.py")
		for i in range(99999999999):
			os.system("clear")
		
#Main Page

while count<2:

	
	
	a()
