"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random


def summ(num):
    a = [random.randrange(-100, 100, 1) for _ in range(num)]
    aindexes = sorted((a.index(min(a)), a.index(max(a))))
    print("Сумма равняется {}".format(sum(a[aindexes[0] + 1: aindexes[1]])))


if __name__ == '__main__':
    dig = int(input('Введите число элекментов в массиве: '))
    summ(dig)