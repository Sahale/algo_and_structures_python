"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


from memory_profiler import profile


# def cycle():
#     n = int(input('Введите число: '))
#     sum = 0
#     buffer = 0
#     for i in range(1, n + 1):
#         sum += i
#         buffer = n * (n + 1) // 2
#     print('Все хорошо: sum = {}, buffer = {}'.format(sum, buffer))
#
#
# @profile
# def ama_recursion(n, sum, buffer, flag):
#     recursion(n, sum, buffer, flag)
#
#
# def recursion(n, sum, buffer, flag):
#     if n == 0:
#         print('Все хорошо: sum = {}, buffer = {}'.format(sum, buffer))
#     else:
#         sum += n
#         if flag == 0:
#             buffer = n * (n + 1) // 2
#             flag = 1
#         else:
#             pass
#         n -= 1
#         recursion(n, sum, buffer, flag)
#
#
# if __name__ == '__main__':
#     cycle()
#     n = int(input('Введите число: '))
#     sum = 0
#     buffer = 0
#     flag = 0
#     ama_recursion(n, sum, buffer, flag)

import random

@profile
def often():
    length = 10000000
    a = [random.randrange(1, 10000, 1) for _ in range(length)]
    print(a)
    num = max(a, key=a.count)
    print(num)


if __name__ == '__main__':
    often()
