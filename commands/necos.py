import json
import random
import typing as ty

import aiohttp
from pydantic import BaseModel, Field
from vkbottle import API
from vkbottle.bot import BotLabeler, Message

bl = BotLabeler()
bl.vbml_ignore_case = True


class OperatorModelRange(BaseModel):
    min_number: int = Field(default_factory=int, alias='min')
    max_number: int = Field(default_factory=int, alias='max')

    def __str__(self) -> str:
        return f"{self.min_number}-{self.max_number}"


class OperatorModel(BaseModel):
    code: int = Field(default_factory=int)
    range: OperatorModelRange
    region: str
    operator: str
    time: str


class OperatorModelList(BaseModel):
    operators: ty.List[OperatorModel]

    def get_model(self, code: int, in_range: int) -> ty.Optional[OperatorModel]:
        filtered_by_code = [model for model in self.operators if model.code == code]
        for model in filtered_by_code:
            if model.range.min_number < in_range < model.range.max_number:
                return model

    def parse_number(self, number: str) -> ty.Tuple[str, ty.Optional[OperatorModel]]:
        number = number.replace('-', '')
        if len(number) == 12 and "+" in number and "7" in number:
            normalized_number = number[1:]
        elif len(number) == 11 and (number[0] == "7" or number[0] == "8"):
            normalized_number = '7' + number[1:]
        elif len(number) == 10:
            normalized_number = '7' + number
        else:
            return number, None

        try:
            list(int(s) for s in normalized_number)
        except:
            return normalized_number, None

        code = int(normalized_number[1:4])
        in_range = int(normalized_number[4:])
        return normalized_number, self.get_model(code, in_range)


with open('operators.json', 'r', encoding='utf-8') as file:
    OPERATORS = OperatorModelList.parse_raw(file.read())


@bl.message(text="номер <number>")
async def greeting(message: Message, number: str):
    device_id = ""
    number, model = OPERATORS.parse_number(number)
    profile_text = ""
    try:
        vk_me_api = API(
            token='',
            requests_session=aiohttp.ClientSession(
                raise_for_status=True,
                headers={
                    "User-Agent": "VKAndroidApp/7.0-9912 (Android 11; SDK 30; arm64-v8a; "
                                  "Xiaomi M2003J15SC; ru; 2340x1080)"
                }
            )
        )
        await vk_me_api.method(
            "account.resetMessagesContacts",
            device_id=device_id
        )
        cont_res = await vk_me_api.method(
            "account.importMessagesContacts",
            contacts=json.dumps([{
                "device_local_id": random.randint(1, 999999),
                "name": f"Search Subject {number}",
                "is_favorite": False,
                "phones": [number],
                "emails": []
            }]),
            device_id=device_id,
            fields="first_name,first_name_acc,first_name_gen,last_name,last_name_acc,last_name_gen,"
                   "screen_name,photo_50,"
                   "photo_100,photo_200,photo_400,sex,verified,domain,blacklisted,blacklisted_by_me,country,city,"
                   "occupation,online_info,can_call,is_service,friend_status,contacts,is_messages_blocked,"
                   "can_invite_to_chats,emoji_status,image_status,bdate,can_write",
            extended=1
        )

        profile = cont_res['profiles'][0]

        profile_text = f"👤 Профиль ВК: [id{profile['id']}|{profile['first_name']} {profile['last_name']}]"
    except:
        pass

    if not model and not profile_text:
        return "⚠ Не удалось определить номер"

    response = ""

    if model:
        response += (
            f"🆔 Номер телефона: {number}\n"
            f"👥 Оператор: {model.operator}\n"
            f"🗺️ Регион: {model.region}\n"
            f"🔗 Диапазон: {model.range}\n"
            f"🕐 Регистрация: {model.time}\n"
        )
    if profile_text:
        response += f"\n{profile_text}"
    return response
