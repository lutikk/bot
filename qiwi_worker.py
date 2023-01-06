import time
from tortoise import Tortoise
from middlewares import NoBotMiddleware, RegistrationMiddleware
import asyncio
from models import User
import config
from yoomoney import Client



async def init_tortoise():
    await Tortoise.init(
        db_url='sqlite://data/db.sqlite3',
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas()


NoBotMiddleware()
RegistrationMiddleware()
client = Client(config.y_token)
user = client.account_info()


async def main():
    while True:
        try:
            await init_tortoise()
            history = client.operation_history(type="deposition")  # ищем в истории операции с этим кодом
            hui = history.operations[0].__dict__
            tran = hui["operation_id"]
            summa1 = hui["amount"]
            a = summa1 * 100
            b = a / 98
            summa = round(b)
            user_id = hui["label"]
            print(user_id)
            user = await User.get(id=str(user_id))
            lyl1 = user.transaction
            if lyl1 == None:
                lyl = 1
            else:
                lyl = user.transaction

            print(lyl)
            if int(tran) == int(lyl):

                print("не зачислил")
            else:
                user.money += int(summa)
                print("Зачислил")
                user.transaction = tran
                await user.save()

        except Exception as err:
            print(f"Ошибка {err}")



if __name__ == "__main__":
    asyncio.run(main())