from pyqiwip2p import QiwiP2P
from vkbottle.bot import BotLabeler, Message
from config import QIWI_PRIV_KEY
from utils import get_forward, get_nikname
from models import User
from config import main_token
import vk_api
bl = BotLabeler()
bl.vbml_ignore_case = True

@bl.message(text=["Магазин", "магазин"])
async def magaz(message: Message):
    text = """
Машины
Недвижимость
Бизнесы
Компьютеры
Самолёты
Вертолёты
Телефоны

Купить вип

"""
    return text


async def rang(yr, users, ma):
    try:
        user_db = await User.get(id=users)
        user_db.rank = yr
        a = user_db.money
        s = int(a) - int(ma)
        user_db.money = s
        await user_db.save()
        return "OK"
    except:
        return "Error"


@bl.message(text=["Купить вип", "купить вип", "Купить Вип", "купить Вип"])
async def greceting(message: Message):
    user_db = await User.get(id=message.from_id)
    if user_db.rank >= 1:
        return "У вас уже VIP доступ"
    else:
        p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY, default_amount=148)
        new_bill = p2p.bill(amount=50, lifetime=120, comment=f"VIP{message.from_id}")
        s = (new_bill.pay_url)
        vk = vk_api.VkApi(token=main_token)
        nikk = await get_nikname(m=message, user_id=message.from_id)
        q = vk.method("utils.getShortLink", {"url": s, "private": 0})["short_url"]
        text = f"Ссылка строго для {nikk} и будет действительна 2 часа.\nВип выдастся автоматически после оплаты\n\n{q}"
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return

async def zvd_v(user_id, mani, manii):
    users = await User.get(id=user_id)
    ma = users.reputation_to_give
    lyl = int(ma) + int(mani)
    a = users.money
    s = int(a) - int(manii)
    users.money = s
    users.reputation_to_give = lyl
    await users.save()
"""

@bl.message(
    text=["Купить звезды <a>", "купить звезды <a>", "Купить Звезды <a>", "купить Звезды <a>", "Купить звёзды <a>",
          "купить звёзды <a>", "Купить Звёзды <a>", "купить Звёзды <a>"])
async def reting(message: Message, a: int):
    if int(a) < 0 or int(a) == 0:
        return
    user_db = await User.get(id=message.from_id)
    mani = user_db.money

    if 1 == 1:
        l = int(a) * 2
        if int(l) == int(mani):

            await zvd_v(user_id=message.from_id, mani=a, manii=l)
            return "Вы приобрели " + str(a) + " звезд"
        elif int(l) < int(mani):
            await zvd_v(user_id=message.from_id, mani=a, manii=l)
            return "Вы приобрели " + str(a) + " звезд"
        else:
            n = int(l) - int(mani)
            return "Вам не хватает " + str(n) + " ананасиков"


@bl.message(text=["Купить доллары <a>", "купить Доллары <a>", "Купить Доллары <a>", "купить доллары <a>"])
async def greetlsing(message: Message, a: int):
    if int(a) < 0 or int(a) == 0:
        return
    user_db = await User.get(id=message.from_id)

    mani = user_db.money

    if 1 == 1:
        l = int(a) * 50000
        if int(a) == int(mani):
            v = mani - int(a)
            user_db.money = v
            bal = user_db.balance
            itog = bal + int(l)
            user_db.balance = itog
            await user_db.save()
            return "Вы приобрели " + str(l) + " долларов"
        elif int(a) < int(mani):
            v = mani - int(a)
            user_db.money = v
            bal = user_db.balance
            itog = bal + int(l)
            user_db.balance = itog
            await user_db.save()
            return "Вы приобрели " + str(l) + " долларов"
        else:
            n = int(a) - int(mani)
            return "Вам не хватает " + str(n) + " ананасиков"


@bl.message(text="подарить пак")
async def greceting(message: Message):
    user1 = await User.get(id=message.from_id)
    if user1.rank >= 66:
        user_db = await User.get(id=message.reply_message.from_id)
        user_db.stic += 150
        rand = user_db.stic

        await user_db.save()
        user = message.reply_message.from_id
        msg = f"Для @id{user} От ЛадноБота"
        r = requests.post(
            f'https://api.vk.com/method/gifts.send?guid={rand}&gift_id=10001&v=5.131&user_ids={user}&message={msg}&confirm=1&access_token={token}')
        ww = requests.post(
            f'https://api.vk.com/method/gifts.send?guid={rand}&gift_id=10001&v=5.131&user_ids={user}&message={msg}&confirm=1&access_token={token}')

        print(r.content)
        print(ww.content)
        return f"Получил стикерпак от разработчика"


@bl.message(text="рулетка")
async def greceting(message: Message):
    user_db = await User.get(id=message.from_id)
    if user_db.rank >= 6:
        mani = user_db.money
        if mani >= 20:
            maa = int(mani) - 20
            user_db.money = maa
            await user_db.save()
            a = randint(1, 6)
            if a == 1:
                s = randint(100, 1000)
                user_db.experience += s

                await user_db.save()
                return f'Выйграл {s} опыта'

            elif a == 2:
                if user_db.rank >= 1:
                    s = randint(100, 1000)
                    user_db.experience += s

                    await user_db.save()
                    return f'Выйграл {s} опыта'
                else:
                    user_db.rank = 1
                    await user_db.save()
                    return "Выйграл VIP доступ"
            elif a == 3:
                s = randint(1, 30)
                user_db.money += s
                await user_db.save()
                return f"Выиграл {s} Ананасиков"
            elif a == 4:
                s = randint(150000, 1500000)
                user_db.balance += s
                await user_db.save()
                return f"Выйграл {s} Долларов"
            else:
                return "Увы... Вам ничего не выпало"
    if user_db.rank >= 2:
        return "Ты не можешь играть в рулетку"
    mani = user_db.money
    if mani >= 20:
        maa = int(mani) - 20
        user_db.money = maa
        await user_db.save()
        a = randint(1, 6)
        if a == 1:
            s = randint(100, 1000)
            user_db.experience += s

            await user_db.save()
            return f'Выйграл {s} опыта'

        elif a == 2:
            if user_db.rank >= 1:
                s = randint(100, 1000)
                user_db.experience += s

                await user_db.save()
                return f'Выйграл {s} опыта'
            else:
                user_db.rank = 1
                await user_db.save()
                return "Выйграл VIP доступ"
        elif a == 3:
            s = randint(1, 30)
            user_db.money += s
            await user_db.save()
            return f"Выиграл {s} Ананасиков"
        elif a == 4:
            s = randint(150000, 1500000)
            user_db.balance += s
            await user_db.save()
            return f"Выйграл {s} Долларов"

        else:
            return "Увы... Вам ничего не выпало"
    return f"Рулетка стоит 20 ананасиков. У вас в мешке {mani} ананасиков" \
           "\nЧто бы купить ананасы введите команду:\n" \
           "Купить ананасы {кол-во}"


"""
