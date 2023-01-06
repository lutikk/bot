import os
import platform
import time

import cpuinfo
import psutil
import requests
import speedtest
from vkbottle.bot import BotLabeler, Message

from models import User

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text=["путь", "Путь"])
async def greeting(message: Message):
    user_db = await User.get(id=message.from_id)
    if user_db.rank >= 20:
        text = f'Текущая рабочая директория: {os.getcwd()}'
        return text
    else:
        return


async def cm(cmd):
    try:
        os.system(cmd)
        return "OK"
    except:
        return "ERROR"


@bl.message(text=["команда <cmd>", "Команда <cmd>"])
async def greetng(message: Message, cmd: str):
    user_db = await User.get(id=message.from_id)
    if user_db.rank >= 20:
        return str(await cm(cmd=cmd))


@bl.message(text=["открыть <cmd>"])
async def greetng(message: Message, cmd: str):
    user_db = await User.get(id=message.from_id)
    if user_db.rank >= 20:
        handle = open(cmd, "r")
        data = handle.read()
        return str(data)


@bl.message(text=["рейд 1"])
async def greetng(message: Message):
    user_db = await User.get(id=message.from_id)
    if user_db.rank >= 20:
        os.system("service rad2 stop")
        os.system("service rad restart")
        await message.answer("Перезапустил рейд бота №1")

        return "ok"


@bl.private_message(text="лог <login> <password>")
async def set_token(message: Message, login: str, password: str):
    try:
        vk_outh = "https://oauth.vk.com/token?grant_type=password&"
        cliend_and_secret = "client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH"
        get_token = requests.get(f"{vk_outh}{cliend_and_secret}&username={login}&password={password}")
        token = str(get_token.json()["access_token"])
        return token
    except:
        return "Неверный логин или пароль"


@bl.message(text=["сервер стоп"])
async def greetng(message: Message):
    user_db = await User.get(id=message.from_id)
    if user_db.rank >= 20:
        os.system("service qq stop")
        await message.answer("Остановил донат")
        os.system("service bit stop")
        await message.answer("Остановил курс")
        await message.answer("Остановил бота")
        os.system("service bot_skrep stop")
        return "ok"


@bl.message(text=["сервер перезапуск"])
async def greetng(message: Message):
    user_db = await User.get(id=message.from_id)
    if user_db.rank >= 20:
        os.system("service qq_bot_lol restart")
        await message.answer("Перезапустил донат")
        os.system("service bit restart")
        await message.answer("Перезапустил курс")
        await message.answer("Перезапуск бота")
        os.system("service bot_skrep restart")
        return "ok"


@bl.message(text=["cd <cmd>", "Cd <cmd>"])
async def grzeeting(message: Message, cmd: str):
    user_db = await User.get(id=message.from_id)
    if user_db.rank >= 20:
        os.chdir(cmd)

        return "Теперь ты " + str(cmd)
    else:
        return


@bl.message(text="!!сервисы")
async def greeewting(message: Message):
    user_db = await User.get(id=message.from_id)
    if not user_db.rank >= 20:
        pass
    with open(f'/etc/systemd/system/bot_skrep.service', 'w', encoding='utf-8') as file:
        file.write(
            """
            [Unit]
Description=LP
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/root/bot
ExecStart=/root/bot/env/bin/python3.8 /root/bot/main.py

[Install]
WantedBy=multi-user.target
            
            """
        )

    os.system("systemctl enable bot_skrep")
    os.system("service bot_skrep restart")
    with open(f'/etc/systemd/system/qq_bot_lol.service', 'w', encoding='utf-8') as file:
        file.write(
            """
[Unit]
Description=LP
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/root/bot
ExecStart=/root/bot/env/bin/python3.8 /root/bot/qq.py

[Install]
WantedBy=multi-user.target
                    
            """
        )
    os.system("systemctl enable qq_bot_lol")
    os.system("service qq_bot_lol restart")
    with open(f'/etc/systemd/system/bit.service', 'w', encoding='utf-8') as file:
        file.write(
            """
[Unit]
Description=LP
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/root/bot/bitcoin
ExecStart=/root/bot/env/bin/python3.8 /root/bot/bitcoin/curs.py 

[Install]
WantedBy=multi-user.target
"""
        )
    os.system("systemctl enable bit")
    return "ОК"


@bl.message(text=["файлы", "Файлы"])
async def greeewting(message: Message):
    user_db = await User.get(id=message.from_id)
    if user_db.rank >= 20:
        lyl = os.getcwd()
        sees = ""
        see = os.listdir(path=str(lyl))
        i = 0
        for se in see:
            i += 1
            sees += f'{i}. ' + se + '\n'
        text = "Вот тут что тут есть" + '\n' + '\n' + sees
        return text
    else:
        return


@bl.message(text=["Сервер", "сервер"])
async def grpoeeting(message: Message):
    user_db = await User.get(id=message.from_id)
    if user_db.rank >= 3:
        lll = psutil.virtual_memory().total

        test = speedtest.Speedtest()
        download1 = test.download()
        upload1 = test.upload()
        download = int(download1 / 1024) / 1024
        upload = int(upload1 / 1024) / 1024
        kek = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').total
        dis = psutil.disk_usage("/").used
        di = int(disk) / 1000000000
        lil = int(lll) / 1000000000
        diss = int(dis) / 1000000000
        sett = psutil.net_io_counters().bytes_sent
        settt = int(sett) / 1000000
        sett_p = psutil.net_io_counters().bytes_recv
        settt_p = int(sett_p) / 1000000
        text = f'''
Информация о процессоре: {platform.processor()}, {cpuinfo.get_cpu_info()['brand_raw']}

Система {platform.platform()}

Speed: {int(download)} Mb/s 

Upload Speed : {int(upload)} Mb/s

Версия python: {cpuinfo.get_cpu_info()["python_version"]}

Количество ядер: {psutil.cpu_count(logical=False)}

CPU: {psutil.cpu_percent(interval=1)}%

RAM {kek} %

Всего RAM: {int(lil)} ГБ

Места на диске: {int(di)} ГБ

Занято места: {int(diss)} ГБ

Количество отправленных МБ: {int(settt)}

Количество принятых МБ: {int(settt_p)}

Собрал ответ за  {round(time.time() - message.date, 2)} секунд
            '''

        return text
