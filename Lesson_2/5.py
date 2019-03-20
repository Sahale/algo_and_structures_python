"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

def cycle():
    n = 32
    # '+ 1' чтобы таблица печаталась полностью
    for i in range(((127 - 32) // 10) + 1):
        y = 0
        while y < 10 and n <= 127:
            print('num:', '%3d' % n, chr(n), end='|')
            n += 1
            y += 1
        print()


# Мы будем тут только передавать номер числа
def recursion(num):
    if num <= 127:
        if num % 10 == 2 and num != 32:
            print()
        print('num:', '%3d' % num, chr(num), end='|')
        num += 1
        recursion(num)

if __name__ == '__main__':
    cycle()
    num = 32
    recursion(num)