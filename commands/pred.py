from vkbottle.bot import BotLabeler, Message
from utils import get_forward, search_user_ids, get_nikname
from models import User
from config import admin_id as log
bl = BotLabeler()
bl.vbml_ignore_case = True


async def rang(yr, users):
    try:
        user_db = await User.get(id=users)
        user_db.rank = yr
        await user_db.save()
        return "OK"
    except:
        return "Error"


@bl.message(text="ранг <a:int> <vk_user_id>")
async def greeting(message: Message, a: int, vk_user_id: str, **kwargs):

    user_db = await User.get(id=message.from_id)
    lll = message.from_id
    idd = search_user_ids(message.text)
    sss = idd[0]
    try:
        user_rep = await User.get(id=sss)
        if user_db.rank >= 6:
            if await rang(yr=a, users=sss) == "OK":
                nik2 = await get_nikname(message, sss)
                await message.answer(message=f"Выдал ранг {a} {nik2}", disable_mentions=1, forward=get_forward(message))

                message.peer_id = log
                nik2 = await get_nikname(message, sss)
                nik = await get_nikname(message, lll)
                text = f"{nik} Выдал {a} ранг " \
                       f"{nik2}"
                return text
            else:
                return "Что то пошло не так\nСкорее всего юзера нет в БД"
        if user_db.rank >= 5:
            if int(a) >= 4:
                return "У тебя не хватает прав "
            if user_rep.rank > int(a):
                return "Ты не можешь понижать"
            if await rang(yr=a, users=sss) == "OK":
                nik2 = await get_nikname(message, sss)
                await message.answer(f"Выдал ранг {a} {nik2}", disable_mentions=1, forward=get_forward(message))
                message.peer_id = log
                nik = await get_nikname(message, lll)
                text = f"{nik} Выдал {a} ранг " \
                       f"{nik2}"
                return text
            else:
                return "Что то пошло не так\nСкорее всего юзера нет в БД"
    except:
        return "Что то пошло не так\nСкорее всего юзера нет в БД"


@bl.message(text="ранг <a>")
async def greeting(message: Message, a: int):
    user_db = await User.get(id=message.from_id)
    lll = message.from_id
    sss = message.reply_message.from_id
    try:
        user_rep = await User.get(id=sss)
        if user_db.rank >= 6:
            if await rang(yr=a, users=sss) == "OK":
                nik2 = await get_nikname(message, sss)
                await message.answer(message=f"Выдал ранг {a} {nik2}", disable_mentions=1, forward=get_forward(message))

                message.peer_id = log
                nik2 = await get_nikname(message, sss)
                nik = await get_nikname(message, lll)
                text = f"{nik} Выдал {a} ранг " \
                       f"{nik2}"
                return text
            else:
                return "Что то пошло не так\nСкорее всего юзера нет в БД"
        if user_db.rank >= 5:
            if int(a) >= 4:
                return "У тебя не хватает прав "
            if user_rep.rank >= int(a):
                return "Ты не можешь понижать"
            if await rang(yr=a, users=sss) == "OK":
                nik2 = await get_nikname(message, sss)
                await message.answer(f"Выдал ранг {a} {nik2}", disable_mentions=1, forward=get_forward(message))
                message.peer_id = log
                nik = await get_nikname(message, lll)
                text = f"{nik} Выдал {a} ранг " \
                       f"{nik2}"
                return text
            else:
                return "Что то пошло не так\nСкорее всего юзера нет в БД"
    except:
        return "Что то пошло не так\nСкорее всего юзера нет в БД"
