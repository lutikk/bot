import time

from vkbottle.bot import BotLabeler, Message

from models import User
from utils import get_forward

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text=["Пинг", "пинг"])
async def greeting(message: Message):
    delta = round(time.time() - message.date, 2)

    # А ты думал тут все чесно будет? Не, я так не работаю...
    if delta < 0:
        delta = "666"
    return await message.answer(f"Понг\nВыбесил за {delta} секунд", attachment='photo-201566067_457240629',
                                disable_mentions=1, forward=get_forward(message))


@bl.message(text=["!ник <nik>", "!Ник <nik>"])
async def greeing(message: Message, nik: str):
    user_db = await User.get(id=message.from_id)
    sss = nik.replace(".", "․")
    async for user in User.filter(nickname=sss):
        n = await message.get_user(user_ids=user.id)
        return f"Такой ник сейчас у [id{n.id}|{n.first_name} {n.last_name}]"
    user_db.nickname = sss
    await user_db.save()
    return f"Поставил ник {sss}"


@bl.message(text=["!назначить ник <nik>", "!Назначить Ник <nik>"])
async def reeting(message: Message, nik: str):
    user_db = await User.get(id=message.from_id)
    user_rep = await User.get(id=message.reply_message.from_id)
    if user_db.rank >= 5:
        sss = nik.replace(".", "․")
        async for user in User.filter(nickname=sss):
            n = await message.get_user(user_ids=user.id)
            return f"Такой ник сейчас у [id{n.id}|{n.first_name} {n.last_name}]"
        user_rep.nickname = sss
        await user_rep.save()
        return f"Поставил ник {sss}"

    if user_db.rank >= 1:
        if user_rep.rank >= 1:
            return "Можно устанавливать ник только юзерам"
        sss = nik.replace(".", "․")
        async for user in User.filter(nickname=sss):
            n = await message.get_user(user_ids=user.id)
            return f"Такой ник сейчас у [id{n.id}|{n.first_name} {n.last_name}]"
        user_rep.nickname = sss
        await user_rep.save()
        return f"Поставил ник {sss}"


@bl.message(text=["Мешок", "мешок", "Баланс", "баланс"])
async def grdeeting(message: Message):
    user_db = await User.get(id=message.from_id)

    dd = user_db.balance
    return f"Баланс: {dd} $\nБиткойны 🪙: {user_db.bitcoin}"


@bl.message(text="!!обнулить")
async def greetin(message: Message):
    user_db = await User.get(id=message.from_id)
    if user_db.rank >= 10:
        user_rep = await User.get(id=message.reply_message.from_id)
        user_rep.rank = 0
        user_rep.balance = 0
        user_rep.experience = 0
        user_rep.work = "нет"
        user_rep.business = "нет"
        user_rep.house = "нет"
        user_rep.transport = "нет"
        user_rep.mobile = "нет"
        user_rep.pc = "нет"
        user_rep.aircopt = "нет"
        user_rep.airplane = "нет"
        user_rep.bitcoin = 0
        user_rep.bitcoin_ferm = 0
        await user_rep.save()
        return "OK"


@bl.message(text="!!обнулить [id<vk_user_id:int>|<other>")
async def greetings(message: Message, vk_user_id: int, **kwargs):
    user_db = await User.get(id=message.from_id)
    if user_db.rank >= 10:
        user_rep = await User.get(id=vk_user_id)

        user_rep.rank = 0
        user_rep.balance = 0

        user_rep.experience = 0
        user_rep.work = "нет"
        user_rep.business = "нет"
        user_rep.house = "нет"
        user_rep.transport = "нет"
        user_rep.mobile = "нет"
        user_rep.pc = "нет"
        user_rep.aircopt = "нет"
        user_rep.airplane = "нет"
        user_rep.bitcoin = 0
        user_rep.bitcoin_ferm = 0
        await user_rep.save()
        return "OK"
