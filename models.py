from tortoise import Model, fields


class User(Model):
    id = fields.IntField(pk=True)  # вк айди
#    reputation = fields.IntField(default=0)  # репутация
#    reputation_to_give = fields.IntField(default=0)  # репутация на выдачу
#    money = fields.IntField(default=0)  # деньни (наверное ананасики)
    rank = fields.IntField(default=0)  # ранг
    nickname = fields.CharField(max_length=32, null=True)  # Ник максимум 32 символа
    farm_time = fields.IntField(default=80000)  # Время фермы
    transaction = fields.IntField(null=True)  # в душе не ебу
    balance = fields.BigIntField(default=5000)  # Игравой балас
    work = fields.CharField(max_length=256, null=True)  # Бля наверное название работы
    experience = fields.IntField(default=0)  # Опыт работы
    transport = fields.TextField(null=True)  # Наверное машины
    house = fields.TextField(null=True)  # дом (учи английский долбаеб)
    business = fields.TextField(null=True)  # бизнес
    dev_up = fields.CharField(max_length=128, null=True)  # ключик дев ап (не помню нахуй он нужен)
    biz_time = fields.IntField(default=80000)  # Вроде бы последняя работа бизнеса
    brak_zv = fields.CharField(max_length=256, null=True)  # блять браки
    brak = fields.CharField(max_length=256, null=True)  # надо вырезать
    pr_ignor = fields.CharField(max_length=256, null=True)  # что то связанное с игнором
    pr_admin = fields.CharField(max_length=256, null=True)  # вроде как какой админ внес в игнор
    pr_col = fields.IntField(default=0)  # количество раз в игноре
    mobile = fields.CharField(max_length=256, null=True)  # телефон
    pc = fields.CharField(max_length=256, null=True)  # комп
    aircopt = fields.CharField(max_length=256, null=True)  # Что то летающее
    airplane = fields.CharField(max_length=256, null=True)  # что то летающее
    stic = fields.IntField(default=100)  # вроде нужно было для получения стикеров но так как бот без доната то вырежим
    bonys_vip = fields.IntField(default=80000)  # время получения бонуса вип
    bonys = fields.IntField(default=80000)  # время получения бонуса
    bitcoin = fields.IntField(default=0)  # количество биткойнов
    bitcoin_ferm = fields.IntField(default=0)  # количество биткойн ферм
    bitcoin_time = fields.IntField(default=80000)  # последнее время сбора биткойнов
    balanse_time = fields.IntField(default=80000)
    perevod_limit = fields.IntField(default=0)


    @classmethod
    async def get_or_new(cls, **kwargs) -> "User":
        user, _ = await cls.get_or_create(**kwargs)
        return user
