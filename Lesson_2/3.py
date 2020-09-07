"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


def cycle():
    a = int(input('Введите число, которое будет отзеркалировано: '))
    b = str('')
    for i in range(len(str(a))):
        b = b + str(a % 10)
        a = a // 10
    print(b)


def recursion(a, b):
    if a == 0:
        print(b)
    else:
        b = b + str(a % 10)
        a = a // 10
        recursion(a, b)


if __name__ == '__main__':
    # cycle()
    a = int(input('Введите число: '))
    b = str('')
    recursion(a, b)