from random import randint

from vkbottle.bot import BotLabeler, Message

from models import User

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text="магазин машины")
async def greeting(message: Message):
    text = """
1) Самокат -> 500$
2) Велосипед -> 1000$
3) Audi -> 1000000$
4) Ford -> 9000000$
5) Hyundai -> 15000000$
6) Mercedes Benz -> 20000000$
7) Nissan -> 15000000$
8) Skoda -> 16000000$
9) Volkswagen -> 25000000$
10) BMW -> 30000000$
11) Honda -> 19000000$
12) Kia -> 17000000$
13) Mazda -> 23000000$
14) Mitsubishi -> 32000000$
15) Renault -> 35000000$
16) Toyota -> 40000000$

Команда: Купить машину {номер машины}   
    """
    return text


@bl.message(text="магазин компьютеры")
async def greeting(message: Message):
    text = """
1) DЕXР Аquilоn О175 -> 2 377 300$
2) HYРЕRРС NЕО -> 7 027 300$
3) DЕLL Аliеnwаrе Аurоrа R7 ->74 726 623$
4) HYРЕRРС СОSMОS X 3 -> 191 827 929$
5) HYРЕRРС РRЕMIUM -> 654 830 700 $

Команда: Купить компьютер {номер компьютера} 
    """
    return text


@bl.message(text=["магазин самолёты", "магазин самолеты"])
async def greeting(message: Message):
    text = """
1) Параплан -> 10 003$
2) АН-2 -> 82 825$
3) Сеssnа-172Е -> 92 748$
4) Suреrmаrinе Sрitfirе -> 103 030$
5) BRM NG-5 -> 202 928 $
6) Сеssnа T210 -> 94 529 938$
7) Bеесhсrаft 1900D -> 433 344 940$
8) Сеssnа 550 -> 176 162 773$
9) Hаwkеr 4000 -> 539 299 299$
10) Lеаrjеt 31 -> 28 288 384 894$
11) Аirbus А318 -> 838 848 492$
12) F-35А -> 299 393 849$
13) Bоеing 747-430 Сustоm -> 19 293 994 884$
14) С-17А Glоbеmаstеr III -> 10 000 000 000$
15) F-22 Rарtоr -> 250 000 000 000$
16) Аirbus 380 Сustоm -> 7 209 888 484$
17) B-2 Sрirit Stеаlth Bоmbе -> 91 728 616 626$

Команда: Купить самолёт {номер самолёта}
    """
    return text


@bl.message(text=["магазин вертолёты", "магазин вертолеты"])
async def greeting(message: Message):
    text = """
1) Шарик с пропеллером -> 12 533$
2) RоtоrWау Еxес 162F -> 32 533$
3) Rоbinsоn R44 -> 43 467$
4) Hillеr UH-12С -> 5 867 866$
5) АW119 Kоаlа -> 6 789 999$
6) MBB BK 117 -> 8 898 776$
7) Еurосорtеr ЕС130 -> 8 390 000$
8) Lеоnаrdо АW109 Роwеr -> 98 075 324$
9) Sikоrskу S-76 -> 1 242 434 360$
10) Bеll 429WLG -> 11 545 546$
11) NHI NH90 - > 124 483 733$
12) Kаzаn Mi-35M -> 944 837 265 654$
13) Bеll V-22 Оsрrеу -> 134 476 363 264$

Команда: Купить вертолёт {номер вертолёта}
    """
    return text


@bl.message(text="магазин телефоны")
async def greeting(message: Message):
    text = """
1) Nokia 108 -> $1 200
2) Nokia 3310 -> $2 200
3) Nokia 6300 Gold Edition -> $3 200
4) HTC S740 -> $45 064
5) iPhone 3G -> $64 246
6) Samsung Galaxy -> $735 336
7) HTC Legend -> $214 679
8) Samsung Galaxy J6 -> $364 606
9) iPhone 5 -> $1 744 736
10) Honor 7A -> $6 423 466
11) iPhone 7s+ -> $36 254 241
12) Honor 6A -> $84 773 366
13) iPhone 11 -> $ 486 521 541
14) iPhone 12 mini -> $688 476 362
15) iPhone 12 Pro -> $10 000 000 000

Команда: Купить телефон {номер телефона}
    """

    return text


async def apc(user_id, lyl):
    user_db = await User.get(id=user_id)
    user_db.pc = lyl
    await user_db.save()


async def airc(user_id, lyl):
    user_db = await User.get(id=user_id)
    user_db.aircopt = lyl
    await user_db.save()


async def airpl(user_id, lyl):
    user_db = await User.get(id=user_id)
    user_db.airplane = lyl
    await user_db.save()


async def mob(user_id, lyl):
    user_db = await User.get(id=user_id)
    user_db.mobile = lyl
    await user_db.save()


async def imus(user_id, lyl):
    user_db = await User.get(id=user_id)
    user_db.transport = lyl
    await user_db.save()


async def manii_ig(user_id, mani):
    user_db = await User.get(id=user_id)
    a = user_db.balance
    s = int(a) - int(mani)
    user_db.balance = s
    await user_db.save()


async def mani_ig(user_id, mani):
    user_db = await User.get(id=user_id)
    a = user_db.balance
    s = int(a) + int(mani)
    user_db.balance = s
    await user_db.save()


##############################################
##############################################
##############################################


@bl.message(text="купить компьютер <pc:int>")
async def greeting(message: Message, pc: int):
    lol = message.from_id
    user_db = await User.get(id=message.from_id)
    if 1 == 1:

        im = user_db.pc
        lel = user_db.balance
        pcs = ['DЕXР Аquilоn О175',  # 1 #index=0
               'HYРЕRРС NЕО',  # 2 #index=1
               'DЕLL Аliеnwаrе Аurоrа R7',  # 3 #index=2
               'HYРЕRРС СОSMОS X 3',  # 4 #index=3
               'HYРЕRРС РRЕMIUM']
        ##СТОЙМОСТЬ
        cost = [2377300,  # 1 #index=0
                7027300,  # 2 #index=1
                74726623,  # 3 #index=2
                191827929,  # 4 #index=3
                654830700]
        if str(im) == "нет" or im == None:
            index = pc - 1
            if pc >= 1 and pc <= 5:
                if float(lel) >= cost[index]:
                    await apc(user_id=lol, lyl=pcs[index])
                    await manii_ig(user_id=lol, mani=cost[index])
                    return f'Вы приобрели "{pcs[index]}"'
                else:
                    s = cost[index] - lel
                    return f'На покупку "{pcs[index]}" вам не хватает {s}$'
            else:
                return "Нет такой цифры"
        else:
            return f'Сначала надо избавиться от "{im}"\nКоманда: продать вертолет'


@bl.message(text="продать компьютер")
async def greeting(message: Message):
    lol = message.from_id
    user_db = await User.get(id=lol)
    if 1 == 1:
        im = user_db.pc
        pcs = ['DЕXР Аquilоn О175',  # 1 #index=0
               'HYРЕRРС NЕО',  # 2 #index=1
               'DЕLL Аliеnwаrе Аurоrа R7',  # 3 #index=2
               'HYРЕRРС СОSMОS X 3',  # 4 #index=3
               'HYРЕRРС РRЕMIUM']
        ##СТОЙМОСТЬ
        cost = [2377300,  # 1 #index=0
                7027300,  # 2 #index=1
                74726623,  # 3 #index=2
                191827929,  # 4 #index=3
                654830700]
        if str(im) == "нет" or im == None:
            return "Вам нечего продавать"
        else:
            index = pcs.index(im)
            costMax = cost[index]
            wls = randint(1, costMax)
            await apc(user_id=lol, lyl="нет")
            await mani_ig(user_id=lol, mani=wls)
            return f"Вы продали {im} за {wls}$"


@bl.message(text=["купить вертолёт <aircopt:int>", "купить вертолет <aircopt:int>"])
async def greeting(message: Message, aircopt: int):
    lol = message.from_id
    user_db = await User.get(id=message.from_id)
    if 1 == 1:

        im = user_db.aircopt
        lel = user_db.balance
        aircoptes = ['Шарик с пропеллером',  # 1 #index=0
                     'RоtоrWау Еxес 162F',  # 2 #index=1
                     'Rоbinsоn R44',  # 3 #index=2
                     'Hillеr UH-12С',  # 4 #index=3
                     'АW119 Kоаlа',  # 5 #index=4
                     'MBB BK 117',  # 6 #index=5
                     'Еurосорtеr ЕС130',  # 7 #index=6
                     'Lеоnаrdо АW109 Роwеr',  # 8 #index=7
                     'Sikоrskу S-76',  # 9 #index=8
                     'Bеll 429WLG',  # 10 #index=9
                     'NHI NH90',  # 11 #index=10
                     'Kаzаn Mi-35M',  # 12 #index=11
                     'Bеll V-22 Оsрrеу']
        ##СТОЙМОСТЬ
        cost = [12533,  # 1 #index=0
                32533,  # 2 #index=1
                43467,  # 3 #index=2
                5867866,  # 4 #index=3
                6789999,  # 5 #index=4
                8898776,  # 6 #index=5
                8390000,  # 7 #index=6
                98075324,  # 8 #index=7
                1242434360,  # 9 #index=8
                11545546,  # 10 #index=9
                124483733,  # 11 #index=10
                944837265654,  # 12 #index=11
                134476363264]
        if str(im) == "нет" or im == None:
            index = aircopt - 1
            if aircopt >= 1 and aircopt <= 13:
                if float(lel) >= cost[index]:
                    await airc(user_id=lol, lyl=aircoptes[index])
                    await manii_ig(user_id=lol, mani=cost[index])
                    return f'Вы приобрели "{aircoptes[index]}"'
                else:
                    s = cost[index] - lel
                    return f'На покупку "{aircoptes[index]}" вам не хватает {s}$'
            else:
                return "Нет такой цифры"
        else:
            return f'Сначала надо избавиться от "{im}"\nКоманда: продать вертолет'


@bl.message(text=["продать вертолёт", "продать вертолет"])
async def greeting(message: Message):
    lol = message.from_id
    user_db = await User.get(id=lol)
    if 1 == 1:
        im = user_db.aircopt
        aircoptes = ['Шарик с пропеллером',  # 1 #index=0
                     'RоtоrWау Еxес 162F',  # 2 #index=1
                     'Rоbinsоn R44',  # 3 #index=2
                     'Hillеr UH-12С',  # 4 #index=3
                     'АW119 Kоаlа',  # 5 #index=4
                     'MBB BK 117',  # 6 #index=5
                     'Еurосорtеr ЕС130',  # 7 #index=6
                     'Lеоnаrdо АW109 Роwеr',  # 8 #index=7
                     'Sikоrskу S-76',  # 9 #index=8
                     'Bеll 429WLG',  # 10 #index=9
                     'NHI NH90',  # 11 #index=10
                     'Kаzаn Mi-35M',  # 12 #index=11
                     'Bеll V-22 Оsрrеу']
        cost = [12533,  # 1 #index=0
                32533,  # 2 #index=1
                43467,  # 3 #index=2
                5867866,  # 4 #index=3
                6789999,  # 5 #index=4
                8898776,  # 6 #index=5
                8390000,  # 7 #index=6
                98075324,  # 8 #index=7
                1242434360,  # 9 #index=8
                11545546,  # 10 #index=9
                124483733,  # 11 #index=10
                944837265654,  # 12 #index=11
                134476363264]
        if str(im) == "нет" or im == None:
            return "Вам нечего продавать"
        else:
            index = aircoptes.index(im)
            costMax = cost[index]
            wls = randint(1, costMax)
            await airc(user_id=lol, lyl="нет")
            await mani_ig(user_id=lol, mani=wls)
            return f"Вы продали {im} за {wls}$"


@bl.message(text=["купить самолет <airplane:int>", "купить самолёт <airplane:int>"])
async def greeting(message: Message, airplane: int):
    lol = message.from_id
    user_db = await User.get(id=message.from_id)
    if 1 == 1:

        im = user_db.airplane
        lel = user_db.balance
        airplanes = ['Параплан',  # 1 #index=0
                     'АН-2',  # 2 #index=1
                     'Сеssnа-172Е',  # 3 #index=2
                     'Suреrmаrinе Sрitfirе',  # 4 #index=3
                     'BRM NG-5',  # 5 #index=4
                     'Сеssnа T210',  # 6 #index=5
                     'Bеесhсrаft 1900D',  # 7 #index=6
                     'Сеssnа 550',  # 8 #index=7
                     'Hаwkеr 4000',  # 9 #index=8
                     'Lеаrjеt 31',  # 10 #index=9
                     'Аirbus А318',  # 11 #index=10
                     'F-35А',  # 12 #index=11
                     'Bоеing 747-430 Сustоm',  # 13 #index=12
                     'С-17А Glоbеmаstеr III',  # 14 #index=13
                     'F-22 Rарtоr',  # 15 #index=14
                     'Аirbus 380 Сustоm',
                     'B-2 Sрirit Stеаlth Bоmbе']
        ##СТОЙМОСТЬ
        cost = [10003,  # 1 #index=0
                82825,  # 2 #index=1
                92748,  # 3 #index=2
                103030,  # 4 #index=3
                202928,  # 5 #index=4
                94529938,  # 6 #index=5
                433344940,  # 7 #index=6
                176162773,  # 8 #index=7
                539299299,  # 9 #index=8
                28288384894,  # 10 #index=9
                838848492,  # 11 #index=10
                299393849,  # 12 #index=11
                19293994884,  # 13 #index=12
                10000000000,  # 14 #index=13
                250000000000,
                7209888484,
                91728616626
                ]
        if str(im) == "нет" or im == None:
            index = airplane - 1
            if airplane >= 1 and airplane <= 17:
                if float(lel) >= cost[index]:
                    await airpl(user_id=lol, lyl=airplanes[index])
                    await manii_ig(user_id=lol, mani=cost[index])
                    return f'Вы приобрели "{airplanes[index]}"'
                else:
                    s = cost[index] - lel
                    return f'На покупку "{airplanes[index]}" вам не хватает {s}$'
            else:
                return "Нет такой цифры"
        else:
            return f'Сначала надо избавиться от "{im}"\nКоманда: продать самолет'


@bl.message(text=["продать самолёт", "продать самолёт"])
async def greeting(message: Message):
    lol = message.from_id
    user_db = await User.get(id=lol)
    if 1 == 1:
        im = user_db.airplane
        airplanes = ['Параплан',  # 1 #index=0
                     'АН-2',  # 2 #index=1
                     'Сеssnа-172Е',  # 3 #index=2
                     'Suреrmаrinе Sрitfirе',  # 4 #index=3
                     'BRM NG-5',  # 5 #index=4
                     'Сеssnа T210',  # 6 #index=5
                     'Bеесhсrаft 1900D',  # 7 #index=6
                     'Сеssnа 550',  # 8 #index=7
                     'Hаwkеr 4000',  # 9 #index=8
                     'Lеаrjеt 31',  # 10 #index=9
                     'Аirbus А318',  # 11 #index=10
                     'F-35А',  # 12 #index=11
                     'Bоеing 747-430 Сustоm',  # 13 #index=12
                     'С-17А Glоbеmаstеr III',  # 14 #index=13
                     'F-22 Rарtоr',  # 15 #index=14
                     'Аirbus 380 Сustоm',
                     'B-2 Sрirit Stеаlth Bоmbе']
        cost = [10003,  # 1 #index=0
                82825,  # 2 #index=1
                92748,  # 3 #index=2
                103030,  # 4 #index=3
                202928,  # 5 #index=4
                94529938,  # 6 #index=5
                433344940,  # 7 #index=6
                176162773,  # 8 #index=7
                539299299,  # 9 #index=8
                28288384894,  # 10 #index=9
                838848492,  # 11 #index=10
                299393849,  # 12 #index=11
                19293994884,  # 13 #index=12
                10000000000,  # 14 #index=13
                250000000000,
                7209888484,
                91728616626
                ]
        if str(im) == "нет" or im == None:
            return "Вам нечего продавать"
        else:
            index = airplanes.index(im)
            costMax = cost[index]
            wls = randint(1, costMax)
            await airpl(user_id=lol, lyl="нет")
            await mani_ig(user_id=lol, mani=wls)
            return f"Вы продали {im} за {wls}$"


@bl.message(text="купить телефон <mobile:int>")
async def greeting(message: Message, mobile: int):
    lol = message.from_id
    user_db = await User.get(id=message.from_id)
    if 1 == 1:

        im = user_db.mobile  ## ПОСТАВИЛ MOBILE
        lel = user_db.balance
        mobiles = ['Nokia 108',  # 1 #index=0
                   'Nokia 3310',  # 2 #index=1
                   'Nokia 6300 Gold Edition',  # 3 #index=2
                   'HTC S740',  # 4 #index=3
                   'iPhone 3G',  # 5 #index=4
                   'Samsung Galaxy',  # 6 #index=5
                   'HTC Legend',  # 7 #index=6
                   'Samsung Galaxy J6',  # 8 #index=7
                   'iPhone 5',  # 9 #index=8
                   'Honor 7A',  # 10 #index=9
                   'iPhone 7s+',  # 11 #index=10
                   'Honor 6A',  # 12 #index=11
                   'iPhone 11',  # 13 #index=12
                   'iPhone 12 mini',  # 14 #index=13
                   'iPhone 12 Pro']  # 15 #index=14
        ##СТОЙМОСТЬ
        costMob = [1200,  # 1 #index=0
                   2200,  # 2 #index=1
                   3200,  # 3 #index=2
                   45064,  # 4 #index=3
                   64246,  # 5 #index=4
                   735336,  # 6 #index=5
                   214679,  # 7 #index=6
                   364606,  # 8 #index=7
                   1744736,  # 9 #index=8
                   6423466,  # 10 #index=9
                   36254241,  # 11 #index=10
                   84773366,  # 12 #index=11
                   486521541,  # 13 #index=12
                   688476362,  # 14 #index=13
                   10000000000]  # 15 #index=14
        if str(im) == "нет" or im == None:
            index = mobile - 1
            if mobile >= 1 and mobile <= 15:
                if float(lel) >= costMob[index]:
                    await mob(user_id=lol, lyl=mobiles[index])
                    await manii_ig(user_id=lol, mani=costMob[index])
                    return f'Вы приобрели "{mobiles[index]}"'
                else:
                    s = costMob[index] - lel
                    return f'На покупку "{mobiles[index]}" вам не хватает {s}$'
            else:
                return "Нет такой цифры"
        else:
            return f'Сначала надо избавиться от "{im}"\nКоманда: продать телефон'


@bl.message(text="продать телефон")
async def greeting(message: Message):
    lol = message.from_id
    user_db = await User.get(id=lol)
    if 1 == 1:
        im = user_db.mobile
        mobiles = ['Nokia 108',  # 1 #index=0
                   'Nokia 3310',  # 2 #index=1
                   'Nokia 6300 Gold Edition',  # 3 #index=2
                   'HTC S740',  # 4 #index=3
                   'iPhone 3G',  # 5 #index=4
                   'Samsung Galaxy',  # 6 #index=5
                   'HTC Legend',  # 7 #index=6
                   'Samsung Galaxy J6',  # 8 #index=7
                   'iPhone 5',  # 9 #index=8
                   'Honor 7A',  # 10 #index=9
                   'iPhone 7s+',  # 11 #index=10
                   'Honor 6A',  # 12 #index=11
                   'iPhone 11',  # 13 #index=12
                   'iPhone 12 mini',  # 14 #index=13
                   'iPhone 12 Pro']
        ##СТОЙМОСТЬ ->->->->->->->->->->->->->->->->->->->->->->->->->->->->-> СДЕЛАЕШЬ СВОИ ЦЕНЫ И СКОПИПАСТИШЬ СЮДА
        costMob = [1200,  # 1 #index=0
                   2200,  # 2 #index=1
                   3200,  # 3 #index=2
                   45064,  # 4 #index=3
                   64246,  # 5 #index=4
                   735336,  # 6 #index=5
                   214679,  # 7 #index=6
                   364606,  # 8 #index=7
                   1744736,  # 9 #index=8
                   6423466,  # 10 #index=9
                   36254241,  # 11 #index=10
                   84773366,  # 12 #index=11
                   486521541,  # 13 #index=12
                   688476362,  # 14 #index=13
                   10000000000]
        if str(im) == "нет" or im == None:
            return "Вам нечего продавать"
        else:
            index = mobiles.index(im)
            costMax = costMob[index]
            wls = randint(1, costMax)
            await mob(user_id=lol, lyl="нет")
            await mani_ig(user_id=lol, mani=wls)
            return f"Вы продали {im} за {wls}$"


##############################################
##############################################
##############################################

@bl.message(text="купить машину <transport>")
async def greeting(message: Message, transport: str):
    lol = message.from_id
    user_db = await User.get(id=message.from_id)
    if 1 == 1:

        im = user_db.transport
        lel = user_db.balance
        if str(im) == "нет" or im == None:
            if str(transport) == "1":
                lel = user_db.balance
                if float(lel) >= 500:
                    await imus(user_id=lol, lyl="Самокат")
                    await manii_ig(user_id=lol, mani=500)
                    return "Вы приобрели Самокат"
                else:
                    s = 500 - lel
                    return f'На покупку "Самоката" вам не хватает {s}$'
            elif str(transport) == "2":

                if float(lel) >= 1000:
                    await imus(user_id=lol, lyl="Велосипед")
                    await manii_ig(user_id=lol, mani=1000)
                    return "Вы приобрели Велосипед"
                else:
                    s = 1000 - lel
                    return f'На покупку "Велосипеда" вам не хватает {s}$'
            elif str(transport) == "3":

                if float(lel) >= 1000000:
                    await imus(user_id=lol, lyl="Audi")
                    await manii_ig(user_id=lol, mani=1000000)
                    return "Вы приобрели Audi"
                else:
                    s = 1000000 - lel
                    return f'На покупку "Audi" вам не хватает {s}$'
            elif str(transport) == "4":

                if float(lel) >= 9000000:
                    await imus(user_id=lol, lyl="Ford")
                    await manii_ig(user_id=lol, mani=9000000)
                    return "Вы приобрели Ford"
                else:
                    s = 9000000 - lel
                    return f'На покупку "Ford" вам не хватает {s}$'
            elif str(transport) == "5":

                if float(lel) >= 15000000:
                    await imus(user_id=lol, lyl="Hyundai")
                    await manii_ig(user_id=lol, mani=15000000)
                    return "Вы приобрели Hyundai"
                else:
                    s = 15000000 - lel
                    return f'На покупку "Hyundai" вам не хватает {s}$'
            elif str(transport) == "6":

                if float(lel) >= 20000000:
                    await imus(user_id=lol, lyl="Mercedes Benz")
                    await manii_ig(user_id=lol, mani=20000000)
                    return "Вы приобрели Mercedes Benz"
                else:
                    s = 20000000 - lel
                    return f'На покупку "Benz" вам не хватает {s}$'
            elif str(transport) == "7":

                if float(lel) >= 15000000:
                    await imus(user_id=lol, lyl="Nissan")
                    await manii_ig(user_id=lol, mani=15000000)
                    return "Вы приобрели Nissan"
                else:
                    s = 15000000 - lel
                    return f'На покупку "Nissan" вам не хватает {s}$'
            elif str(transport) == "8":

                if float(lel) >= 16000000:
                    await imus(user_id=lol, lyl="Skoda")
                    await manii_ig(user_id=lol, mani=16000000)

                    return "Вы приобрели Skoda"
                else:
                    s = 16000000 - lel
                    return f'На покупку "Skoda" вам не хватает {s}$'
            elif str(transport) == "9":

                if float(lel) >= 25000000:
                    await imus(user_id=lol, lyl="Volkswagen")
                    await manii_ig(user_id=lol, mani=25000000)

                    return "Вы приобрели Volkswagen"
                else:
                    s = 25000000 - lel
                    return f'На покупку "Volkswagen" вам не хватает {s}$'
            elif str(transport) == "10":

                if float(lel) >= 30000000:
                    await imus(user_id=lol, lyl="BMW")
                    await manii_ig(user_id=lol, mani=30000000)

                    return "Вы приобрели BMW"
                else:
                    s = 30000000 - lel
                    return f'На покупку "BMW" вам не хватает {s}$'
            elif str(transport) == "11":

                if float(lel) >= 19000000:
                    await imus(user_id=lol, lyl="Honda")
                    await manii_ig(user_id=lol, mani=19000000)

                    return "Вы приобрели Honda"
                else:
                    s = 19000000 - lel
                    return f'На покупку "Honda" вам не хватает {s}$'
            elif str(transport) == "12":

                if float(lel) >= 17000000:
                    await imus(user_id=lol, lyl="Kia")
                    await manii_ig(user_id=lol, mani=17000000)

                    return "Вы приобрели Kia"
                else:
                    s = 17000000 - lel
                    return f'На покупку "Kia" вам не хватает {s}$'
            elif str(transport) == "13":

                if float(lel) >= 23000000:
                    await imus(user_id=lol, lyl="Mazda")
                    await manii_ig(user_id=lol, mani=23000000)

                    return "Вы приобрели Mazda"
                else:
                    s = 23000000 - lel
                    return f'На покупку "Mazda" вам не хватает {s}$'
            elif str(transport) == "14":

                if float(lel) >= 32000000:
                    await imus(user_id=lol, lyl="Mitsubishi")
                    await manii_ig(user_id=lol, mani=32000000)

                    return "Вы приобрели Mitsubishi"
                else:
                    s = 32000000 - lel
                    return f'На покупку "Mitsubishi" вам не хватает {s}$'
            elif str(transport) == "15":

                if float(lel) >= 35000000:
                    await imus(user_id=lol, lyl="Renault")
                    await manii_ig(user_id=lol, mani=35000000)

                    return "Вы приобрели Renault"
                else:
                    s = 35000000 - lel
                    return f'На покупку "Renault" вам не хватает {s}$'
            elif str(transport) == "16":

                if float(lel) >= 40000000:
                    await imus(user_id=lol, lyl="Toyota")
                    await manii_ig(user_id=lol, mani=40000000)

                    return "Вы приобрели Toyota"
                else:
                    s = 40000000 - lel
                    return f'На покупку "Toyota" вам не хватает {s}$'
            else:
                return "Нету такого номера"


        else:

            return f'Сначала надо избавиться от "{im}"\nКоманда: Продать Машину'


@bl.message(text="продать машину")
async def greeting(message: Message):
    lol = message.from_id
    user_db = await User.get(id=lol)
    if 1 == 1:

        im = user_db.transport
        if str(im) == "нет" or im == None:
            return "Вам нечего продавать"
        else:
            if str(im) == "Самокат":
                await imus(user_id=lol, lyl="нет")
                l = randint(1, 500)
                await mani_ig(user_id=lol, mani=l)
                return f"Вы продали {im} за {l}$"
            elif str(im) == "Велосипед":
                await imus(user_id=lol, lyl="нет")
                l = randint(1, 1000)
                await mani_ig(user_id=lol, mani=l)
                return f"Вы продали {im} за {l}$"
            elif str(im) == "Audi":
                await imus(user_id=lol, lyl="нет")
                l = randint(1, 1000000)
                await mani_ig(user_id=lol, mani=l)
                return f"Вы продали {im} за {l}$"
            else:
                l = randint(1, 1000000)
                await imus(user_id=lol, lyl="нет")
                await mani_ig(user_id=lol, mani=l)
                return f"Вы продали {im} за {l}$"


@bl.message(text="магазин недвижимость")
async def greeting(message: Message):
    lol = message.from_id
    text = """
1) Незавершенное строительство -> 5000000$
2) Зданиe -> 9000000$
3) Однушка в Москве -> 90000000$
4) Двушка в Москве -> 10000000$
5) Трешка в Москве -> 150000000$
6) Студия в Москве -> 80000000$
7) Однушка в Санкт-Петербурге -> 80000000$
8) Двушка в Санкт-Петербурге -> 10000000$
9) Трешка в Санкт-Петербурге -> 120000000$
10) Студия в Санкт -Петербурге -> 60000000$
11) Однушка в Сочи -> 70000000$
12) Двушка в Сочи -> 90000000$
13) Трешка в Сочи -> 130000000$
14) Студия в Сочи -> 95000000$
15) Однушка в Филадельфии (Крым) -> 60000000$
16) Двушка в Филадельфии (Крым) -> 90000000$
17) Трешка в Филадельфии (Крым) -> 130000000$
18) Студия в Филадельфии (Крым) -> 50000000$
19) Однушка на мальдивах -> 100000000$
20) Двушка на мальдивах -> 200000000$
21) Трешка на мальдивах -> 300000000$
22) Студия на мальдивах -> 90000000$

Команда: Купить недвижимость {номер недвижимости} 
    """

    return text


async def imus_ned(user_id, lyl):
    user_db = await User.get(id=user_id)
    user_db.house = lyl
    await user_db.save()


@bl.message(
    text="купить недвижимость <transport>")
async def greeting(message: Message, transport: str):
    lol = message.from_id
    user_db = await User.get(id=lol)
    if 1 == 1:
        im = user_db.house
        if str(im) == "нет" or im == None:
            lel = user_db.balance
            if str(transport) == "1":

                if float(lel) >= 5000000:
                    kek = "Незавершенное строительство"
                    await imus_ned(user_id=lol, lyl=kek)
                    await manii_ig(user_id=lol, mani=5000000)

                    return f'Вы приобрели {kek}'
                else:
                    kek = "Незавершенное строительство"
                    s = 5000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'


            elif str(transport) == "2":
                '2) Зданиe -> 9000000$'

                if float(lel) >= 9000000:
                    kek = "Зданиe"
                    await imus_ned(user_id=lol, lyl="Зданиe")
                    await manii_ig(user_id=lol, mani=9000000)

                    return f'Вы приобрели {kek}'
                else:
                    kek = "Зданиe"
                    s = 9000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'
            elif str(transport) == "3":
                '3) Однушка в Москве -> 90000000$'
                kek = "Однушка в Москве"
                if float(lel) >= 90000000:
                    await imus_ned(user_id=lol, lyl="Однушка в Москве")
                    await manii_ig(user_id=lol, mani=90000000)
                    kek = "Однушка в Москве"
                    return f'Вы приобрели {kek}'
                else:
                    s = 90000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'
            elif str(transport) == "4":
                '4) Двушка в Москве -> 10000000$'

                if float(lel) >= 10000000:
                    await imus_ned(user_id=lol, lyl="Двушка в Москве")
                    await manii_ig(user_id=lol, mani=10000000)
                    kek = "Двушка в Москве"
                    return f'Вы приобрели {kek}'
                else:
                    kek = "Двушка в Москве"

                    s = 10000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'
            elif str(transport) == "5":
                '5) Трешка в Москве -> 150000000$'

                if float(lel) >= 150000000:
                    await imus_ned(user_id=lol, lyl="Трешка в Москве")
                    await manii_ig(user_id=lol, mani=150000000)
                    kek = "Трешка в Москве"
                    return f'Вы приобрели {kek}'
                else:
                    kek = "Трешка в Москве"

                    s = 150000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'
            elif str(transport) == "6":
                '6) Студия в Москве -> 80000000$'

                if float(lel) >= 80000000:
                    await imus_ned(user_id=lol, lyl="Студия в Москве")
                    await manii_ig(user_id=lol, mani=80000000)
                    kek = "Студия в Москве"
                    return f'Вы приобрели {kek}'
                else:
                    kek = "Студия в Москве"

                    s = 80000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'
            elif str(transport) == "7":
                '7) Однушка в Санкт-Петербурге -> 80000000$'

                if float(lel) >= 80000000:
                    await imus_ned(user_id=lol, lyl="Однушка в Санкт-Петербурге")
                    await manii_ig(user_id=lol, mani=80000000)
                    kek = "Однушка в Санкт-Петербурге"
                    return f'Вы приобрели {kek}'
                else:
                    kek = "Однушка в Санкт-Петербурге"

                    s = 80000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'
            elif str(transport) == "8":
                '8) Двушка в Санкт-Петербурге -> 10000000$'

                if float(lel) >= 10000000:
                    await imus_ned(user_id=lol, lyl="Двушка в Санкт-Петербурге")
                    await manii_ig(user_id=lol, mani=10000000)
                    kek = "Двушка в Санкт-Петербурге"
                    return f'Вы приобрели {kek}'
                else:
                    kek = "Двушка в Санкт-Петербурге"

                    s = 10000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'
            elif str(transport) == "9":
                '9) Трешка в Санкт-Петербурге -> 120000000$'

                if float(lel) >= 120000000:
                    await imus_ned(user_id=lol, lyl="Трешка в Санкт-Петербурге")
                    await manii_ig(user_id=lol, mani=120000000)
                    kek = "Трешка в Санкт-Петербурге"
                    return f'Вы приобрели {kek}'
                else:
                    kek = "Трешка в Санкт-Петербурге"

                    s = 120000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'
            elif str(transport) == "10":
                '10) Студия в Санкт-Петербурге -> 60000000$'

                if float(lel) >= 60000000:
                    await imus_ned(user_id=lol, lyl="Студия в Санкт-Петербурге")
                    await manii_ig(user_id=lol, mani=60000000)
                    kek = "Студия в Санкт-Петербурге"
                    return f'Вы приобрели {kek}'
                else:
                    kek = "Студия в Санкт-Петербурге"

                    s = 60000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'
            elif str(transport) == "11":

                if float(lel) >= 70000000:
                    await imus_ned(user_id=lol, lyl="Однушка в Сочи")
                    await manii_ig(user_id=lol, mani=70000000)
                    kek = "Однушка в Сочи"
                    return f'Вы приобрели {kek}'
                else:
                    kek = "Однушка в Сочи"

                    s = 70000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'
            elif str(transport) == "12":

                if float(lel) >= 90000000:
                    await imus_ned(user_id=lol, lyl="Двушка в Сочи")
                    await manii_ig(user_id=lol, mani=90000000)
                    kek = "Двушка в Сочи"
                    return f'Вы приобрели {kek}'
                else:
                    kek = "Двушка в Сочи"

                    s = 90000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'
            elif str(transport) == "13":

                if float(lel) >= 130000000:
                    await imus_ned(user_id=lol, lyl="Трешка в Сочи")
                    await manii_ig(user_id=lol, mani=130000000)
                    kek = "Трешка в Сочи"
                    return f'Вы приобрели {kek}'
                else:
                    kek = "Трешка в Сочи"

                    s = 130000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'
            elif str(transport) == "14":

                if float(lel) >= 95000000:
                    await imus_ned(user_id=lol, lyl="Студия в Сочи")
                    await manii_ig(user_id=lol, mani=95000000)
                    kek = "Студия в Сочи"
                    return f'Вы приобрели {kek}'
                else:
                    kek = "Студия в Сочи"

                    s = 95000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'
            elif str(transport) == "15":

                if float(lel) >= 60000000:
                    await imus_ned(user_id=lol, lyl="Однушка в Филадельфии (Крым)")
                    await manii_ig(user_id=lol, mani=60000000)
                    kek = "Однушка в Филадельфии (Крым)"
                    return f'Вы приобрели {kek}'
                else:
                    kek = "Однушка в Филадельфии (Крым)"

                    s = 60000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'
            elif str(transport) == "16":
                if float(lel) >= 90000000:
                    await imus_ned(user_id=lol, lyl="Двушка в Филадельфии (Крым)")
                    await manii_ig(user_id=lol, mani=90000000)
                    kek = "Двушка в Филадельфии (Крым)"
                    return f'Вы приобрели {kek}'
                else:
                    kek = "Двушка в Филадельфии (Крым)"

                    s = 90000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'
            elif str(transport) == "17":

                if float(lel) >= 130000000:
                    await imus_ned(user_id=lol, lyl="Трешка в Филадельфии (Крым)")
                    await manii_ig(user_id=lol, mani=130000000)
                    kek = "Трешка в Филадельфии (Крым)"
                    return f'Вы приобрели {kek}'
                else:
                    kek = "Трешка в Филадельфии (Крым)"

                    s = 130000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'
            elif str(transport) == "18":
                if float(lel) >= 50000000:
                    await imus_ned(user_id=lol, lyl="Студия в Филадельфии (Крым)")
                    await manii_ig(user_id=lol, mani=50000000)
                    kek = "Студия в Филадельфии (Крым)"
                    return f'Вы приобрели {kek}'
                else:
                    kek = "Студия в Филадельфии (Крым)"

                    s = 50000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'
            elif str(transport) == "19":
                if float(lel) >= 100000000:
                    await imus_ned(user_id=lol, lyl="Однушка на мальдивах")
                    await manii_ig(user_id=lol, mani=100000000)
                    kek = "Однушка на мальдивах"
                    return f'Вы приобрели {kek}'
                else:
                    kek = "Однушка на мальдивах"

                    s = 100000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'
            elif str(transport) == "20":

                if float(lel) >= 200000000:
                    await imus_ned(user_id=lol, lyl="Двушка на мальдивах")
                    await manii_ig(user_id=lol, mani=200000000)
                    kek = "Двушка на мальдивах"
                    return f'Вы приобрели {kek}'
                else:
                    kek = "Двушка на мальдивах"

                    s = 200000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'
            elif str(transport) == "21":

                if float(lel) >= 300000000:
                    await imus_ned(user_id=lol, lyl="Трешка на мальдивах")
                    await manii_ig(user_id=lol, mani=300000000)
                    kek = "Трешка на мальдивах"
                    return f'Вы приобрели {kek}'
                else:
                    kek = "Трешка на мальдивах"

                    s = 300000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'
            elif str(transport) == "22":
                if float(lel) >= 90000000:
                    await imus_ned(user_id=lol, lyl="Студия на мальдивах")
                    await manii_ig(user_id=lol, mani=90000000)
                    kek = "Студия на мальдивах"
                    return f'Вы приобрели {kek}'
                else:
                    kek = "Студия на мальдивах"

                    s = 90000000 - lel
                    return f'На покупку "{kek}" вам не хватает {s}$'

            else:
                return "Нету такого номера"
        else:

            return f'Сначала надо избавиться от "{im}"\nКоманда: Продать недвижимость'


@bl.message(text="продать Недвижимость")
async def greeting(message: Message):
    lol = message.from_id
    user_db = await User.get(id=lol)
    if 1 == 1:
        im = user_db.house
        if str(im) == "нет" or im == None:
            return "Вам нечего продавать"
        else:
            await imus_ned(user_id=lol, lyl="нет")
            l = randint(1, 5000000)
            await mani_ig(user_id=lol, mani=l)
            return f"Вы продали {im} за {l}$"
