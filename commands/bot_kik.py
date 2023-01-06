from vkbottle.bot import BotLabeler, Message

from models import User
from utils import get_forward, search_user_ids

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text='кик')
async def bot_kik1(message: Message):
    db_user = await User.get(id=message.from_id)
    if db_user.rank >= 6:
        await message.ctx_api.messages.remove_chat_user(message.chat_id, message.reply_message.from_id)
        return
    if db_user.rank >= 4:
        db_replai = await User.get(id=message.reply_message.from_id)
        if db_replai.rank >= 3:
            await message.answer(message="Куда на своих?", disable_mentions=1, forward=get_forward(message))
            return
        else:
            await message.ctx_api.messages.remove_chat_user(message.chat_id, message.reply_message.from_id)


@bl.message(text="кик <vk_user_id>")
async def kik_bot(message: Message, vk_user_id: str, **kwargs):
    user_ids = search_user_ids(vk_user_id)
    db_user = await User.get(id=message.from_id)
    if db_user.rank >= 6:
        for user_id in user_ids:
            await message.ctx_api.messages.remove_chat_user(message.chat_id, user_id)
    if db_user.rank >= 4:
        db_replai = await User.get(id=vk_user_id)

        if db_replai.rank >= 3:
            await message.answer(message="Куда на своих?", disable_mentions=1, forward=get_forward(message))
            return
        else:
            for user_id in user_ids:
                await message.ctx_api.messages.remove_chat_user(message.chat_id, user_id)
