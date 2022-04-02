# CBC IV

У нас режим шифрования CBC и начальный вектор должен быть рандомным, а тут у нас такой себе рандомным
Можем просто перебрать все возможные варианты

```Python
def decrypt(key, msg):
    crypto = AES.new(key, AES.MODE_CBC, key)
    return crypto.decrypt(pad(msg, 16))


dt = open('top_secret_Gergert.evil_ransomware_29', 'rb').read()

while True:
    key = os.urandom(2) + ("A" * 14).encode('utf-8')
    dec = decrypt(key, dt).decode('utf-8', errors='ignore')

    if dec.__contains__('kctf'):
        print(dec)
        break
```

Флаг: 
```
kctf{r4ns0mw4r3_haV3_4Lr34Dy_g0t_Ev3ry0n3}
```
