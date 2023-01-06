import time
from time import gmtime
from time import strftime
from utils import get_forward, search_user_ids, get_nikname
from vkbottle.bot import BotLabeler, Message

from models import User

bl = BotLabeler()
bl.vbml_ignore_case = True

async def time_per(user_id):
    user_db = await User.get(id=user_id)
    if (time.time() - user_db.balanse_time) >= 86400:
        user_db.balanse_time = time.time()
        user_db.perevod_limit = 0
        await user_db.save()
        return 'OK'
    else:
        return 'NO'

async def perevod(message: Message, user_otprav, user_polu, suma):
    lyl = await time_per(user_id=user_otprav)
    print(lyl)
    user_ot = await User.get(id=user_otprav)
    user_p = await User.get(id=user_polu)
    print("начнем")
    if user_ot.rank >= 2:
        await message.answer("Ты не можешь переводить валюту",  disable_mentions=1, forward=get_forward(message))
        return
    elif user_ot.rank == 1:
        limit = 10000000 - user_ot.perevod_limit
        if limit <= 0:
            l = user_ot.balanse_time + 86400
            s = l - time.time()
            t = strftime("%H:%M:%S", gmtime(s))
            await message.answer(f"Ты сможешь совершать переводы через {t}", disable_mentions=1, forward=get_forward(message))
            return


        if limit < int(suma):
            await message.answer(f"Ты можешь перевести не больше {limit}$", disable_mentions=1, forward=get_forward(message))
            return
        elif user_ot.balance < int(suma):
            await message.answer(f"У тебя нет столько денег...", disable_mentions=1,
                                 forward=get_forward(message))
            return
        else:
            user_ot.balance -= suma
            user_ot.perevod_limit += suma
            user_p.balance += suma
            await user_ot.save()
            await user_p.save()
            name = await get_nikname(message, user_p.id)
            text = f"Вы перевели {name} {suma}$"
            await message.answer(text, disable_mentions=1, forward=get_forward(message))
            return
    elif user_ot.rank == 0:
        limit = 5000000 - user_ot.perevod_limit
        if limit <= 0:
            l = user_ot.balanse_time + 86400
            s = l - time.time()
            t = strftime("%H:%M:%S", gmtime(s))
            await message.answer(f"Ты сможешь совершать переводы через {t}", disable_mentions=1,
                                 forward=get_forward(message))
            return

        if limit < int(suma):
            await message.answer(f"Ты можешь перевести не больше {limit}$", disable_mentions=1,
                                 forward=get_forward(message))
            return
        elif user_ot.balance < int(suma):
            await message.answer(f"У тебя нет столько денег...", disable_mentions=1,
                                 forward=get_forward(message))
            return
        else:
            user_ot.balance -= suma
            user_ot.perevod_limit += suma
            user_p.balance += suma
            await user_ot.save()
            await user_p.save()
            name = await get_nikname(message, user_p.id)
            text = f"Вы перевели {name} {suma}$"
            await message.answer(text, disable_mentions=1, forward=get_forward(message))
            return

@bl.message(text='передать <a:int>')
async def greting(message: Message, a: int):
    await perevod(message, message.from_id, message.reply_message.from_id, a)
    return


@bl.message(text='передать <a:int> <vk_user_id>')
async def greting(message: Message, a: int, vk_user_id: str, **kwargs):
    user_id = search_user_ids(vk_user_id)
    await perevod(message, message.from_id, user_id[0], a)
    return