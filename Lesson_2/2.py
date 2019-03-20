"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

# Отсутствует обработка для случая, если пользователь ввел не число

def cycle():
    while True:
        a = str(input('Введите число: '))
        even = 0
        odd = 0
        for i in a:
            if int(i) % 2 == 0:
                even += int(i)
            else:
                odd += int(i)
        print('Сумма четных:', even)
        print('Сумма нечетных:', odd)


# Понимание пришло не сразу...(
def recursion(digit, even, odd):
    check = digit % 10
    if digit == 0:
        print('Четное:', even)
        print('Нечетное', odd)
        digit = int(input('Введите число: '))
        recursion(digit, even = 0, odd = 0)
    elif check % 2 == 0:
        even += check
        recursion(digit // 10, even, odd)
    else:
        odd += check
        recursion(digit // 10, even, odd)

if __name__ == '__main__':
    # cycle()
    dig = int(input('Введите число: '))
    even = 0
    odd = 0
    recursion(dig, even, odd)