import time
from random import randint
from time import gmtime
from time import strftime

from vkbottle.bot import BotLabeler, Message

from models import User
from utils import get_forward

bl = BotLabeler()

bl.vbml_ignore_case = True


@bl.message(text=["нанять", "Нанять"])
async def vakansi(message: Message):
    db_user = await User.get(id=message.from_id)
    db_use = await User.get(id=message.reply_message.from_id)
    if db_user.rank >= 6:
        try:
            db_use.work = 'Проститутка Лютика'
            await db_use.save()
            return "Теперь ты проститутка Лютика"
        except:
            return "Что-то пошло не так, скорее всего её нет в бд."


@bl.message(text="уволить")
async def vakansi(message: Message):
    db_user = await User.get(id=message.from_id)
    db_use = await User.get(id=message.reply_message.from_id)
    if db_user.rank >= 6:
        try:
            db_use.work = 'нет'
            await db_use.save()
            return "Теперь ты безработная шалава"
        except:
            return "Что-то пошло не так, скорее всего её нет в бд."


@bl.message(text=["нанять [id<vk_user_id:int>|<other>", "Нанять [id<vk_user_id:int>|<other>"])
async def vakansi(message: Message, vk_user_id: int, **kwargs):
    db_user = await User.get(id=message.from_id)
    db_use = await User.get(id=vk_user_id)
    if db_user.rank >= 6:
        try:
            db_use.work = 'Проститутка Лютика'
            await db_use.save()
            return "Теперь ты проститутка Лютика"
        except:
            return "Что-то пошло не так, скорее всего её нет в бд."


async def ferma(opt, user_id, mani, time):
    db_user = await User.get(id=user_id)
    optt = db_user.experience
    opt_t = int(optt) + int(opt)
    ma = db_user.balance
    ly = int(ma) + int(mani)
    db_user.experience = opt_t
    db_user.balance = ly
    if db_user.house == None or db_user.house == "нет":
        ttt = time
    else:
        ttt = time - randint(1, 1000)
    db_user.farm_time = ttt
    await db_user.save()


async def vorking(message: Message, ma, l, a):
    db_user = await User.get(id=message.from_id)
    if (time.time() - int(ma)) >= 3600:

        await ferma(user_id=message.from_id, opt=l, mani=a, time=time.time())

        opt = db_user.experience
        if int(opt) >= 1000:
            return f"Отработал, за работу получил {l} опыта и {a}$\nТак же, вам доступны работы работы более высокого урованя\nКоманда: Вакансии"
        return f"Отработал, за работу получил {l} опыта и {a}$"
    else:
        l = db_user.farm_time + 3600
        s = l - time.time()
        t = strftime("%M:%S", gmtime(s))
        return f'Ты слишком устал, отдохни еще {t}'


@bl.message(text=["работать", "Работать"])
async def greeting(message: Message):
    lol = message.from_id
    if 1 == 1:
        db_user = await User.get(id=message.from_id)
        ma = db_user.farm_time
        rab = db_user.work
        s = time.time()

        if str(rab) == "нет":
            return 'Ты нигде не работаешь\nЧто бы устроиться на работу напиши "Вакансии"'
        elif str(rab) == "Уборщик":
            l = randint(30, 60)
            a = randint(10000, 15000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return

        elif str(rab) == "Посудомойщик":

            l = randint(40, 70)
            a = randint(15000, 18000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return


        elif str(rab) == "Таксист":

            l = randint(50, 80)
            a = randint(20000, 25000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return
        elif str(rab) == "Переводчик":

            l = randint(50, 80)
            a = randint(20000, 25000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return

        elif str(rab) == "Психотерапевт":

            l = randint(50, 90)
            a = randint(20000, 28000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return

        elif str(rab) == "Кладовщик":

            l = randint(60, 100)
            a = randint(27000, 32000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return

        elif str(rab) == "Каменщик":

            l = randint(60, 100)
            a = randint(30000, 35000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return
        elif str(rab) == "Фотограф":

            l = randint(60, 100)
            a = randint(37000, 40000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return
        elif str(rab) == "Журналист":

            l = randint(60, 100)
            a = randint(40000, 45000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return
        elif str(rab) == "Стоматолог":

            l = randint(60, 100)
            a = randint(45000, 50000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return

        elif str(rab) == "Повар":

            l = randint(60, 100)
            a = randint(55000, 60000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return

        elif str(rab) == "Инженер":

            l = randint(60, 100)
            a = randint(58000, 60000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return

        elif str(rab) == "Спасатель":

            l = randint(60, 100)
            a = randint(65000, 67000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return

        elif str(rab) == "Географ":

            l = randint(60, 100)
            a = randint(72000, 75000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return

        elif str(rab) == "Врач":

            l = randint(60, 100)
            a = randint(76000, 83000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return

        elif str(rab) == "Сценарист":

            l = randint(60, 100)
            a = randint(85000, 90000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return

        elif str(rab) == "Видеооператор":

            l = randint(60, 100)
            a = randint(90000, 100000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return

        elif str(rab) == "Химик":

            l = randint(60, 100)
            a = randint(100000, 110000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return

        elif str(rab) == "Археолог":

            l = randint(60, 100)
            a = randint(110000, 120000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return
        elif str(rab) == "Прораб":

            l = randint(60, 100)
            a = randint(120000, 125000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return
        elif str(rab) == "Риелтор":

            l = randint(60, 100)
            a = randint(130000, 132000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return
        elif str(rab) == "Банкир":

            l = randint(60, 100)
            a = randint(135000, 140000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return
        elif str(rab) == "Нефтяник":

            l = randint(60, 100)
            a = randint(145000, 150000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return
        elif str(rab) == "Авиатор":

            l = randint(60, 100)
            a = randint(155000, 160000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return
        elif str(rab) == "Брокер":

            l = randint(60, 100)
            a = randint(170000, 175000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return
        elif str(rab) == "Программист":

            l = randint(60, 100)
            a = randint(180000, 190000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return
        elif str(rab) == "Экономист":

            l = randint(60, 100)
            a = randint(190000, 200000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return
        elif str(rab) == "Судья":

            l = randint(60, 100)
            a = randint(210000, 215000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return
        elif str(rab) == "Дипломат":

            l = randint(60, 100)
            a = randint(200000, 230000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return
        elif str(rab) == "Прокурор":

            l = randint(60, 100)
            a = randint(230000, 250000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return
        elif str(rab) == "Проститутка Лютика":

            l = randint(500, 900)
            a = randint(1000000, 1000000000)
            text = await vorking(message=message, ma=ma, a=a, l=l)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return


@bl.message(text=["Вакансии", "вакансии"])
async def vakansii(message: Message):
    user_db = await User.get(id=message.from_id)
    text = ""
    if user_db.experience >= 60000:
        text += "Прокурор -> 250000\n"
    if user_db.experience >= 58000:
        text += "Дипломат -> 230000\n"
    if user_db.experience >= 56000:
        text += "Судья -> 215000\n"
    if user_db.experience >= 54000:
        text += "Экономист -> 200000\n"
    if user_db.experience >= 52000:
        text += "Программист -> 190000\n"
    if user_db.experience >= 50000:
        text += "Брокер -> 175000\n"
    if user_db.experience >= 48000:
        text += "Авиатор -> 160000\n"
    if user_db.experience >= 46000:
        text += "Нефтяник -> 150000\n"
    if user_db.experience >= 44000:
        text += "Банкир -> 140000\n"
    if user_db.experience >= 42000:
        text += "Риелтор -> 132000\n"
    if user_db.experience >= 40000:
        text += "Прораб -> 125000\n"
    if user_db.experience >= 38000:
        text += "Археолог -> 120000\n"
    if user_db.experience >= 36000:
        text += "Химик -> 110000\n"
    if user_db.experience >= 34000:
        text += "Видеооператор -> 100000\n"
    if user_db.experience >= 32000:
        text += "Сценарист -> 90000\n"
    if user_db.experience >= 30000:
        text += "Врач -> 83000\n"
    if user_db.experience >= 28000:
        text += "Географ -> 75000\n"
    if user_db.experience >= 26000:
        text += "Спасатель -> 67000\n"
    if user_db.experience >= 24000:
        text += "Инженер -> 60000\n"
    if user_db.experience >= 22000:
        text += "Повар -> 55000\n"
    if user_db.experience >= 20000:
        text += "Стоматолог -> 50000\n"
    if user_db.experience >= 18000:
        text += "Журналист -> 45000\n"
    if user_db.experience >= 16000:
        text += "Фотограф -> 40000\n"
    if user_db.experience >= 14000:
        text += "Каменщик -> 35000\n"
    if user_db.experience >= 12000:
        text += "Кладовщик -> 32000\n"
    if user_db.experience >= 8000:
        text += "Психотерапевт -> 28000\n"
    if user_db.experience >= 6000:
        text += "Переводчик -> 25000\n"
    if user_db.experience >= 3000:
        text += "Таксист -> 20000\n"
    if user_db.experience >= 1000:
        text += "Посудомойщик -> 18000\n"
    if user_db.experience >= 0:
        text += "Уборщик -> 15000"

    return text


@bl.message(text=["Вакансия <rab>", "вакансия <rab>"])
async def vakansi(message: Message, rab: str):
    lol = message.from_id
    db_user = await User.get(id=lol)
    if 1 == 1:
        rabot1 = db_user.work
        if rabot1 == None:
            rabot = "нет"
        else:
            rabot = db_user.work
        if str(rabot) == "нет":

            if str(rab) == "Уборщик" or str(rab) == "уборщик":
                opt = db_user.experience
                if int(opt) >= 0:
                    a = "Уборщик"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Уборщик"'
            elif str(rab) == "Посудомойщик" or str(rab) == "посудомойщик":
                opt = db_user.experience
                if int(opt) >= 1000:
                    a = "Посудомойщик"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Посудомойщик"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Таксист" or str(rab) == "таксист":
                opt = db_user.experience
                if int(opt) >= 3000:
                    a = "Таксист"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Таксист"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Переводчик" or str(rab) == "переводчик":
                opt = db_user.experience
                if int(opt) >= 6000:
                    a = "Переводчик"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Переводчик"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Психотерапевт" or str(rab) == "психотерапевт":
                opt = db_user.experience
                if int(opt) >= 8000:
                    a = "Психотерапевт"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Психотерапевт"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Кладовщик" or str(rab) == "кладовщик":
                opt = db_user.experience
                if int(opt) >= 12000:
                    a = "Кладовщик"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Кладовщик"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Каменщик" or str(rab) == "каменщик":
                opt = db_user.experience
                if int(opt) >= 14000:
                    a = "Каменщик"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Каменщик"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Фотограф" or str(rab) == "фотограф":
                opt = db_user.experience
                if int(opt) >= 16000:
                    a = "Фотограф"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Фотограф"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Журналист" or str(rab) == "журналист":
                opt = db_user.experience
                if int(opt) >= 18000:
                    a = "Журналист"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Журналист"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Стоматолог" or str(rab) == "стоматолог":
                opt = db_user.experience
                if int(opt) >= 20000:
                    a = "Стоматолог"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Стоматолог"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Повар" or str(rab) == "повар":
                opt = db_user.experience
                if int(opt) >= 22000:
                    a = "Повар"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Повар"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Инженер" or str(rab) == "инженер":
                opt = db_user.experience
                if int(opt) >= 24000:
                    a = "Инженер"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Инженер"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Спасатель" or str(rab) == "спасатель":
                opt = db_user.experience
                if int(opt) >= 26000:
                    a = "Спасатель"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Спасатель"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Географ" or str(rab) == "географ":
                opt = db_user.experience
                if int(opt) >= 28000:
                    a = "Географ"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Географ"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Врач" or str(rab) == "врач":
                opt = db_user.experience
                if int(opt) >= 30000:
                    a = "Врач"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Врач"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Сценарист" or str(rab) == "сценарист":
                opt = db_user.experience
                if int(opt) >= 32000:
                    a = "Сценарист"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Сценарист"'
                else:
                    return "У вас не хватает опыта для этой работы"

            elif str(rab) == "Видеооператор" or str(rab) == "видеооператор":
                opt = db_user.experience
                if int(opt) >= 34000:
                    a = "Видеооператор"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Видеооператор"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Химик" or str(rab) == "химик":
                opt = db_user.experience
                if int(opt) >= 36000:
                    a = "Химик"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Химик"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Археолог" or str(rab) == "археолог":
                opt = db_user.experience
                if int(opt) >= 38000:
                    a = "Археолог"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Археолог"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Прораб" or str(rab) == "прораб":
                opt = db_user.experience
                if int(opt) >= 40000:
                    a = "Прораб"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Прораб"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Риелтор" or str(rab) == "риелтор":
                opt = db_user.experience
                if int(opt) >= 42000:
                    a = "Риелтор"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "Риелтор"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Банкир" or str(rab) == "банкир":
                opt = db_user.experience
                if int(opt) >= 44000:
                    a = "Банкир"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "{a}"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Нефтяник" or str(rab) == "нефтяник":
                opt = db_user.experience
                if int(opt) >= 46000:
                    a = "Нефтяник"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "{a}"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Авиатор" or str(rab) == "авиатор":
                opt = db_user.experience
                if int(opt) >= 48000:
                    a = "Авиатор"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "{a}"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Брокер" or str(rab) == "брокер":
                opt = db_user.experience
                if int(opt) >= 50000:
                    a = "Брокер"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "{a}"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Программист" or str(rab) == "программист":
                opt = db_user.experience
                if int(opt) >= 52000:
                    a = "Программист"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "{a}"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Экономист" or str(rab) == "экономист":
                opt = db_user.experience
                if int(opt) >= 54000:
                    a = "Экономист"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "{a}"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Судья" or str(rab) == "судья":
                opt = db_user.experience
                if int(opt) >= 56000:
                    a = "Судья"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "{a}"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Дипломат" or str(rab) == "дипломат":
                opt = db_user.experience
                if int(opt) >= 58000:
                    a = "Дипломат"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "{a}"'
                else:
                    return "У вас не хватает опыта для этой работы"
            elif str(rab) == "Прокурор" or str(rab) == "прокурор":
                opt = db_user.experience
                if int(opt) >= 60000:
                    a = "Прокурор"
                    db_user.work = a
                    await db_user.save()
                    return f'Вы устроились на работу "{a}"'
                else:
                    return "У вас не хватает опыта для этой работы"
        else:
            return "Тебе надо уволиться, с предыдущего места работы"


@bl.message(text=["Уволиться", "уволиться"])
async def vakansi(message: Message):
    if 1 == 1:
        db_user = await User.get(id=message.from_id)
        rabot = db_user.work
        if not str(rabot) == "нет":
            db_user.work = 'нет'
            await db_user.save()
            return f'Вы уволились с работы "{rabot}"'
        else:
            return "Ты нигде не работал"


@bl.message(text=["работа", "Работа"])
async def vakansi(message: Message):
    db_user = await User.get(id=message.from_id)
    if 1 == 1:
        rabot1 = db_user.work
        if rabot1 == None:
            rabot = 'нет'
        else:
            rabot = db_user.work
        if not str(rabot) == "нет":

            return f'Вы работаете "{rabot}"'
        else:
            return "Вы нигде не работаете"
