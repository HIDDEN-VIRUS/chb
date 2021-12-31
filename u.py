import getpass,time,os,sys
import os 
a="1"
import signal
import time,os,sys
import sys, random
import threading,time
import os,requests
os.system("pip install mechanize ")
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
import os,sys,time,random
print("")
print("")
color = ["\033[1;31m","\033[1;32m", "\033[96m", '\33[93m' '\33[94m']
m = random.choice(color)+"Update CK "
for msg in m:
    sys.stdout.write(msg)
    sys.stdout.flush()
    time.sleep(0.09)
print("")

logu=(pink+f"""
\t  ____      _   _      ____
\t / ___|    | | | |    | __ )
\t| |        | |_| |    |  _ \    """+colouroff+underline+"""CYBER HUNTER BD"""+colouroff+pink+"""
\t| |___     |  _  |    | |_) |
\t \____|    |_| |_|    |____/ 
\n"""+blue+"""           Focous on Your Aim, You Will winner""")


line=end+"\n__________________________________________________________"
def a():
	print(logu+"\n\n	"+green+"   Developed By : MD ALAMIN CHOWDORY"+green+"\n\n 	"+red+"  \n\n            "+line)
a()

r=requests.get("https://pastebin.com/zHRgbXCi").text

r2=str(r)

if a==r2:
 pass
 os.system("python main.py")
 
else:
    print("update This Tool ")
   
    os.system("cd $home && rm -rf chb && git clone https://github.com/CyberHanterBangladesh/chb  ")
    
