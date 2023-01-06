import json

import requests
import vk_api
from vkbottle.bot import BotLabeler, Message
from vkbottle.bot import rules as vkb_rules

from config import main_token, dev_up_key
from models import User

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text=["чатссылка", "ссыль", "чат-ссылка", "чат ссылка"])
async def greeting(message: Message):
    vk = vk_api.VkApi(token=main_token)
    reset = 0
    url = vk.method("messages.getInviteLink", {"peer_id": int(message.peer_id), "reset": reset})["link"]
    db_user = await User.get(id=message.from_id)
    if db_user.nickname == None:
        nik1 = await message.get_user(user_ids=message.from_id)
        nik = f"[id{nik1.id}|{nik1.first_name} {nik1.last_name}]"
    else:

        nik = f"[id{message.from_id}|{db_user.nickname}]"
    payload = {"key": dev_up_key, "url": url}
    r = requests.post('https://api.dev-up.ru/method/utils.createShortLink',
                      data=json.dumps(payload),
                      headers={'content-type': 'application/json'})
    q = vk.method("utils.getShortLink", {"url": url, "private": 0})["short_url"]
    url_dev = r.json()['response']['link']['url']

    await message.answer(disable_mentions=True,
                         message=f"{nik} Ссылка на эту беседу:\n{url_dev}\nАльтернативная ссылка на беседу: {q}")


@bl.message(text=["Ссыль новая", "ссыль новая", "Ссыль Новая", "ссыль Новая"])
async def greting(message: Message):
    db_user = await User.get(id=message.from_id)
    if 5 >= db_user.rank:

        vk = vk_api.VkApi(token=main_token)
        reset = 1
        url = vk.method("messages.getInviteLink", {"peer_id": int(message.peer_id), "reset": reset})["link"]
        db_user = await User.get(id=message.from_id)
        if db_user.nickname == None:
            nik1 = await message.get_user(user_ids=message.from_id)
            nik = f"[id{nik1.id}|{nik1.first_name} {nik1.last_name}]"
        else:

            nik = f"[id{message.from_id}|{db_user.nickname}]"
        payload = {"key": dev_up_key, "url": url}
        r = requests.post('https://api.dev-up.ru/method/utils.createShortLink',
                          data=json.dumps(payload),
                          headers={'content-type': 'application/json'})
        q = vk.method("utils.getShortLink", {"url": url, "private": 0})["short_url"]
        url_dev = r.json()['response']['link']['url']

        return f"{nik} Ссылка на эту беседу:\n{url_dev}\nАльтернативная ссылка на беседу: {q}"


@bl.chat_message(vkb_rules.ChatActionRule(["chat_invite_user", "chat_invite_user_by_link"]))
async def invite(m: Message):
    print(m)
