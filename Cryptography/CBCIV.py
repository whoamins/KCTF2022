from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
import os

key = os.urandom(2) + ("A" * 14).encode('utf-8')


def encrypt(key, msg):
	crypto = AES.new(key, AES.MODE_CBC,key)
	return crypto.encrypt(pad(msg, 16))


dt = open('top_secret_Gergert.txt', 'rb').read()
enc_dt = encrypt(key, dt)

open('top_secret_Gergert.evil_ransomware_29', 'wb').write(enc_dt)
os.remove('top_secret_Gergert.txt')
