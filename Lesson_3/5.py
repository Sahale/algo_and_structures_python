#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
import random


def minel(dig):
    a = [random.randrange(-100, 100, 1) for _ in range(dig)]
    minnum = []
    i = 0
    while i < dig:
        if a[i] < 0:
            minnum.append(a[i])
        i += 1
    print(a)
    print('Число {} на позиции {}'.format(max(minnum), a.index(max(minnum)) + 1))



if __name__ == '__main__':
    num = int(input('Введите число элементов в массиве: '))
    minel(num)
