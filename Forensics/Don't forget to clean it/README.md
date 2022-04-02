# Don't forget to clean it

Не забывай чистить историю браузера!

Volatility имеет плагин IEHistory, который позволяет достать историю браузера iehistory.

```
python3 vol.py -f ../mem.raw --profile=Win7SP1x64 iehistory
```

И находим там такое:
```
Process: 2856 iexplore.exe
Cache type "URL " at 0x3a35000
Record length: 0x180
Location: :2022040120220402: Alex@https://yandex.ru/search/?text=kctf%7Bfl4g_fr0m_br0ws3r_K113RDNVCXKDFAS%7D&clid=2242160&httpsmsn=1&msnews=1&refig=97195b70078f40c5b56f1b2d6fc7cab3
Last modified: 2022-04-01 08:08:20 UTC+0000
Last accessed: 2022-04-01 15:08:20 UTC+0000
File Offset: 0x180, Data Offset: 0x0, Data Length: 0x0
```

Флаг:
```
kctf{fl4g_fr0m_br0ws3r_K113RDNVCXKDFAS}
```
