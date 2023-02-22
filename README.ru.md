# "Камень, Ножницы, Бумага" Telegram бот на python
<img src="https://avatars.mds.yandex.net/get-dialogs/758954/2fa17e69fbe35a68007f/orig"  width="100" height="100">

Простой бот для игры в камень, ножницы,
бумага на платформе Telegram, написанный
на **[python](https://www.python.org/)**
с использованием библиотеки **[aiogram3](https://docs.aiogram.dev/en/dev-3.x/install.html)**.
___

## Установка и запуск
1. Заходим на официальный сайт питона(**[тык](https://www.python.org/**)**) и скачиваем последнюю версию. 

    Выбираем файл - Windows installer (64-bit).

    Скачиваем, устанавливаем. При установке, **обязательно поставьте галочку на "Add Python to path"**


2. Копируете или скачиваете себе код, затем в файле `.env.example` вставляете свой токен, полученный у [BotFather](https://t.me/BotFather) в телеграмме,
   **вставлять токен нужно без пробелов**.

   **После обязательно измените имя файла `.env.example` на `.env`!**


3.  Далее нужно установить необходимые библиотеки, для этого открываем консоль и вводим следующие команды по очереди:
   
   ```
   pip install --upgrade pip
   ```
   ```
   pip install -r requirements.txt
   ```
   
   Поскольку бот написан на aiogram3, а это еще бета версия библиотеки, ее нужно устанавливать специальной командой ([подробнее тут](https://docs.aiogram.dev/en/dev-3.x/install.html))
   ```
   pip install -U --pre aiogram
   ```


4. После установки всех библиотек запускаем файл `bot.py` и бот выходит в сеть!:tada:
___


 