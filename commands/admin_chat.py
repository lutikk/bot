from vkbottle.bot import BotLabeler, Message
import json
from models import Chat
import vk_api
from config import main_token
from config import get_forward
bl = BotLabeler()
bl.vbml_ignore_case = True




@bl.message(text='+чм')
async def greeting(message: Message):
    adm = ""

    chat_db = await Chat.get(id=message.peer_id)

    if chat_db.activete == "True":
        return "В этом чате уже активирован ЧМ"
    adm_list = json.load(open('admin.json'))


    vk_session = vk_api.VkApi(token=main_token)
    vk = vk_session.get_api()
    ss = vk.messages.getConversationMembers(peer_id=message.peer_id, fields='managers')['items']
    i = 1
    for manager in ss:
        if manager['member_id'] < 0:
            if i == 1:
                nik = await message.get_user(user_ids=message.from_id)
                adm += f"Создатель: [id{nik.id}|{nik.first_name} {nik.last_name}]\n"
                adm_list["admin_5"].append({'id': message.from_id})
            else:
                pass
        else:
            try:
                if manager['is_admin']:
                    if i == 1:
                        qq = manager['member_id']
                        nik = await message.get_user(user_ids=manager['member_id'])
                        adm += f"Создатель: [id{nik.id}|{nik.first_name} {nik.last_name}]\n"
                        adm_list["admin_5"].append({'id': qq})
                    else:
                        qq = manager['member_id']
                        nik = await message.get_user(user_ids=manager['member_id'])
                        adm += f"Администратор: [id{nik.id}|{nik.first_name} {nik.last_name}]\n"
                        adm_list["admin_4"].append({'id': qq})

            except:
                pass
        i += 1

    chat_db.activete = True
    chat_db.admins = adm_list
    await chat_db.save()
    return "OK"

