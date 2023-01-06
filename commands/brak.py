from vkbottle.bot import BotLabeler, Message

from models import User
from utils import search_user_ids, get_forward

bl = BotLabeler()
bl.vbml_ignore_case = True


async def brak(message: Message, lol, kek):
    print("Начнем тест браков")
    user_db = await User.get(id=lol)  # Основной id
    user_rep = await User.get(id=kek)  # айди на который будет брак
    if user_db.brak == None or user_db.brak == "нет":

        if user_rep.brak == None or user_rep.brak == "нет":
            user_rep.brak_zv = user_db.id
            await user_rep.save()
            text = "Отправил заявку на брак"
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return
        else:
            a = user_rep.brak
            user_br = await User.get(id=a)
            nik1 = user_br.nickname
            if nik1 == None:
                a = await message.get_user(user_ids=user_br.id)
                nik = f'[id{a.id}|{a.first_name} {a.last_name}]'
            else:
                nik = f'[id{a.id}|{user_br.nickname}]'
            nik2 = user_rep.nickname
            if nik2 == None:
                a = await message.get_user(user_ids=user_rep.id)
                nik3 = f'[id{a.id}|{a.first_name} {a.last_name}]'
            else:
                nik3 = f'[id{a.id}|{user_rep.nickname}]'

            text = f'📝📝 К сожалению, {nik3} уже состоит в браке с {nik}\n'
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return

    else:
        a = user_db.brak
        user_br = await User.get(id=a)
        nik1 = user_br.nickname
        if nik1 == None:
            a = await message.get_user(user_ids=user_br.id)
            nik = f'[id{a.id}|{a.first_name} {a.last_name}]'
        else:
            nik = f'[id{a.id}|{user_br.nickname}]'

        return f'📝 Вы уже состоите в браке с {nik}\n'


@bl.message(text="брак")
async def bot_kik1(message: Message):
    if message.reply_message.from_id == message.from_id:
        await message.answer(message="Хватит дрочить", disable_mentions=1, forward=get_forward(message))
        return

    try:
        lol = message.from_id
        print(lol)
        kek = message.reply_message.from_id
        print(kek)
        text = await brak(message, lol, kek)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    except:
        return


@bl.message(text="брак нет")
async def bot_kik1(message: Message):
    user_db = await User.get(id=message.from_id)
    if user_db.brak_zv == None or user_db.brak_zv == "нет":
        return "Вам никто не предлагал брак"
    user_db.brak_zv = "нет"
    await user_db.save()
    await message.answer(message="Отклонил заявку на брак", disable_mentions=1, forward=get_forward(message))
    return

@bl.message(text="брак да")
async def bot_kik1(message: Message):
    lol = message.from_id
    user_db = await User.get(id=lol)
    if user_db.brak_zv == "нет" or user_db.brak_zv == None:
        await message.answer(message="Вам никто не предлагал брак", disable_mentions=1, forward=get_forward(message))
        return
    s = user_db.brak_zv
    user_rep = await User.get(id=s)
    user_db.brak = s
    user_db.brak_zv = "нет"
    user_rep.brak = lol
    user_rep.brak_zv = "нет"
    await user_rep.save()
    await user_db.save()
    nik3 = user_db.nickname
    if nik3 == None:
        a = await message.get_user(user_ids=user_db.id)
        nik1 = f'[id{a.id}|{a.first_name} {a.last_name}]'
    else:
        nik1 = f'[id{user_db.id}|{user_db.nickname}]'
    nik4 = user_rep.nickname
    if nik4 == None:
        b = await message.get_user(user_ids=user_rep.id)
        nik2 = f'[id{b.id}|{b.first_name} {b.last_name}]'
    else:
        nik2 = f'[id{user_rep.id}|{user_rep.nickname}]'

    text = f"💍 {nik1} приняла предложение о браке\n" \
           f"👨‍⚖👰 С сегодняшнего дня {nik2} и {nik1} состоят в браке"
    await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
    return



@bl.message(text="брак <vk_user_id>")
async def bot_kik1(message: Message, vk_user_id: str, **kwargs):
    if vk_user_id == message.from_id:
        return "Хватит дрочить"
    try:
        user_ids = search_user_ids(vk_user_id)
        lol = message.from_id
        kek = user_ids[0]
        text = await brak(message, lol, kek)
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return

    except:
        return




@bl.message(text="развод")
async def bot_kik1(message: Message):
    lol = message.from_id
    user_db = await User.get(id=lol)
    if user_db.brak == None or user_db.brak == "нет":
        text = "Вы не состоите в браке"
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    user_rep = await User.get(id=user_db.brak)
    user_db.brak = "нет"
    user_rep.brak = "нет"
    await user_rep.save()
    await user_db.save()
    text = "Ваш развод прошел успешно"
    await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
    return
