from dev_up import DevUpAPI
from typing import Union, Iterable
from config import def_ap_cay

def join(data: Union[str, Iterable], separator: str = ",") -> str:
    if isinstance(data, str):
        data = [data]
    if not data:
        return ''
    return separator.join([str(obj) for obj in data])

def sticer(def_ap_cay, vk_user):
    api = DevUpAPI(def_ap_cay)
    stickers = api.vk.get_stickers(vk_user).response
    text = f"📄 Пользователь (имя сам определяй через user.get) " \
           f"имеет {stickers.count} стикеров из {stickers.count_all}\n" \
           f"💰 Стоимость в голосах: {stickers.price.votes}\n" \
           f"💵 Стоимость в рублях: {stickers.price.rub}₽\n\n"
    text_stickers = []
    for sticker in stickers.stickers:
        text_stickers += [f"{sticker.name}"]

    ss = text + join(text_stickers, ", ")
    print(ss)


if __name__ == "__main__":
    print(sticer(def_ap_cay=def_ap_cay, vk_user=1))
