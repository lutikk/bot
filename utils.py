import json
import time
from random import randint
from time import strftime, gmtime
from typing import TypeVar, Union, Iterable
from dev_up import DevUpAPI


import config
import re
import vk_api
from vkbottle.bot import Message

from models import User


def get_forward(m: Message) -> dict:
    return json.dumps(dict(
        peer_id=m.peer_id,
        conversation_message_ids=m.conversation_message_id,
        is_reply=True
    ), ensure_ascii=False)


async def biznes_up(user_id, stoim_biznes, name_biznes, old_biznes):
    """Нужно для улучшения бизнеса
    user_id -> id юзера
    stoim_biznes -> стоимость бизнеса
    name_biznes -> название улучшения
    old_biznes -> старое название
    """
    user_db = await User.get(id=user_id)
    if user_db.balance >= stoim_biznes:
        sss = user_db.balance - stoim_biznes
        user_db.balance = sss
        user_db.business = name_biznes
        await user_db.save()
        return f"Бизнес {old_biznes} улучшен до бизнеса {name_biznes}"
    else:
        f = stoim_biznes - user_db.balance
        return f"Для улучшения не хватает {f}$"


async def biznes_sn(user_id, minim, maxim):
    "снятие баланса с бизнеса"
    user_db = await User.get(id=user_id)
    ttt = time.time()
    if (ttt - user_db.biz_time) >= 3600:

        if user_db.mobile == None or user_db.mobile == "нет":
            y = ttt
        else:
            ti = randint(1, 1000)
            y = ttt - ti
        ttt_itog = ttt - user_db.biz_time
        s = round(ttt_itog)
        a = s / 3600  # Сколько часов прошло
        f = randint(minim, maxim)  # Сколько получит за час
        q = a * f  # Сколько получит за все время
        qq = round(q)
        user_db.balance += qq
        user_db.biz_time = y
        await user_db.save()
        return f'С бизнеса {user_db.business} получил {qq}$'
    else:
        l = user_db.biz_time + 3600
        s = l - time.time()
        t = strftime("%M:%S", gmtime(s))
        return f"Собирать прибыль можно будет через {t}"


def get_user_id_by_domain(user_domain: str):
    """Поиск ID по домену"""
    vk = vk_api.VkApi(token=config.main_token)

    obj = vk.method('utils.resolveScreenName', {"screen_name": user_domain})

    if isinstance(obj, list):
        return
    if obj['type'] == 'user':
        return obj["object_id"]


def search_user_ids(text):
    result = []

    regex = r"(?:vk\.com\/(?P<user>[\w\.]+))|(?:\[id(?P<user_id>[\d]+)\|)"

    for user_domain, user_id in re.findall(regex, text):
        if user_domain:
            result.append(get_user_id_by_domain(user_domain))
        if user_id:
            result.append(int(user_id))

    _result = []
    for r in result:
        if r is not None:
            _result.append(r)
    return _result


async def plas_many_admin(message: Message, user_id, admin_user_id, summ):
    user_rep = await User.get(id=user_id)

    try:
        balans = user_rep.money
        itog = int(balans) + int(summ)
        user_rep.money = itog
        await user_rep.save()
        nik2 = await message.get_user(user_ids=user_id)
        nik = await message.get_user(user_ids=admin_user_id)
        text = f"[id{nik.id}|{nik.first_name} {nik.last_name}] Выдал {summ} ананасиков [id{nik2.id}|{nik2.first_name} {nik2.last_name}]"
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        for user in await message.ctx_api.users.get(user_ids=[u.id async for u in User.filter(rank=5)]):
            try:
                message.peer_id = user.id
                await message.answer(text)
            except:
                pass
        message.peer_id = config.admin_id
        await message.answer(text)

        return text
    except:
        return 'Что то пошло не так\nСкорее всего юзера нет в бд'

async def get_nikname(m: Message, user_id: int):
    user_db = await User.get(id=user_id)
    if user_db.nickname == None or user_db.nickname == 'нет':
        a = await m.get_user(user_ids=user_id)
        print(a)
        nik3 = f'[id{a.id}|{a.first_name} {a.last_name}]'
    else:
        nik3 = f'[id{user_db.id}|{user_db.nickname}]'
        print(nik3)
    return nik3


async def minus_many_admin(message: Message, user_id, admin_user_id, summ):
    user_rep = await User.get(id=user_id)

    try:
        balans = user_rep.money
        itog = int(balans) - int(summ)
        user_rep.money = itog
        await user_rep.save()
        nik2 = await message.get_user(user_ids=user_id)
        nik = await message.get_user(user_ids=admin_user_id)
        text = f"[id{nik.id}|{nik.first_name} {nik.last_name}] Забрал {summ} ананасиков у [id{nik2.id}|{nik2.first_name} {nik2.last_name}]"
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        for user in await message.ctx_api.users.get(user_ids=[u.id async for u in User.filter(rank=5)]):
            try:
                message.peer_id = user.id
                await message.answer(text)
            except:
                pass
        message.peer_id = config.admin_id
        await message.answer(text)

        return text
    except:
        return 'Что то пошло не так\nСкорее всего юзера нет в бд'


async def minus_balans_admin(message: Message, user_id, admin_user_id, summ):
    user_rep = await User.get(id=user_id)

    try:
        balans = user_rep.balance
        itog = int(balans) - int(summ)
        user_rep.balance = itog
        await user_rep.save()
        nik2 = await message.get_user(user_ids=user_id)
        nik = await message.get_user(user_ids=admin_user_id)
        text = f"[id{nik.id}|{nik.first_name} {nik.last_name}] Забрал {summ}$ [id{nik2.id}|{nik2.first_name} {nik2.last_name}]"
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        for user in await message.ctx_api.users.get(user_ids=[u.id async for u in User.filter(rank=5)]):
            try:
                message.peer_id = user.id
                await message.answer(text)
            except:
                pass
        message.peer_id = config.admin_id
        await message.answer(text)

        return text
    except:
        return 'Что то пошло не так\nСкорее всего юзера нет в бд'


async def plas_balans_admin(message: Message, user_id, admin_user_id, summ):
    user_rep = await User.get(id=user_id)

    try:
        balans = user_rep.balance
        itog = int(balans) + int(summ)
        user_rep.balance = itog
        await user_rep.save()
        nik2 = await message.get_user(user_ids=user_id)
        nik = await message.get_user(user_ids=admin_user_id)
        text = f"[id{nik.id}|{nik.first_name} {nik.last_name}] Выдал {summ}$ [id{nik2.id}|{nik2.first_name} {nik2.last_name}]"
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        for user in await message.ctx_api.users.get(user_ids=[u.id async for u in User.filter(rank=5)]):
            try:
                message.peer_id = user.id
                await message.answer(text)
            except:
                pass
        message.peer_id = config.admin_id
        await message.answer(text)

        return
    except:
        text = 'Что то пошло не так\nСкорее всего юзера нет в бд'
        await message.answer(text)


T = TypeVar("T")


def join(data: Union[str, Iterable], separator: str = ",") -> str:
    if isinstance(data, str):
        data = [data]
    if not data:
        return ''
    return separator.join([str(obj) for obj in data])


def get_or_none(value: T) -> Union[T, str]:
    if value is None:
        return "N/A"
    return value


def b2s(value: bool) -> str:
    if value is None:
        return "N/A"
    return "✅" if value else "🚫"

async def ip(message: Message, dev_up_key, lll):
    api = DevUpAPI(dev_up_key)
    web_info = api.utils.get_web_info(lll).response

    text = (
        f"Информация об веб-адресе <<{lll}>>\n"
        f"Адрес: {get_or_none(web_info.ip_info.address)}\n"
        f"IP: {get_or_none(web_info.ip_info.ip)}\n"
        f"DNS: {get_or_none(web_info.ip_info.dns)}\n"
        f"Offset: {get_or_none(web_info.ip_info.offset)}\n"
    )
    if web_info.ip_info.organization:
        org = web_info.ip_info.organization
        text += f"Организация: {get_or_none(org.name)} | AS: {get_or_none(org.as_code)} {get_or_none(org.as_name)}\n"
        del org
    if web_info.ip_info.connection:
        conn = web_info.ip_info.connection
        text += (
            f"\nСоединение:\n"
            f"Статус: {get_or_none(conn.status)}\n"
            f"Прокси: {b2s(conn.proxy)}\n"
            f"web-server: {b2s(conn.web_server)}\n"
            f"Прямое соединение: {b2s(conn.direct_connection)}\n"
            f"Мобильная сеть: {b2s(conn.mobile_network)}\n"
        )
        del conn

    text += (
        f"\nГород: {get_or_none(web_info.ip_geo.city)} {get_or_none(web_info.ip_geo.zip)}\n"
        f"Валюта: {get_or_none(web_info.ip_geo.currency)}\n"
        f"Часовой пояс: {get_or_none(web_info.ip_geo.timezone)}\n\n"
    )

    if web_info.ip_geo.continent:
        info = web_info.ip_geo.continent
        text += f"Континент: {get_or_none(info.code)} {get_or_none(info.name)}\n"
        del info
    if web_info.ip_geo.country:
        info = web_info.ip_geo.country
        text += f"Страна: {get_or_none(info.code)} {get_or_none(info.name)}\n"
        del info
    if web_info.ip_geo.region:
        info = web_info.ip_geo.region
        text += f"Регион/город: {get_or_none(info.code)} {get_or_none(info.name)}\n"
        del info
    await message.answer(message=text,
                         disable_mentions=1,
                         forward=get_forward(message),
                         **dict(
                             lat=web_info.ip_geo.coordinates.latitude,
                             long=web_info.ip_geo.coordinates.longitude,
                         ) if web_info.ip_geo.coordinates else dict())

async def stikers(message: Message, dev_up_key, user_id):


    us = await message.get_user(user_ids=user_id)
    try:
        api = DevUpAPI(dev_up_key)
        stickers = api.vk.get_stickers(user_id).response
        text = f"📄 Пользователь [id{us.id}|{us.first_name} {us.last_name}] " \
               f"имеет {stickers.count} стикеров из {stickers.count_all}\n" \
               f"💰 Стоимость в голосах: {stickers.price.votes}\n" \
               f"💵 Стоимость в рублях: {stickers.price.rub}₽\n\n"
        text_stickers = []
        for sticker in stickers.stickers:
            text_stickers += [f"{sticker.name}"]

        ss = text + join(text_stickers, ", ")
        await message.answer(message=ss, disable_mentions=1, forward=get_forward(message))

    except Exception as ex:
        await message.answer(message=ex, disable_mentions=1, forward=get_forward(message))
