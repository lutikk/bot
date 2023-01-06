import json
import os
import time
from os.path import join
from random import randint


def main():
    dirik = os.getcwd()
    bit = json.load(open('bit.json'))
    s = randint(1, 2)
    if s == 1:
        print(1)
        qq = randint(1, 1000)
        bit['bitc'] += qq
        bit['bitc_pr'] += qq
        if bit['bitc'] >= 15500:
            bit['bitc'] = 15500
            bit['bitc_pr'] = 15000
        else:
            pass
        with open(join(dirik, f'bit.json'), 'w') as f:
            f.write(json.dumps(bit, ensure_ascii=False, indent=2))
    elif s == 2:
        print(2)
        qq = randint(1, 300)
        bit['bitc'] -= qq
        bit['bitc_pr'] -= qq
        if bit['bitc'] <= 5500:
            bit['bitc'] = 5500
            bit['bitc_pr'] = 5000
        else:
            pass
        with open(join(dirik, f'bit.json'), 'w') as f:
            f.write(json.dumps(bit, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    while True:
        main()
        time.sleep(60)
