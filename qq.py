import time
from tortoise import Tortoise
from middlewares import NoBotMiddleware, RegistrationMiddleware
import asyncio
from models import User
import config
import re
import requests

async def init_tortoise():
    await Tortoise.init(
        db_url='sqlite://data/db.sqlite3',
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas()

async def main():
    await init_tortoise()
    api_access_token = ''  # токен можно получить здесь https://qiwi.com/api
    my_login = ''
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + api_access_token
    parameters = {'rows': '2'}
    h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + my_login + '/payments', params=parameters)
    json_response = h.json()
    coms = json_response['data'][0]['comment']  # коментарийй
    sums = json_response['data'][0]['sum']['amount']  # сумма
    try:

        text = "".join(c for c in coms if c.isalpha())
        print(text)
        if "VIP" == text:
            if not sums == 50:
                return
            user_id = re.sub('\D', '', coms)
            print(user_id)
            user_db = await User.get(id=user_id)
            if user_db.rank >= 1:
                print("Уже вип")
                return
            else:
                user_db.rank = 1
                await user_db.save()
                print("стал випом")
                return

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    while True:
        asyncio.run(main())
        time.sleep(5)
