import feedparser
from vkbottle.bot import BotLabeler, Message
from utils import get_forward
from models import User

bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text="чат инфо")
async def greetin(message: Message):
    user_db = await User.get(id=message.from_id)
    if user_db.rank >= 3:
        return f"peer_id = {message.peer_id}"


ems = {
    'all': 0,
    'овен': 1,
    'телец': 2,
    'близнецы': 3,
    'рак': 4,
    'лев': 5,
    'дева': 6,
    'весы': 7,
    'скорпион': 8,
    'стрелец': 9,
    'козерог': 10,
    'водолей': 11,
    'рыбы': 12
}


@bl.message(text="гороскоп <a>")
async def greetin(message: Message, a: str):
    pos = ems[a]
    feed = feedparser.parse('http://www.hyrax.ru/cgi-bin/bn_xml.cgi')
    text = feed.entries[pos]['title'] + "\n" + feed.entries[pos]['summary']
    await message.answer(message=text, disable_mentions=1, forward=get_forward(message))
    return

