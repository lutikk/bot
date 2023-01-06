from dev_up import DevUpAPI
from vkbottle.bot import BotLabeler, Message

from config import dev_up_key
from utils import *

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text="стикеры")
async def greetin(message: Message):
    if message.reply_message == None:
        vk_user = message.from_id
    else:
        vk_user = message.reply_message.from_id
    await stikers(message=message, dev_up_key=dev_up_key, user_id=vk_user)
    return


@bl.message(text="стикеры <vk_user>")
async def greetin(message: Message, vk_user: str, **kwargs):
    print(vk_user)
    user_id = search_user_ids(message.text)
    await stikers(message=message, dev_up_key=dev_up_key, user_id=user_id[0])
    return


@bl.message(text="группы")
async def greetin(message: Message):
    if message.reply_message == None:
        vk_user = message.from_id
    else:
        vk_user = message.reply_message.from_id
    us = await message.get_user(user_ids=vk_user)
    dev_api = DevUpAPI(dev_up_key)
    user_groups = await dev_api.vk.get_groups_async(vk_user)
    text = (
        f"📄 Пользователь [id{us.id}|{us.first_name} {us.last_name}] "
        f"имеет {user_groups.response.count} групп\n\n"
    )
    for group in user_groups.response.groups:
        text += f"[club{group.group_id}|{group.name}]\n"
    await message.answer(message=text, disable_mentions=1, forward=get_forward(message))


@bl.message(text="группы <vk_user>")
async def greetin(message: Message, vk_user: str, **kwargs):
    user_id = search_user_ids(message.text)
    us = await message.get_user(user_ids=user_id[0])
    dev_api = DevUpAPI(dev_up_key)
    user_groups = await dev_api.vk.get_groups_async(user_id[0])
    text = (
        f"📄 Пользователь [id{us.id}|{us.first_name} {us.last_name}] "
        f"имеет {user_groups.response.count} групп\n\n"
    )
    for group in user_groups.response.groups:
        text += f"[club{group.group_id}|{group.name}]\n"
    await message.answer(message=text, disable_mentions=1, forward=get_forward(message))


@bl.message(text="ip <lll>")
async def greetin(message: Message, lll: str):
    await ip(message=message, dev_up_key=dev_up_key, lll=lll)
    return


@bl.message(text="расшифровка <nomer>")
async def greeting(message: Message, nomer: str):
    api = DevUpAPI(dev_up_key)

    custom = await api.make_request_async(
        "utils.checklink",
        data=dict(url=nomer),
        dataclass=dict
    )
    print(custom['response']["original_url"])
    text = f"Сокращенная ссылка: {custom['response']['url']}\n" \
           f"Оригинальная ссылка {custom['response']['original_url']}"
    await message.answer(message=text, disable_mentions=1, forward=get_forward(message))


@bl.message(text=["плейлист <nomer>", "плейлисты <nomer>"])
async def greeting(message: Message, nomer: str):
    api = DevUpAPI(dev_up_key)

    try:
        custom = await api.make_request_async(
            "vk.searchPlaylists",
            data=dict(q=nomer),
            dataclass=dict
        )
        print(custom)
        text = f"{custom['response']['msg_response']}"
        await message.answer(message=text, attachment=custom['response']['attachments'], disable_mentions=1,
                             forward=get_forward(message))
    except Exception as ex:
        await message.answer(message=f'⚠ Ошибка: {ex}', disable_mentions=1, forward=get_forward(message))


@bl.message(text=["песни <nomer>", "музыка <nomer>"])
async def greeting(message: Message, nomer: str):
    api = DevUpAPI(dev_up_key)

    try:
        custom = await api.make_request_async(
            "vk.searchAudio",
            data=dict(q=nomer),
            dataclass=dict
        )
        print(custom)
        text = f"{custom['response']['msg_response']}"
        await message.answer(message=text, attachment=custom['response']['attachments'], disable_mentions=1,
                             forward=get_forward(message))
    except Exception as ex:
        await message.answer(message=f'⚠ Ошибка: {ex}', disable_mentions=1, forward=get_forward(message))


@bl.message(text="подписки")
async def kik_bot(message: Message):
    if message.reply_message == None:
        vk_user_id = message.from_id
    else:
        vk_user_id = message.reply_message.from_id
    us = await message.get_user(user_ids=vk_user_id)

    api = DevUpAPI(dev_up_key)

    custom = await api.make_request_async(
        "vk.userGetSubscriptions",
        data=dict(user_id=f"{vk_user_id}"),
        dataclass=dict
    )
    print(custom)
    if custom['response']['count'] == 0:
        return f"Пользователь [id{us.id}|{us.first_name} {us.last_name}] ни на кого не подписан"
    else:
        i = 0
        text = f"Пользователь [id{us.id}|{us.first_name} {us.last_name}] подписан на {custom['response']['count']} человек\n\n"
        while custom['response']['count'] > i:
            sss = custom["response"]["subscriptions"][i]
            uss = await message.get_user(user_ids=sss)
            text += f'[id{uss.id}|{uss.first_name} {uss.last_name}]\n'
            i += 1
    await message.answer(message=text, disable_mentions=1, forward=get_forward(message))


@bl.message(text="подписки <vk_user>")
async def kik_bot(message: Message, vk_user: str, **kwargs):
    print(vk_user)
    vk_user_id = search_user_ids(message.text)
    us = await message.get_user(user_ids=vk_user_id[0])

    api = DevUpAPI(dev_up_key)

    custom = await api.make_request_async(
        "vk.userGetSubscriptions",
        data=dict(user_id=f"{vk_user_id[0]}"),
        dataclass=dict
    )
    print(custom)
    if custom['response']['count'] == 0:
        return f"Пользователь [id{us.id}|{us.first_name} {us.last_name}] ни на кого не подписан"
    else:
        i = 0
        text = f"Пользователь [id{us.id}|{us.first_name} {us.last_name}] подписан на {custom['response']['count']} человек\n\n"
        while custom['response']['count'] > i:
            sss = custom["response"]["subscriptions"][i]
            uss = await message.get_user(user_ids=sss)
            text += f'[id{uss.id}|{uss.first_name} {uss.last_name}]\n'
            i += 1
    await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
