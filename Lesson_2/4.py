"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

def cycle():
    n = int(input('Введите число элементов: '))
    sum = 0
    zn = 1
    i = 1
    while i <= n:
        if i == 1:
            sum += zn
            i += 1
        else:
            zn = zn * -0.5
            sum += zn
            i += 1
    print(sum)

def recursion(sum, zn, n, limit):
    if limit == 1:
        print('1')
    else:
        if n == limit:
            print(sum)
        else:
            zn = zn * -0.5
            sum += zn
            n += 1
            recursion(sum, zn, n, limit)

if __name__ == '__main__':
    cycle()
    limit = int(input('Введите число элементов: '))
    sum = 1
    zn = 1
    n = 1
    recursion(sum, zn, n, limit)