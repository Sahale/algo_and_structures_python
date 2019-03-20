"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""

def cycle():
    n = int(input('Введите число: '))
    sum = 0
    buffer = 0
    for i in range(1, n + 1):
        sum += i
        buffer = n * (n + 1) // 2
    print('Все хорошо: sum = {}, buffer = {}'.format(sum, buffer))

def recursion(n, sum, buffer, flag):
    if n == 0:
        print('Все хорошо: sum = {}, buffer = {}'.format(sum, buffer))
    else:
        sum += n
        if flag == 0:
            buffer = n * (n + 1) // 2
            flag = 1
        else:
            pass
        n -= 1
        recursion(n, sum, buffer, flag)


if __name__ == '__main__':
    cycle()
    n = int(input('Введите число: '))
    sum = 0
    buffer = 0
    flag = 0
    recursion(n, sum, buffer, flag)