from vkbottle.bot import BotLabeler, Message

import utils
from models import User

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text=['+баланс <a:int> <vk_user_id>'])
async def gre(message: Message, a: int, vk_user_id: str, **kwargs):
    kek2 = utils.search_user_ids(vk_user_id)
    lll = kek2[0]
    lyl = message.from_id
    user_db = await User.get(id=lyl)
    user_rep = await User.get(id=lll)

    if user_db.rank >= 4:
        if not int(a) > 0:
            text = "Долбаеб..."
            await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
            return
        await utils.plas_balans_admin(message, lll, lyl, a)

    elif user_db.rank >= 3:
        if user_rep.rank >= 2:
            if not int(a) > 0:
                text = "Долбаеб..."
                await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
                return
            await utils.plas_balans_admin(message, lll, lyl, a)
            return

        else:
            text = "Ты не можешь выдавать валюту людям ниже тестировщика"
            await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
            return
    elif user_db.rank >= 2:
        if lll == lyl:
            if not int(a) > 0:
                text = "Долбаеб..."
                await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
                return
            await utils.plas_balans_admin(message, lll, lyl, a)
            return

        else:
            return


@bl.message(text=['+баланс <a>'])
async def gre(message: Message, a: int):
    lll = message.reply_message.from_id
    lyl = message.from_id
    user_db = await User.get(id=lyl)
    user_rep = await User.get(id=lll)
    if user_db.rank >= 4:
        if not int(a) > 0:
            text = "Долбаеб..."
            await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
            return
        await utils.plas_balans_admin(message, lll, lyl, a)
        return
    elif user_db.rank >= 3:
        if user_rep.rank >= 2:
            if not int(a) > 0:
                text = "Долбаеб..."
                await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
                return
            await utils.plas_balans_admin(message, lll, lyl, a)

            return
        else:
            text = "Ты не можешь выдавать валюту людям ниже тестировщика"
            await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
            return
    elif user_db.rank >= 2:
        if lll == lyl:
            if not int(a) > 0:
                text = "Долбаеб..."
                await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
                return
            await utils.plas_balans_admin(message, lll, lyl, a)
            return
        else:
            return


"""@bl.message(text=['+ананасы [id<vk_user_id:int>|<other> <a>'])
async def gre(message: Message, a: int, vk_user_id: int, **kwargs):
    kek2 = utils.search_user_ids(vk_user_id)
    lll = kek2[0]
    lyl = message.from_id
    user_db = await User.get(id=lyl)
    user_rep = await User.get(id=lll)
    if user_db.rank >= 4:
        if not int(a) > 0:
            text = "Долбаеб..."
            await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
            return
        await utils.plas_many_admin(message, lll, lyl, a)
        return
    elif user_db.rank >= 3:
        if user_rep.rank >= 2:
            if not int(a) > 0:
                text = "Долбаеб..."
                await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
                return
            await utils.plas_many_admin(message, lll, lyl, a)
            return
        else:
            text = "Ты не можешь выдавать валюту людям ниже тестировщика"
            await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
            return
    elif user_db.rank >= 2:
        if lll == lyl:
            if not int(a) > 0:
                text = "Долбаеб..."
                await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
                return
            await utils.plas_many_admin(message, lll, lyl, a)
            return
        else:
            return"""


@bl.message(text=['-баланс <a:int> <vk_user_id>'])
async def greeting(message: Message, a: int, vk_user_id: int, **kwargs):
    kek2 = utils.search_user_ids(vk_user_id)
    kek = kek2[0]
    lyl = message.from_id
    user_db = await User.get(id=lyl)
    if user_db.rank >= 4:
        if not int(a) > 0:
            text = "Долбаеб..."
            await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
            return
        await utils.minus_balans_admin(message, kek, lyl, a)
        return



"""@bl.message(text=['-ананасы <a:int> <vk_user_id>'])
async def greeting(message: Message, a: int, vk_user_id: str, **kwargs):
    kek2 = utils.search_user_ids(vk_user_id)
    kek = kek2[0]
    lyl = message.from_id
    user_db = await User.get(id=lyl)

    if user_db.rank >= 4:
        if not int(a) > 0:
            text = "Долбаеб..."
            await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
            return
        await utils.minus_many_admin(message, kek, lyl, a)
        return"""


"""@bl.message(text=['+ананасы <a>'])
async def geeting(message: Message, a: int):
    lll = message.reply_message.from_id
    lyl = message.from_id
    user_db = await User.get(id=lyl)
    user_rep = await User.get(id=lll)
    if user_db.rank >= 4:
        if not int(a) > 0:
            text = "Долбаеб..."
            await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
            return

        await utils.plas_many_admin(message, lll, lyl, a)
        return

    elif user_db.rank >= 3:
        if user_rep.rank >= 2:
            if not int(a) > 0:
                text = "Долбаеб..."
                await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
                return
            text = await utils.plas_many_admin(message, lll, lyl, a)
            return
        else:
            text = "Ты не можешь выдавать валюту людям ниже тестировщика"
            await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
            return
    elif user_db.rank >= 2:
        if not int(a) > 0:
            text = "Долбаеб..."
            await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
            return
        if lll == lyl:
            await utils.plas_many_admin(message, lll, lyl, a)
            return
        else:
            text = "Ты не можешь выдавать людям валюту"
            await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
            return"""


"""@bl.message(text=['-ананасы <a>'])
async def geetin(message: Message, a: int):
    kek = message.reply_message.from_id
    lyl = message.from_id
    user_db = await User.get(id=lyl)

    if user_db.rank >= 4:
        if not int(a) > 0:
            text = "Долбаеб..."
            await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
            return
        await utils.minus_many_admin(message, kek, lyl, a)
        return"""


@bl.message(text=['-баланс <a>'])
async def geetin(message: Message, a: int):
    kek = message.reply_message.from_id
    lyl = message.from_id
    user_db = await User.get(id=lyl)

    if user_db.rank >= 4:
        if not int(a) > 0:
            text = "Долбаеб..."
            await message.answer(message=text, disable_mentions=1, forward=utils.get_forward(message))
            return
        else:
            await utils.minus_balans_admin(message, kek, lyl, a)
            return
