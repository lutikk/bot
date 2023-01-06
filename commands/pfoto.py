import random
from random import randint

from vk_api import VkApiError
from vkbottle import PhotoMessageUploader
from vkbottle.api import API
from vkbottle.bot import Bot
from vkbottle.bot import BotLabeler, Message

import config
from config import ALBUMS, GROUP_ID, user_token
from models import User

bl = BotLabeler()
bl.vbml_ignore_case = True
bot = Bot(config.main_token)
a = randint(0, 46)
api = API(user_token[a])
photo_uploader = PhotoMessageUploader(bot.api, generate_attachment_strings=True)


@bl.message(text=["Аниме", "аниме"])
async def photo_random(message: Message):
    albom_gp = GROUP_ID[0]
    albom = ALBUMS[0]
    if 1 == 1:
        try:
            info_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=0)
            data_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=15,
                                              offset=random.randint(0, info_album.count))
            random_item = random.choice(data_album.items)
            await message.answer(attachment=f'photo{albom_gp}_{random_item.id}')
            return
        except VkApiError:
            info_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=0)
            data_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=15,
                                              offset=random.randint(0, info_album.count))
            random_item = random.choice(data_album.items)
            await message.answer(attachment=f'photo{albom_gp}_{random_item.id}')
            return


@bl.message(text="сохра")
async def photo_random(message: Message):
    albom_gp = GROUP_ID[0]
    albom = ALBUMS[1]
    if 1 == 1:
        try:
            info_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=0)
            data_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=15,
                                              offset=random.randint(0, info_album.count))
            random_item = random.choice(data_album.items)
            await message.answer(attachment=f'photo{albom_gp}_{random_item.id}')
            return
        except VkApiError:
            info_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=0)
            data_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=15,
                                              offset=random.randint(0, info_album.count))
            random_item = random.choice(data_album.items)
            await message.answer(attachment=f'photo{albom_gp}_{random_item.id}')
            return


@bl.message(text="сохра вип")
async def photo_random(message: Message):
    albom_gp = GROUP_ID[0]
    albom = ALBUMS[2]
    user_db = await User.get(id=message.from_id)
    if user_db.rank >= 1:
        try:
            info_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=0)
            data_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=15,
                                              offset=random.randint(0, info_album.count))
            random_item = random.choice(data_album.items)
            await message.answer(attachment=f'photo{albom_gp}_{random_item.id}')
            return
        except VkApiError:
            info_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=0)
            data_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=15,
                                              offset=random.randint(0, info_album.count))
            random_item = random.choice(data_album.items)
            await message.answer(attachment=f'photo{albom_gp}_{random_item.id}')
            return


@bl.message(text="интим")
async def photo_random(message: Message):
    albom_gp = GROUP_ID[0]
    albom = ALBUMS[3]
    user_db = await User.get(id=message.from_id)
    if user_db.rank >= 1:
        try:
            info_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=0)
            data_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=15,
                                              offset=random.randint(0, info_album.count))
            random_item = random.choice(data_album.items)
            await message.answer(attachment=f'photo{albom_gp}_{random_item.id}')
            return
        except VkApiError:
            info_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=0)
            data_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=15,
                                              offset=random.randint(0, info_album.count))
            random_item = random.choice(data_album.items)
            await message.answer(attachment=f'photo{albom_gp}_{random_item.id}')
            return


@bl.message(text="сигны группы")
async def photo_random(message: Message):
    albom_gp = GROUP_ID[0]
    albom = ALBUMS[4]

    if 1 == 1:
        try:
            info_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=0)
            data_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=15,
                                              offset=random.randint(0, info_album.count))
            random_item = random.choice(data_album.items)
            await message.answer(attachment=f'photo{albom_gp}_{random_item.id}')
            return
        except VkApiError:
            info_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=0)
            data_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=15,
                                              offset=random.randint(0, info_album.count))
            random_item = random.choice(data_album.items)
            await message.answer(attachment=f'photo{albom_gp}_{random_item.id}')
            return


@bl.message(text="жопы группы")
async def photo_random(message: Message):
    albom_gp = GROUP_ID[0]
    albom = ALBUMS[5]

    if 1 == 1:
        try:
            info_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=0)
            data_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=15,
                                              offset=random.randint(0, info_album.count))
            random_item = random.choice(data_album.items)
            await message.answer(attachment=f'photo{albom_gp}_{random_item.id}')
            return
        except VkApiError:
            info_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=0)
            data_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=15,
                                              offset=random.randint(0, info_album.count))
            random_item = random.choice(data_album.items)
            await message.answer(attachment=f'photo{albom_gp}_{random_item.id}')
            return


@bl.message(text="дай котика")
async def photo_random(message: Message):
    albom_gp = GROUP_ID[0]
    albom = ALBUMS[6]

    if 1 == 1:
        try:
            info_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=0)
            data_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=15,
                                              offset=random.randint(0, info_album.count))
            random_item = random.choice(data_album.items)
            await message.answer(attachment=f'photo{albom_gp}_{random_item.id}')
            return
        except VkApiError:
            info_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=0)
            data_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=15,
                                              offset=random.randint(0, info_album.count))
            random_item = random.choice(data_album.items)
            await message.answer(attachment=f'photo{albom_gp}_{random_item.id}')
            return


@bl.message(text="пикча")
async def photo_random(message: Message):
    albom_gp = GROUP_ID[0]
    albom = ALBUMS[7]

    if 1 == 1:
        try:
            info_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=0)
            data_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=15,
                                              offset=random.randint(0, info_album.count))
            random_item = random.choice(data_album.items)
            await message.answer(attachment=f'photo{albom_gp}_{random_item.id}')
            return
        except VkApiError:
            info_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=0)
            data_album = await api.photos.get(owner_id=albom_gp, album_id=albom, count=15,
                                              offset=random.randint(0, info_album.count))
            random_item = random.choice(data_album.items)
            await message.answer(attachment=f'photo{albom_gp}_{random_item.id}')
            return
