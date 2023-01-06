import random

from vkbottle.bot import BotLabeler, Message

from models import User
from utils import get_forward

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text='казино <cost:int>')
async def greeting(message: Message, cost: int):
    if message.peer_id ==2000000001:
        return "Нельзя в этом чате в казино играть"
    if not cost >= 50:
        return "Минимальная ставка 50$"
    db_user = await User.get(id=message.from_id)

    if db_user.balance < cost:
        return "Вам не хватает для ставки"

    qqq = db_user.balance - cost
    db_user.balance = qqq
    await db_user.save()
    result_k = random.randint(0, 10)
    if result_k <= 4:
        sss = cost * 2
        db_user.balance += sss
        await db_user.save()
        text = (f"Вы выйграли 2X\n"
                    f"Сумма выйгрыша: {sss}$\n"
                    f"Баланс: {db_user.balance}\n$")
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    elif result_k <= 6:
        sss = cost / 2
        db_user.balance += sss
        await db_user.save()
        text = (f"Вы проиграли 0.5\n"
                    f"Сумма проигрыша: {sss}$\n"
                    f"Баланс: {db_user.balance}$\n")
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return
    else:
        sss = 0
        db_user.balance += sss
        await db_user.save()
        text = (f"Вы проиграли все\n"
                    f"Сумма проигрыша: {sss}$\n"
                    f"Баланс: {db_user.balance}$\n"
                )
        await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
        return




