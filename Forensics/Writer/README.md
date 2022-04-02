# Writer

Где пишут все писатели? Очевидно, что в блокнотах.

Для того чтобы сдампить то, что было в блокноте, нам нужно, во-первых, найти PID блокнота

```
python2 vol.py -f ../mem.raw --profile=Win7SP1x64 pslist | grep notepad
```

Вывод:
```
0xfffffa8004792060 notepad.exe            2272   1992      1       60      1      0 2022-04-01 15:06:21 UTC+0000
```

Дампим данный процесс

```
python2 vol.py -f ../mem.raw --profile=Win7SP1x64 memdump --dump-dir=./ -p 2272
```

Грепаем все вхождения kctf:
```
strings 2272.dmp | grep "kctf"
```

И в самом начале у нас показывается нужный флаг:

```
kctf{n0t3p4d_fl4g_K1T_K4I}
```
