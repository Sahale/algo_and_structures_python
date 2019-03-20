"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""

def cycle():
    a = int(input('Введите число: '))
    b = int(input('Введите искомое: '))
    count = 0
    for i in range(len(str(a))):
        buffer = a % 10
        if buffer == b:
            count += 1
        a = a // 10
    print(count)

def recursion(digit, search, count):
    if len(str(digit)) == 1:
        buffer = digit % 10
        if buffer == search:
            count += 1
        print(count)
        digit = int(input('Введите число: '))
        search = int(input('Введите искомое: '))
        count = 0
        recursion(digit, search, count)
    else:
        buffer = digit % 10
        if buffer == search:
            count += 1
        digit = digit // 10
        recursion(digit, search, count)


if __name__ == '__main__':
    # cycle()
    digit = int(input('Введите число: '))
    search = int(input('Введите искомое: '))
    count = 0
    recursion(digit, search, count)