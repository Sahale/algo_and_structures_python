# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random


rows = 5
columns = 4


def minc(matrix):
    minimalcol = []
    for i in range(columns):
        minim = []
        for j in range(rows):
            minim.append(matrix[j][i])
        minimalcol.append(min(minim))
    print(minimalcol)
    print(max(minimalcol))

    # for i in rows:
    #     for j in columns:
    #         minim.append(min)
    # print(minim)


if __name__ == '__main__':
    matrix = [[random.randrange(-10, 10, 1) for j in range(columns)] for i in range(rows)]
    print(matrix)
    minc(matrix)
