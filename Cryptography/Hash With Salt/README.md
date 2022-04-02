# Hash With Salt

Берем словарик и добавляем в конец каждого слова соль (kaictf1337).

И запускаем брут на наш хэш
```
john --format=Raw-MD5 --wordlist=wordlist.txt hash
```

Флаг:
```
kctf{iloveyoukaictf1337}
```
