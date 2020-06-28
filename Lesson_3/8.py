"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

import random


def matrix(manmat1, manmat2, manmat3, manmat4, manmat5):
    manmat1.append(sum(manmat1))
    print(manmat1)
    manmat2.append(sum(manmat2))
    print(manmat2)
    manmat3.append(sum(manmat3))
    print(manmat3)
    manmat4.append(sum(manmat4))
    print(manmat4)
    manmat5.append(sum(manmat5))
    print(manmat5)


if __name__ == '__main__':
    manmat1 = list(map(int, input('Введите первую строчку матрицы: ').strip().split()))[:3]
    manmat1.append(random.randrange(-1000, 1000, 1))
    manmat2 = list(map(int, input('Введите вторую строчку матрицы: ').strip().split()))[:3]
    manmat2.append(random.randrange(-1000, 1000, 1))
    manmat3 = list(map(int, input('Введите третью строчку матрицы: ').strip().split()))[:3]
    manmat3.append(random.randrange(-1000, 1000, 1))
    manmat4 = list(map(int, input('Введите четвёртую строчку матрицы: ').strip().split()))[:3]
    manmat4.append(random.randrange(-1000, 1000, 1))
    manmat5 = list(map(int, input('Введите пятую строчку матрицы: ').strip().split()))[:3]
    manmat5.append(random.randrange(-1000, 1000, 1))
    matrix(manmat1, manmat2, manmat3, manmat4, manmat5)
