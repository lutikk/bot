from tortoise.exceptions import DoesNotExist
from vkbottle.bot import BotLabeler, Message

from models import User
from utils import get_forward, search_user_ids

bl = BotLabeler()
bl.vbml_ignore_case = True


async def admin_info(message: Message, user_id):
    user_db = await User.get(id=user_id)
    a = await message.get_user(user_ids=user_id)
    name = f'[id{a.id}|{a.first_name} {a.last_name}]'
    text = f"Аккаунт VK 👑: {name}\n"
    if user_db.rank >= 6:
        text += 'Ранг в "Ладно" 💼: Владелец\n'
    elif user_db.rank == 5:
        text += 'Ранг в "Ладно" 💼: Администратор\n'
    elif user_db.rank == 4:
        text += 'Ранг в "Ладно" 💼: Агент ТП\n'
    elif user_db.rank == 3:
        text += 'Ранг в "Ладно" 💼: Разработчик\n'
    elif user_db.rank == 2:
        text += 'Ранг в "Ладно" 💼: Toster\n'
    elif user_db.rank == 1:
        text += 'Ранг в "Ладно" 💼: VIP\n'
    elif user_db.rank == 0:
        text += 'Ранг в "Ладно" 💼: User\n'
    else:
        text += 'Ранг в "Ладно" 💼: Игнор\n'
    if user_db.nickname == None or user_db.nickname == "нет":
        text += f'Ник: {user_db.nickname}\n'
    else:
        text += f'Ник: {user_db.nickname}\n'
    if user_db.brak == None or user_db.brak == "нет":
        text += f'Брак: нет\n'
    else:
        # блять можно не надо а?
        user_br = await User.get(id=user_db.brak)
        nik3 = user_br.nickname
        if nik3 == None:
            a = await message.get_user(user_ids=user_br.id)
            text += f'Брак [id{a.id}|{a.first_name} {a.last_name}]\n'
        else:
            text += f'Брак [id{user_br.id}|{user_br.nickname}]\n'

    text += f'Доллары $:{user_db.balance}\n'
    text += f'Работа 💼: {user_db.work}\n'
    text += f'Опыт работы 🔬: {user_db.experience}\n'
    text += f"Биткойны 🪙: {user_db.bitcoin}\n"
    text += f"Фермы 🏦: {user_db.bitcoin_ferm}\n"
    text += f'Машина 🚙: {user_db.transport}\n'
    text += f'Дом 🏡: {user_db.house}\n'
    text += f"ПК 💻: {user_db.pc}\n"
    text += f"Телефон 📱: {user_db.mobile}\n"
    text += f"Вертолёт 🚁: {user_db.aircopt}\n"
    text += f'Самолет ✈: {user_db.airplane}\n'
    text += f'Бизнес 🏤: {user_db.business}\n\n'
    if user_db.brak_zv == None or user_db.brak_zv == "нет":
        text += "Заявок на брак нет\n"
    else:
        a = await message.get_user(user_ids=user_db.brak_zv)
        text += f'Заявка на брак от [id{a.id}|{a.first_name} {a.last_name}]\n'
    return text


async def info(message: Message, user_id):
    user_db = await User.get(id=user_id)
    a = await message.get_user(user_ids=message.reply_message.from_id)
    name = f'[id{a.id}|{a.first_name} {a.last_name}]'
    text = f"Аккаунт VK 👑: {name}\n"
    if user_db.rank >= 6:
        text += 'Ранг в "Ладно" 💼: Владелец\n'
    elif user_db.rank == 5:
        text += 'Ранг в "Ладно" 💼: Администратор\n'
    elif user_db.rank == 4:
        text += 'Ранг в "Ладно" 💼: Агент ТП\n'
    elif user_db.rank == 3:
        text += 'Ранг в "Ладно" 💼: Разработчик\n'
    elif user_db.rank == 2:
        text += 'Ранг в "Ладно" 💼: Toster\n'
    elif user_db.rank == 1:
        text += 'Ранг в "Ладно" 💼: VIP\n'
    elif user_db.rank == 0:
        text += 'Ранг в "Ладно" 💼: User\n'
    else:
        text += 'Ранг в "Ладно" 💼: Игнор\n'
    if user_db.nickname == None or user_db.nickname == "нет":
        pass
    else:
        text += f'Ник: {user_db.nickname}\n'
    if user_db.brak == None or user_db.brak == "нет":
        pass
    else:
        # блять можно не надо а?
        user_br = await User.get(id=user_db.brak)
        nik3 = user_br.nickname
        if nik3 == None:
            a = await message.get_user(user_ids=user_br.id)
            text += f'Брак [id{a.id}|{a.first_name} {a.last_name}]\n'
        else:
            text += f'Брак [id{user_br.id}|{user_br.nickname}]\n'

    if user_db.balance == 0:
        pass
    else:
        text += f'Доллары $:{user_db.balance}\n'

    if user_db.work == None or user_db.work == "нет":
        pass
    else:
        text += f'Работа 💼: {user_db.work}\n'
    if user_db.experience == 0:
        pass
    else:
        text += f'Опыт работы 🔬: {user_db.experience}\n'
    if user_db.bitcoin == 0:
        pass
    else:
        text += f"Биткойны 🪙: {user_db.bitcoin}\n"

    if user_db.bitcoin_ferm == 0:
        pass
    else:
        text += f"Фермы 🏦: {user_db.bitcoin_ferm}\n"
    if user_db.transport == None or user_db.transport == 'нет':
        pass
    else:
        text += f'Машина 🚙: {user_db.transport}\n'
    if user_db.house == None or user_db.house == "нет":
        pass
    else:
        text += f'Дом 🏡: {user_db.house}\n'

    if user_db.pc == None or user_db.pc == "нет":
        pass
    else:
        text += f"ПК 💻: {user_db.pc}\n"
    if user_db.mobile == None or user_db.mobile == "нет":
        pass
    else:
        text += f"Телефон 📱: {user_db.mobile}\n"
    if user_db.aircopt == None or user_db.aircopt == "нет":
        pass
    else:
        text += f"Вертолёт 🚁: {user_db.aircopt}\n"
    if user_db.airplane == None or user_db.airplane == "нет":
        pass
    else:
        text += f'Самолет ✈: {user_db.airplane}\n'

    if user_db.business == None or user_db.business == "нет":
        pass
    else:
        text += f'Бизнес 🏤: {user_db.business}\n'
    return text


@bl.message(text=["Гет", "гет"])
async def greeting(message: Message):
    print(message.from_id, message.reply_message.from_id)
    try:
        user_get = await User.get(id=message.from_id)
        if user_get.rank >= 3:
            text = await admin_info(message, message.reply_message.from_id)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return
        elif user_get.rank >= 1:

            text = await info(message, message.reply_message.from_id)
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return

    except DoesNotExist:
        return "Юзера нет в бд"


@bl.message(text='гет <vk_user_id>')
async def greeting(message: Message, vk_user_id: str, **kwargs):
    try:
        user_id = search_user_ids(vk_user_id)
        user_get = await User.get(id=message.from_id)
        if user_get.rank >= 3:
            text = await admin_info(message, user_id[0])
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return
        elif user_get.rank >= 1:

            text = await info(message, user_id[0])
            await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
            return

    except DoesNotExist:
        return "Юзера нет в бд"
