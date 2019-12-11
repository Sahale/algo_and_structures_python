"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
import random


def searchmin(len):
    a = [random.randrange(-100, 100, 1) for _ in range(len)]
    x2 = 1000
    x1 = min(a)
    for j in range(0, len):
        if a[j] < x2 and j != a.index(x1):
            x2 = a[j]
        j += 1
    print(a, x1, x2)


if __name__ == '__main__':
    dig = int(input('Введи длину массива: '))
    searchmin(dig)