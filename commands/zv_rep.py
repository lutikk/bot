from vkbottle.bot import BotLabeler, Message

from models import User

bl = BotLabeler()
bl.vbml_ignore_case = True


async def zv_user(user_id, mani):
    user = await User.get(id=user_id)
    a = user.reputation_to_give
    s = int(a) - int(mani)
    user.reputation_to_give = s
    await user.save()


async def zv_user1(user_id1, mani):
    user = await User.get(id=user_id1)
    a = user.reputation
    s = int(a) + int(mani)
    user.reputation = s
    await user.save()


@bl.message(text=["*<b>"])
async def greeting(message: Message, b: str):
    lol = message.from_id
    kek = message.reply_message.from_id
    user_db = await User.get(id=lol)
    user_rep = await User.get(id=kek)
    if user_db.rank >= 4:
        c = b.count("*")
        a = int(c) + 1
        if lol == kek:
            return "Жулик! Не голосуй!"
        ma = user_db.reputation_to_give
        if int(ma) == int(a):
            await zv_user(user_id=lol, mani=a)
            await zv_user1(user_id1=kek, mani=a)

            mal = user_rep.reputation + int(a)
            return "✨ Уважение оказано " + str(a) + "\n Репутация: " + str(mal) + " звёздочки"
        elif int(ma) > int(a):
            await zv_user(user_id=lol, mani=a)
            await zv_user1(user_id1=kek, mani=a)

            mal = user_rep.reputation + int(a)
            return "✨ Уважение оказано " + str(a) + "\n Репутация: " + str(mal) + " звёздочки"
    if user_db.rank >= 2:
        return "Ты не можешь выдавать звёзды"
    elif user_db.rank >= 0:

        c = b.count("*")
        a = int(c) + 1
        if lol == kek:
            return "Жулик! Не голосуй!"
        ma = user_db.reputation_to_give
        if int(ma) == int(a):
            await zv_user(user_id=lol, mani=a)
            await zv_user1(user_id1=kek, mani=a)

            mal = user_rep.reputation + int(a)
            return "✨ Уважение оказано " + str(a) + "\n Репутация: " + str(mal) + " звёздочки"
        elif int(ma) > int(a):
            await zv_user(user_id=lol, mani=a)
            await zv_user1(user_id1=kek, mani=a)

            mal = user_rep.reputation + int(a)
            return "✨ Уважение оказано " + str(a) + "\n Репутация: " + str(mal) + " звёздочки"
