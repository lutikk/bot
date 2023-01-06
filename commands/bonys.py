import json
import os
import time
from os.path import join
from random import randint
from time import gmtime
from time import strftime

from vkbottle.bot import BotLabeler, Message

from models import User

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text="бонус")
async def greeting(message: Message):
    user_db = await User.get(id=message.from_id)
    sss = randint(1, 4)
    if (time.time() - user_db.bonys) >= 86400:
        if sss == 1:
            a = randint(10, 1000)
            user_db.bitcoin += a
            user_db.bonys = time.time()
            await user_db.save()
            return f"Вам выпало {a} биткойнов"
        elif sss == 2:
            a = randint(5000, 100000)
            user_db.balance += a
            user_db.bonys = time.time()
            await user_db.save()
            return f"Вам выпало {a}$"
        elif sss == 3:
            a = randint(100, 1000)
            user_db.experience += a
            user_db.bonys = time.time()
            await user_db.save()
            return f"Вам выпало {a} опыта работы"
    else:
        l = user_db.bonys + 86400
        s = l - time.time()
        t = strftime("%H:%M:%S", gmtime(s))

        return f"Следующий бонус можно будет получить через {t}"


@bl.message(text="бонус вип")
async def greeting(message: Message):
    user_db = await User.get(id=message.from_id)
    if user_db.rank >= 1:
        sss = randint(1, 4)
        if (time.time() - user_db.bonys_vip) >= 86400:
            if sss == 1:
                a = randint(100, 10000)
                user_db.bitcoin += a
                user_db.bonys_vip = time.time()
                await user_db.save()
                return f"Вам выпало {a} биткойнов"
            elif sss == 2:
                a = randint(50000, 1000000)
                user_db.balance += a
                user_db.bonys_vip = time.time()
                await user_db.save()
                return f"Вам выпало {a}$"
            elif sss == 3:
                a = randint(100, 1000)
                user_db.experience += a
                user_db.bonys_vip = time.time()
                await user_db.save()
                return f"Вам выпало {a} опыта работы"

        else:
            l = user_db.bonys_vip + 86400
            s = l - time.time()
            t = strftime("%H:%M:%S", gmtime(s))

            return f"Следующий бонус VIP можно будет получить через {t}"


@bl.message(text="ферма")
async def greeting(message: Message):
    user_db = await User.get(id=message.from_id)
    ferma = user_db.bitcoin_ferm
    if (time.time() - user_db.bitcoin_time) >= 3600:
        if ferma == 0:
            return "У вас нет ферм\n" \
                   "Вы можете купить их командой:\n" \
                   "Купить фермы {кол-во}"
        ttt = time.time()
        ttt_itog = ttt - user_db.bitcoin_time
        s = round(ttt_itog)
        a = s / 3600  # Сколько часов прошло
        f = randint(20, 40)  # Сколько получит за час
        qq = a * f  # Сколько получит за все время с одной фермы
        q = qq * user_db.bitcoin_ferm  # сколько со всех ферм
        user_db.bitcoin += round(q)
        if user_db.pc == None or user_db.pc == "нет":
            w = ttt
        else:
            w = ttt - randint(1, 1000)
        user_db.bitcoin_time = w
        await user_db.save()
        return f"Вы собрали с фермы {round(q)} биткойнов"
    else:
        l = user_db.bitcoin_time + 3600
        s = l - time.time()
        t = strftime("%M:%S", gmtime(s))

        return f"Следующие биткойны можно будет получить через {t}"


@bl.message(text="купить фермы <a:int>")
async def greeting(message: Message, a: int):
    if a <= 0:
        return

    user_db = await User.get(id=message.from_id)
    balans = user_db.balance
    s = a * 2000000
    if user_db.rank >= 1:
        aaaa = user_db.bitcoin_ferm + a
        if aaaa <= 10000:
            if balans >= s:
                user_db.balance = balans - s
                user_db.bitcoin_ferm += a
                user_db.bitcoin_time = time.time()
                await user_db.save()
                return f"Вы приобрели {a} ферм"
            q = s - user_db.balance
            return f"Для покупки {a} ферм вам не хватает {q}$"
        else:
            return "Вы не можете купить больше 10000 ферм"
    aaaa = user_db.bitcoin_ferm + a
    if aaaa <= 5000:
        if balans >= s:
            user_db.balance = balans - s
            user_db.bitcoin_ferm += a
            user_db.bitcoin_time = time.time()
            await user_db.save()
            return f"Вы приобрели {a} ферм"
        q = s - user_db.balance
        return f"Для покупки {a} ферм вам не хватает {q}$"
    else:
        return "Вы не можете купить больше 5000 ферм"


@bl.message(text="продать фермы <a:int>")
async def greeting(message: Message, a: int):
    if a <= 0:
        return
    user_db = await User.get(id=message.from_id)
    ferm = user_db.bitcoin_ferm
    if ferm >= a:
        sss = a * 1000000
        user_db.balance += a * 1000000
        user_db.bitcoin_ferm = ferm - a
        await user_db.save()
        return f"Вы продали {a} ферм за {sss} долларов"
    return "У вас нету столько ферм"


@bl.message(text=["продать <a:int> биткойнов", "продать биткойны <a:int>"])
async def greeting(message: Message, a: int):
    if a <= 0:
        return
    user_db = await User.get(id=message.from_id)
    bit = user_db.bitcoin
    if bit >= a:
        sss = bit - a
        user_db.bitcoin = sss
        bit = json.load(open('bitcoin/bit.json'))
        aaa = bit['bitc_pr']
        www = aaa * a
        user_db.balance += www
        await user_db.save()
        return f"Вы продали {a} биткойнов за {www}$"
    return 'У вас нету столько биткойнов'


@bl.message(text=["продать все биткойны", "продать биткойны все"])
async def greeting(message: Message):
    user_db = await User.get(id=message.from_id)
    bit = user_db.bitcoin
    a = user_db.bitcoin
    if a <= 0:
        return
    if bit >= a:
        sss = bit - a
        user_db.bitcoin = sss
        bit = json.load(open('bitcoin/bit.json'))
        aaa = bit['bitc_pr']
        www = aaa * a
        user_db.balance += www
        await user_db.save()
        return f"Вы продали {a} биткойнов за {www}$"


@bl.message(text=["купить <a:int> биткойнов", "купить биткойны <a:int>"])
async def greeting(message: Message, a: int):
    if a <= 0:
        return
    user_db = await User.get(id=message.from_id)
    balans = user_db.balance
    bit = json.load(open('bitcoin/bit.json'))
    w = bit['bitc']  # цена одного биткойна
    sss = a * w  # цена всех биткойнов
    if balans >= sss:
        user_db.balance = balans - sss
        user_db.bitcoin += a
        await user_db.save()

        return f"Вы купили {a} биткойнов за {sss}$"

    q = sss - user_db.balance
    return f"Для покупки {a} биткойнов вам не хватает {q}$"


@bl.message(text="курс")
async def greeting(message: Message):
    bit = json.load(open('bitcoin/bit.json'))
    w = bit['bitc']  # цена одного биткойна
    s = bit['bitc_pr']
    await message.answer(f'Курс покупки биткойна {w}$\n\n'
                         f'Курс продажи биткойна {s}$')


@bl.message(text="+курс <a:int>")
async def greeting(message: Message, a: int):
    user_db = await User.get(id=message.from_id)
    if user_db.rank >= 5:
        bit = json.load(open('bitcoin/bit.json'))
        bit['bitc'] += a
        bit['bitc_pr'] += a
        dirik = os.getcwd()
        with open(join(dirik, 'bitcoin', f'bit.json'), 'w') as f:
            f.write(json.dumps(bit, ensure_ascii=False, indent=2))
        return f"Курс на покупку {bit['bitc']}$\n\n" \
               f"Курс на продажу {bit['bitc_pr']}$"


@bl.message(text="-курс <a:int>")
async def greeting(message: Message, a: int):
    user_db = await User.get(id=message.from_id)
    if user_db.rank >= 5:
        bit = json.load(open('bitcoin/bit.json'))
        bit['bitc'] -= a
        bit['bitc_pr'] -= a
        dirik = os.getcwd()
        with open(join(dirik, 'bitcoin', f'bit.json'), 'w') as f:
            f.write(json.dumps(bit, ensure_ascii=False, indent=2))
        return f"Курс на покупку {bit['bitc']}$\n\n" \
               f"Курс на продажу {bit['bitc_pr']}$"
