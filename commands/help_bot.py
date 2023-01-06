import vk_api
from vkbottle.bot import BotLabeler, Message

from config import main_token
from models import User

bl = BotLabeler()
bl.vbml_ignore_case = True

@bl.message(text='commands')
async def greeting(message: Message):
    user_db = await User.get(id=message.from_id)
    if user_db.rank >= 5:

        handle = open("commands.txt", "r", encoding="utf-8")
        data = handle.read()
        return str(data)
    else:
        return

@bl.message(text=["помощь", "Помощь", "Ладно Помощь", "Ладно помощь", "ладно помощь", "ладно Помощь"])
async def greeting(message: Message):
    ranks_4 = ''
    ranks_5 = ''

    for user in await message.ctx_api.users.get(user_ids=[u.id async for u in User.filter(rank=4)]):
        ranks_4 += f"[id{user.id}|{user.first_name} {user.last_name}]\n"

    for user in await message.ctx_api.users.get(user_ids=[u.id async for u in User.filter(rank=5)]):
        ranks_5 += f"[id{user.id}|{user.first_name} {user.last_name}]\n"

    access_token = main_token
    vk = vk_api.VkApi(token=access_token)
    reset = 0
    url = vk.method("messages.getInviteLink", {"peer_id": 2000000001, "reset": reset})["link"]
    url_help = vk.method("messages.getInviteLink", {"peer_id": 2000000006, "reset": reset})["link"]
    url1 = "https://vk.com/@clip_bot-komandy-bota"
    s = vk.method("utils.getShortLink", {"url": url1, "private": 0})["short_url"]
    q = vk.method("utils.getShortLink", {"url": url, "private": 0})["short_url"]
    help_link = vk.method("utils.getShortLink", {"url": url_help, "private": 0})["short_url"]
    text = f"Все команды доступны по этой ссылке:\n{s}\n\n" \
           f"Вы можете уточнить свой вопрос в чате помощи {help_link}\n" \
           f"\nТак же вы можете обратиться к нашим агентам\n{ranks_4}\n{ranks_5}\n\n" \
           f"Наш чатик для общения: {q}"

    await message.answer(disable_mentions=True, message=text)


@bl.message(text="flvbys ,jnf ")
async def greetng(message: Message):
    user_db = await User.get(id=message.from_id)
    if int(user_db.rank) >= 2:

        ranks_5 = ''
        for user in await message.ctx_api.users.get(user_ids=[u.id async for u in User.filter(rank=5)]):
            ranks_5 += f"[id{user.id}|{user.first_name} {user.last_name}]\n"

        text = f"Админы бота: \n{ranks_5}"
        await message.answer(disable_mentions=True, message=text)


@bl.message(text=["Кто вип", "Кто Вип", "кто Вип", "кто вип"])
async def greetig(message: Message):
    user_db = await User.get(id=message.from_id)
    if int(user_db.rank) >= 4:
        ranks_1 = ""
        for user in await message.ctx_api.users.get(user_ids=[u.id async for u in User.filter(rank=1)]):
            ranks_1 += f"[id{user.id}|{user.first_name} {user.last_name}]\n"

        await message.answer(disable_mentions=True, message=f'Наши дорогие випы:\n{ranks_1}')


@bl.message(text=["Кто тестер", "Кто Тестер", "кто Тестер", "кто тестер"])
async def greting(message: Message):
    sees = ''
    user_db = await User.get(id=message.from_id)
    if int(user_db.rank) >= 3:
        ranks_2 = ""
        for user in await message.ctx_api.users.get(user_ids=[u.id async for u in User.filter(rank=2)]):
            ranks_2 += f"[id{user.id}|{user.first_name} {user.last_name}]\n"
        await message.answer(f'Наши тестеры:\n{ranks_2}', disable_mentions=True, )


@bl.message(text=["Кто разраб", "Кто Разраб", "кто Разраб", "кто разраб"])
async def greetin(message: Message):
    sees = ''
    user_db = await User.get(id=message.from_id)
    if int(user_db.rank) >= 4:
        ranks_3 = ""
        for user in await message.ctx_api.users.get(user_ids=[u.id async for u in User.filter(rank=3)]):
            ranks_3 += f"[id{user.id}|{user.first_name} {user.last_name}]\n"

        await message.answer(message=f'Наши разрабы:\n{ranks_3}', disable_mentions=True)

"""
@bl.message(text=["топ звезды", "топ звёзды", "звезды"])
async def greetin(message: Message):
    sees = ''
    users = await User.filter(rank__lt=2).order_by("-reputation").limit(10)
    vk_users = await message.ctx_api.users.get(user_ids=[u.id for u in users])

    for i, user in enumerate(users, 1):
        for vk_user in vk_users:
            if user.id == vk_user.id:
                sees += f'{i}. [id{vk_user.id}|{vk_user.first_name} {vk_user.last_name}] -> {user.reputation}\n'
    await message.answer(disable_mentions=True, message=f"Топ игроков по звёздам:\n\n{sees}")"""


@bl.message(text="топ")
async def greftin(message: Message):
    sees = ''

    users = await User.filter(rank__lt=2).order_by("-balance").limit(30)
    vk_users = await message.ctx_api.users.get(user_ids=[u.id for u in users])

    for i, user in enumerate(users, 1):
        for vk_user in vk_users:
            if user.id == vk_user.id:
                sees += f'{i}. [id{vk_user.id}|{vk_user.first_name} {vk_user.last_name}] -> {user.balance}$\n'

    await message.answer(disable_mentions=True, message=f"Топ богатейших игроков:\n\n{sees}")
