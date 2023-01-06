import json

import requests_async as requests
from loguru import logger
from vkbottle.bot import BotLabeler, Message

from utils import get_forward

bl = BotLabeler()

bl.vbml_ignore_case = True


async def ii22(text):
    url = f"https://roughs.ru/api/talker?text={text}&source_from=https://vk.com/id677040228/"
    r = await requests.get(url)
    print(r.json())
    text = r.json()['answer']

    return text


async def ii33(text: str, user_id: int):
    try:
        data = {"ask": f'{text}', "userid": user_id}
        headers = {'Content-Type': 'application/x-www-form-urlencoded,'}
        data_json = json.dumps(data, ensure_ascii=False)
        payload = {'query': data_json}
        apiurl = "https://aiproject.ru/api/"
        resp = await requests.post(apiurl, data=payload, headers=headers)
        answer = resp.json()

        responce = answer['aiml'].encode('iso-8859-1').decode('utf-8')  # ответ бота в этой переменной
        logger.opt(colors=True).success(
            f"""<b><green>Запрос:{text}: Ответ: {responce} </green></b>"""
        )
        return responce
    except Exception as err:
        logger.error(f"Ошибка {err}")

async def ii(text):

    js = {
        "key": '',
        "inp": text
    }
    ss = await requests.post('https://luxuryduty.ru/api/dutys/ii/', json=js)
    print(ss)
    print(ss.json())
    return ss.json()


@bl.message(text=["ии <url>", "скрепка <url>", "бот <url>"])
async def greeting(message: Message, url: str):
    text = await ii(url)

    return await message.answer(message=text['response']['answer'])
