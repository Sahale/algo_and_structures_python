"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

def cycle():
    a = int(input('Введите первое число: '))
    a_copy = a
    b = int(input('Введите второе число: '))
    b_copy = b
    sum_a = 0
    sum_b = 0
    buffer = 0
    for i in str(a):
        buffer = a % 10
        sum_a = sum_a + buffer
        a = a // 10
    for i in str(b):
        buffer = b % 10
        sum_b = sum_b + buffer
        b = b // 10
    if sum_a > sum_b:
        print(a_copy, sum_a)
    else:
        print(b_copy, sum_b)

def recursion(a, b, a_copy, b_copy, sum_a, sum_b):
        buffer = 0
        if a > 0:
            buffer = a % 10
            sum_a = sum_a + buffer
            a = a // 10
        if b > 0:
            buffer = b % 10
            sum_b = sum_b + buffer
            b = b // 10
        if a == 0 and b == 0:
            if sum_a > sum_b:
                print(a_copy, sum_a)
                a = int(input('Введите первое число: '))
                a_copy = a
                b = int(input('Введите второе число: '))
                b_copy = b
                sum_a = 0
                sum_b = 0
                recursion(a, b, a_copy, b_copy, sum_a, sum_b)
            else:
                print(b_copy, sum_b)
                a = int(input('Введите первое число: '))
                a_copy = a
                b = int(input('Введите второе число: '))
                b_copy = b
                sum_a = 0
                sum_b = 0
                recursion(a, b, a_copy, b_copy, sum_a, sum_b)
        recursion(a, b, a_copy, b_copy, sum_a, sum_b)


if __name__ == '__main__':
    # cycle()
    a = int(input('Введите первое число: '))
    a_copy = a
    b = int(input('Введите второе число: '))
    b_copy = b
    sum_a = 0
    sum_b = 0
    recursion(a, b, a_copy, b_copy, sum_a, sum_b)