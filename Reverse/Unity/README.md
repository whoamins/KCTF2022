# Unity

На вход дается игра, в которой мы не можем прыгать, а нам очень нужно, что бы заработать очки.

![image](https://user-images.githubusercontent.com/66217512/161377682-9b017e8d-11c1-42b6-9b8f-adccd2c1d575.png)

Для победы нужно набрать 1000 баллов.

Исходный код хранится в ```Assembly-CSharp.dll```

Открываем его в [dnSpy](https://github.com/dnSpy/dnSpy/releases/tag/v6.1.8)

В скрипте ```some_script.cs``` мы можем найти метод ```lol```, который находит ```some_image``` и меняет его положение координат X и Y на 0.

lol() вызывается только тогда, когда мы набираем 1000 баллов. Но мы же даже прыгать не можем....

![image](https://user-images.githubusercontent.com/66217512/161377789-95f9cf17-768e-4f17-a5d6-4ea84ebec0cf.png)


dnSpy и другие инструменты позволяют патчить программы, вот и мы запатчим игру.

Будем вызывать метод lol() в методе Update(). Update() вызывается каждый кадр.

![image](https://user-images.githubusercontent.com/66217512/161377955-75705867-aacc-4423-97e1-20056719940c.png)

Сохраняем, запускаем и получаем флаг

![image](https://user-images.githubusercontent.com/66217512/161377992-60eaec0d-105f-4ba2-9a32-c313c232aa54.png)

Флаг:
```
kctf{G4M3_D3V_1S_H4RD}
```
