import time
from random import randint

from vkbottle.bot import BotLabeler, Message

from models import User
from utils import get_forward, biznes_up, biznes_sn

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text=['бизнесы', "магазин бизнесы"])
async def greeting(message: Message):
    text = """
1) Сад - 250.000$ | 2.000$ в час
2) Шахта - 600.000$ | 6.000$ в час
3) Закусочная - 1.500.000$ | 12.500$ в час
4) Магазин - 5.000.000$ | 40.000$ в час
5) Мотель - 30.000.000$ | 250.000$ в час
6) Стрип-клуб - 200.000.000$ | 1.100.000$ в час
7) Офис - 500.000.000$ | 2.500.000$ в час
8) Киностудия - 3.500.000.000$ | 17.500.000$ в час
9) Завод - 10.000.000.000$ | 45.000.000$ в час
10) Нефтевышка - 30.000.000.000$ | 150.000.000$ в час
11) АЭС - 100.000.000.000$ | 500.000.000$ в час
Чтобы приобрести бизнес введите команду:
Купить бизнес {номер бизнеса}
    """
    return text


@bl.message(text='купить бизнес <a:int>')
async def greeting(message: Message, a: int):
    user_db = await User.get(id=message.from_id)

    im = user_db.business
    lel = user_db.balance
    biznes = [
        'Сад',
        'Шахта',
        'Закусочная',
        'Магазин',
        'Мотель',
        'Стрип-клуб',
        'Офис',
        'Киностудия',
        'Завод',
        'Нефтевышка',
        'АЭС',
    ]
    ##СТОЙМОСТЬ
    cost = [
        250000,
        600000,
        1500000,
        5000000,
        30000000,
        200000000,
        500000000,
        3500000000,
        10000000000,
        30000000000,
        100000000000,
    ]
    if str(im) == "нет" or im == None:
        index = a - 1
        if a >= 1 and a <= 11:

            if float(lel) >= cost[index]:
                user_db.business = biznes[index]
                user_db.balance = lel - cost[index]
                user_db.biz_time = time.time()
                await user_db.save()
                text = f'Вы приобрели "{biznes[index]}"'
                await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
                return
            else:
                s = cost[index] - lel
                text = f'На покупку "{biznes[index]}" вам не хватает {s}$'
                await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
                return
        else:
            text = "Нет такого бизнеса"
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return
    else:
        text = f'Сначала надо избавиться от "{im}"\nКоманда: продать бизнес'
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return


@bl.message(text="продать бизнес")
async def greeting(message: Message):
    lol = message.from_id
    user_db = await User.get(id=lol)
    if 1 == 1:
        im = user_db.business

        biznes = [
            'Сад',
            'Плантация',
            'Ферма',
            'Шахта',
            'Рудник',
            'Карьер',
            'Закусочная',
            'Столовая',
            'Кафе',
            'Магазин',
            'ТЦ',
            "ТЦ ",
            'ЦУМ',
            'Мотель',
            'Отель',
            '5-ти звёздочный отель',
            'Стрип-клуб',
            'Бордель',
            'Офис',
            'Страховой офис',
            'Офис продаж',
            'Отдел биржевых операций',
            'Киностудия',
            'Кинокомпания',
            'Завод',
            'Крупный завод',
            'Фабрика',
            'Нефтевышка',
            'Нефтеплатформа',
            'Нефтехимическая промышленность',
            'АЭС',
            'Крупная АЭС',
            'Производство ядерного оружия'
        ]
        ##СТОЙМОСТЬ
        cost = [
            15000,
            250000,
            400000,
            600000,
            800000,
            1000000,
            1500000,
            2000000,
            3000000,
            3000000,
            5000000,
            10000000,
            20000000,
            30000000,
            50000000,
            100000000,
            200000000,
            300000000,
            500000000,
            750000000,
            1000000000,
            2000000000,
            3500000000,
            6000000000,
            10000000000,
            15000000000,
            25000000000,
            30000000000,
            40000000000,
            60000000000,
            100000000000,
            200000000000,
            400000000000
        ]
        if str(im) == "нет" or im == None:
            return "У вас нет бизнеса"
        else:
            index = biznes.index(im)
            costMax = cost[index]
            wls = randint(1, costMax)
            user_db.business = "нет"
            user_db.balance += wls
            await user_db.save()

            return f"Вы продали {im} за {wls}$"


@bl.message(text='бизнес улучшить')
async def greeting(message: Message):
    user_db = await User.get(id=message.from_id)
    s = user_db.business
    if user_db.business == None or user_db.business == "нет":
        return "Вам нечего улучшать"
    elif user_db.business == "Сад":
        a = 250000
        b = "Плантация"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Плантация":
        a = 400000
        b = "Ферма"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Шахта":
        a = 800000
        b = "Рудник"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Рудник":
        a = 1000000
        b = "Карьер"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Закусочная":
        a = 2000000
        b = "Столовая"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Столовая":
        a = 3000000
        b = "Кафе"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Магазин":
        a = 10000000
        b = "ТЦ"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "ТЦ":
        a = 20000000
        b = "ЦУМ"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Мотель":
        a = 50000000
        b = "Отель"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Отель":
        a = 100000000
        b = "5-ти звёздочный отель"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Стрип-клуб":
        a = 300000000
        b = "Бордель"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Страховой офис":
        a = 24000000
        b = "Офис продаж"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Офис":
        a = 750000000
        b = "Страховой офис"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Страховой офис":
        a = 1000000000
        b = "Офис продаж"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Офис продаж":
        a = 2000000000
        b = "Отдел биржевых операций"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Киностудия":
        a = 6000000000
        b = "Кинокомпания"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Завод":
        a = 15000000000
        b = "Крупный завод"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Крупный завод":
        a = 25000000000
        b = "Фабрика"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Нефтевышка":
        a = 40000000000
        b = "Нефтеплатформа"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Нефтеплатформа":
        a = 60000000000
        b = "Нефтехимическая промышленность"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "АЭС":
        a = 200000000000
        b = "Крупная АЭС"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Крупная АЭС":
        a = 400000000000
        b = "Производство ядерного оружия"
        text = await biznes_up(message.from_id, a, b, s)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    else:
        return "Ваш бизнес улучшен максимально"


@bl.message(text='бизнес снять все')
async def greeting(message: Message):
    lol = message.from_id
    user_db = await User.get(id=lol)
    if user_db.business == None or user_db.business == "нет":
        return "У вас нет бизнеса"
    elif user_db.business == "Сад":
        minim = 1000
        maxim = 2000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Плантация":
        minim = 2000
        maxim = 3000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Ферма":
        minim = 4000
        maxim = 5000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return

    elif user_db.business == "Шахта":
        minim = 5000
        maxim = 6000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Рудник":
        minim = 7000
        maxim = 8000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Карьер":
        minim = 9000
        maxim = 10000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Столовая":
        minim = 17000
        maxim = 17500
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Закусочная":
        minim = 12000
        maxim = 12500
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Кафе":
        minim = 23000
        maxim = 25000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return

    elif user_db.business == "Магазин":
        minim = 35000
        maxim = 40000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "ТЦ":
        minim = 75000
        maxim = 80000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return

    elif user_db.business == "ЦУМ":
        minim = 140000
        maxim = 150000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return

    elif user_db.business == "Мотель":
        minim = 240000
        maxim = 250000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return

    elif user_db.business == "Отель":
        minim = 340000
        maxim = 350000
        ttt = time.time()
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return

    elif user_db.business == "5-ти звёздочный отель":
        minim = 550000
        maxim = 600000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Стрип-клуб":
        minim = 1000000
        maxim = 1100000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Бордель":
        minim = 1400000
        maxim = 1500000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Офис":
        minim = 2400000
        maxim = 2500000
        ttt = time.time()
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Страховой офис":
        minim = 3400000
        maxim = 3500000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Офис продаж":
        minim = 4500000
        maxim = 5000000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Отдел биржевых операций":
        minim = 8500000
        maxim = 9000000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Киностудия":
        minim = 17000000
        maxim = 17500000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Кинокомпания":
        minim = 25000000
        maxim = 27000000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Завод":
        minim = 40000000
        maxim = 45000000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Крупный завод":
        minim = 67000000
        maxim = 67500000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Фабрика":
        minim = 120000000
        maxim = 125000000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Нефтевышка":
        minim = 150000000
        maxim = 155000000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Нефтеплатформа":
        minim = 180000000
        maxim = 185000000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Нефтехимическая промышленность":
        minim = 250000000
        maxim = 255000000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "АЭС":
        minim = 500000000
        maxim = 550000000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Крупная АЭС":
        minim = 800000000
        maxim = 810000000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif user_db.business == "Производство ядерного оружия":
        minim = 2000000000
        maxim = 2000000000
        text = await biznes_sn(message.from_id, minim, maxim)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
