"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""


import collections
import os
import cProfile
import timeit


def diff(com, avg):
    more = []
    less = []
    mid = []
    for i in com:
        if com[i].year > avg:
            more.append(com[i].name)
        elif com[i].year < avg:
            less.append(com[i].name)
        else:
            mid.append(com[i].name)
    print('Прибыль больше: ', more)
    print('Прибыль меньше: ', less)
    print('Прибыль равна средней: ', mid)
    main()


def main():
    while True:
        try:
            n = int(input('Введите число компаний: '))
            break
        except ValueError:
            print('Ты чо сучара ты чо')
    com = {}
    total = 0
    for i in range(n):
        name = str(input('Введите название %d компании: ' % (i + 1)))
        i_q1, i_q2, i_q3, i_q4 = input('Введите прибыль компании по кварталам через пробел: ').split()
        info = collections.namedtuple(name, ['name', 'q1', 'q2', 'q3', 'q4', 'year'])
        un_total = int(i_q1) + int(i_q2) + int(i_q3) + int(i_q4)
        com[i] = info(name=name, q1=i_q1, q2=i_q2, q3=i_q3, q4=i_q4, year=un_total)
        total += un_total
    avg = total / n
    diff(com, avg)


if __name__ == '__main__':
    main()
