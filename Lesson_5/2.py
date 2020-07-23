"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

import collections


def summ(he1, he2, hexlib, hexlibrev):
    sd = collections.deque()
    shift = 0
    mark = 0
    if len(he1) == len(he2):
        for i in range(len(he1)):
            sd1 = hexlib.get(he1.pop())
            sd2 = hexlib.get(he2.pop())
            sdtemp = sd1 + sd2
            if he1:
                pass
            else:
                mark = 1
                if sdtemp > 15 and i == 0:
                    shift = 1
            if mark == 0:
                if shift == 1:
                    if ((sdtemp % 16) + 1) == 16:
                        sd.appendleft(str(0))
                    else:
                        sd.appendleft(str(hexlibrev.get((sdtemp % 16) + 1)))
                else:
                    sd.appendleft(str(hexlibrev.get(sdtemp % 16)))
            else:
                if shift == 1:
                    if ((sdtemp % 16) + 1) == 16:
                        sd.appendleft(str(0))
                        sd.appendleft(str(1))
                    else:
                        sd.appendleft(str(hexlibrev.get((sdtemp % 16) + 1)))
                        sd.appendleft(str(1))
                else:
                    sd.appendleft(str(hexlibrev.get(sdtemp % 16)))
            if sdtemp > 15:
                shift = 1
            else:
                shift = 0
    if len(he2) > len(he1):
        he3 = he2
        he2 = he1
        he1 = he3
    for i in range(len(he1)):
        sd1 = hexlib.get(he1.pop())
        try:
            sd2 = hexlib.get(he2.pop())
        except IndexError:
            sd2 = 0
            mark = 1
        sdtemp = sd1 + sd2
        if mark == 0:
            if shift == 1:
                if ((sdtemp % 16) + 1) == 16:
                    sd.appendleft(str(0))
                else:
                    sd.appendleft(str(hexlibrev.get((sdtemp % 16) + 1)))
            else:
                sd.appendleft(str(hexlibrev.get(sdtemp % 16)))
        else:
            if shift == 1:
                if ((sdtemp % 16) + 1) == 16:
                    sd.appendleft(str(0))
                    sd.appendleft(str(1))
                else:
                    sd.appendleft(str(hexlibrev.get((sdtemp % 16) + 1)))
                    sd.appendleft(str(1))
            else:
                sd.appendleft(str(hexlibrev.get(sdtemp % 16)))
        if sdtemp > 15:
            shift = 1
        else:
            shift = 0
    return sd


def multi(hex1, hex2):
    return format((int(''.join(hex1), 16) * int(''.join(hex2), 16)), 'x').upper()


def main():
    hexlib = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    hexlibrev = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    }
    he1 = collections.deque(input('Введите первое шестнадцатиричное число: '))
    he2 = collections.deque(input('Введите второе шестнадцатиричное число: '))
    hex1 = he1.copy()
    hex2 = he2.copy()
    print('Сумма равняется: ' + ''.join(summ(he1, he2, hexlib, hexlibrev)))
    print('Произведение равняется: ' + multi(hex1, hex2))
    main()


if __name__ == '__main__':
    main()