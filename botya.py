import sqlite3

import vk
import vk_api

from config import user_token

log = 609627697
db = sqlite3.connect('xyin.db')
sql = db.cursor()

vk = vk_api.VkApi(token=user_token)
def_ap_cay = 'ddc68d6af3cb36a2ae1ffdfc41629b25'

sql.execute("""CREATE TABLE IF NOT EXISTS user(
    vk_id INT,
    rep INT,
    mani INT,
    rang INT,
    rep_d INT
)""")

db.commit()

QIWI_PRIV_KEY = ""


def zap(vk_id_lol):
    sas = 'нет'
    user = vk.method("users.get", {"user_ids": vk_id_lol})  # вместо 1 подставляете айди нужного юзера
    nikk = user[0]['first_name'] + ' ' + user[0]['last_name']
    sql.execute("SELECT vk_id FROM user")
    sql.execute(f"INSERT INTO user VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (vk_id_lol, nikk, 0, 0, 0, 0, 86400, 1, 5000, sas, 0, sas, sas, sas, sas))
    db.commit()


def prov(user_id):
    sql.execute(f"SELECT vk_id FROM user WHERE vk_id = '{user_id}'")
    if sql.fetchone() is None:
        return True


def prov_nik(n):
    sql.execute(f"SELECT vk_id FROM user WHERE n = '{n}'")
    if not sql.fetchone() is None:
        return True


def on(vki):
    sas = 'нет'
    sql.execute(
        f"UPDATE user SET n = '{sas}', rep = '{0}', mani = '{0}', rang = '{0}', rep_d = '{0}', time_ferm = '{86400}', ig_mani = '{5000}', rabota = '{sas}', opt = '{0}', transport = '{sas}', dom = '{sas}', biznes = '{sas}' WHERE vk_id = '{vki}'")
    db.commit()


# -1 игнор
# 0 юзер
# 1 вип
# 2 тестер
# 3 разраб
# 4 агент
# 5 админ
# 6 владелец
def mani(user_id, mani):
    sql.execute(f'SELECT mani FROM user WHERE vk_id = {user_id}')

    ma1 = sql.fetchmany()
    ma = ma1[0][0]

    lyl = int(ma) + int(mani)
    sql.execute(f"UPDATE user SET mani = {lyl} WHERE vk_id = {user_id}")
    db.commit()


def manii(user_id, mani):
    ma = 1
    sql.execute(f'SELECT mani FROM user WHERE vk_id = {user_id}')
    ma1 = sql.fetchmany()
    ma = ma1[0][0]
    print(ma)
    lyl = int(ma) - int(mani)
    sql.execute(f"UPDATE user SET mani = {lyl} WHERE vk_id = {user_id}")
    db.commit()


def manii_ig(user_id, mani):
    ma = 1
    sql.execute(f'SELECT ig_mani FROM user WHERE vk_id = {user_id}')
    ma1 = sql.fetchmany()
    ma = ma1[0][0]
    print(ma)
    lyl = float(ma) - float(mani)
    sql.execute(f"UPDATE user SET ig_mani = {lyl} WHERE vk_id = {user_id}")
    db.commit()


def mani_ig(user_id, mani):
    ma = 1
    sql.execute(f'SELECT ig_mani FROM user WHERE vk_id = {user_id}')
    ma1 = sql.fetchmany()
    ma = ma1[0][0]
    print(ma)
    lyl = float(ma) + float(mani)
    sql.execute(f"UPDATE user SET ig_mani = {lyl} WHERE vk_id = {user_id}")
    db.commit()


def ferma_an(lyl, user_id, opt, mani):
    sql.execute(f'SELECT opt FROM user WHERE vk_id = {user_id}')
    ma1 = sql.fetchmany()
    ma = ma1[0][0]
    opt_t = int(ma) + int(opt)

    sql.execute(f'SELECT ig_mani FROM user WHERE vk_id = {user_id}')
    ma1 = sql.fetchmany()
    ma = ma1[0][0]
    ly = int(ma) + int(mani)
    sql.execute(f"UPDATE user SET time_ferm = {lyl}, opt = {opt_t}, ig_mani = {ly} WHERE vk_id = {user_id}")
    db.commit()


def imus(user_id, lyl):
    sql.execute(f"UPDATE user SET transport = '{lyl}' WHERE vk_id = {user_id}")
    db.commit()


def dev(user_id, lyl):
    sql.execute(f"UPDATE user SET dev_ap = '{lyl}' WHERE vk_id = {user_id}")
    db.commit()


def imus_ned(user_id, lyl):
    sql.execute(f"UPDATE user SET dom = '{lyl}' WHERE vk_id = {user_id}")
    db.commit()


def zvd_v(user_id, mani):
    sql.execute(f'SELECT rep_d FROM user WHERE vk_id = {user_id}')
    ma1 = sql.fetchmany()
    ma = ma1[0][0]
    lyl = int(ma) + int(mani)

    sql.execute(f"UPDATE user SET rep_d = {lyl} WHERE vk_id = {user_id}")
    db.commit()


def zvd(user_id, mani):
    sql.execute(f'SELECT rep FROM user WHERE vk_id = {user_id}')
    ma1 = sql.fetchmany()
    ma = ma1[0][0]
    lyl = int(ma) + int(mani)
    sql.execute(f"UPDATE user SET rep = {lyl} WHERE vk_id = {user_id}")
    db.commit()


def zv_user(user_id, mani):
    sql.execute(f'SELECT rep_d FROM user WHERE vk_id = {user_id}')
    ma1 = sql.fetchmany()
    ma = ma1[0][0]
    lyl = int(ma) - int(mani)
    sql.execute(f"UPDATE user SET rep_d = {lyl} WHERE vk_id = {user_id}")
    db.commit()


def zv_user1(user_id1, mani):
    sql.execute(f'SELECT rep FROM user WHERE vk_id = {user_id1}')
    ma1 = sql.fetchmany()
    maiii = ma1[0][0]
    l = int(maiii) + int(mani)
    sql.execute(f"UPDATE user SET rep = {l} WHERE vk_id = {user_id1}")
    db.commit()


def nikk(user_id, zv):
    print(zv)

    sql.execute(f"UPDATE user SET n = '{zv}'  WHERE vk_id = {user_id}")
    db.commit()


def rabota(user_id, zv):
    print(zv)

    sql.execute(f"UPDATE user SET rabota = '{zv}'  WHERE vk_id = {user_id}")
    db.commit()


def vl(user_id):
    sql.execute(f'SELECT rang FROM user WHERE vk_id = {user_id}')
    ma1 = sql.fetchmany()
    a = ma1[0][0]
    # ебать ты не поверишь о это работает :)))
    if 10 < int(a):
        return True
    elif 10 == int(a):
        return True


def admin(user_id):
    sql.execute(f'SELECT rang FROM user WHERE vk_id = {user_id}')
    ma1 = sql.fetchmany()
    a = ma1[0][0]
    # ебать ты не поверишь о это работает :)))
    if 5 < int(a):
        return True
    elif 5 == int(a):
        return True


def agent(user_id):
    sql.execute(f'SELECT rang FROM user WHERE vk_id = {user_id}')
    ma1 = sql.fetchmany()
    a = ma1[0][0]
    # ебать ты не поверишь о это работает :)))
    if 4 < int(a):
        return True
    elif 4 == int(a):
        return True


def razrab(user_id):
    sql.execute(f'SELECT rang FROM user WHERE vk_id = {user_id}')
    ma1 = sql.fetchmany()
    a = ma1[0][0]
    # ебать ты не поверишь о это работает :)))
    if 3 < int(a):
        return True
    elif 3 == int(a):
        return True


def tester(user_id):
    sql.execute(f'SELECT rang FROM user WHERE vk_id = {user_id}')
    ma1 = sql.fetchmany()
    a = ma1[0][0]
    # ебать ты не поверишь о это работает :)))
    if 2 < int(a):
        return True
    elif 2 == int(a):
        return True


def vip(user_id):
    sql.execute(f'SELECT rang FROM user WHERE vk_id = {user_id}')
    ma1 = sql.fetchmany()
    a = ma1[0][0]
    # ебать ты не поверишь о это работает :)))
    if 1 < int(a):
        return True
    elif 1 == int(a):
        return True


def user(user_id):
    sql.execute(f'SELECT rang FROM user WHERE vk_id = {user_id}')
    ma1 = sql.fetchmany()
    a = ma1[0][0]
    # ебать ты не поверишь о это работает :)))
    if 0 < int(a):
        return True
    elif 0 == int(a):
        return True


def rang(user_id, zv):
    sql.execute(f"UPDATE user SET rang = {zv} WHERE vk_id = {user_id}")
    db.commit()
    return True


def ignor(user_id):
    sql.execute(f'SELECT rang FROM user WHERE vk_id = {user_id}')
    ma1 = sql.fetchmany()
    a = ma1[0][0]
    # ебать ты не поверишь о это работает :)))
    if -1 < int(a):
        return True
    elif -1 == int(a):
        return True
