"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""

from random import randint

def cycle():
    num = randint(0, 100)
    i = 0
    while i < 10:
        choise = int(input('Введите число: '))
        if choise == num:
            print('Молодец!')
            print('Начинаем заново')
            cycle()
        elif choise < num:
            print('Загаданное больше')
        else:
            print('Загаданное меньше')
        i += 1
    print('Вы проиграли! Начинаем заново...')
    cycle()

def recursion(num, current):
    if current == 10:
        print('Вы проиграли! Начинаем заново...')
        current = 0
        num = randint(0, 100)
        recursion(num, current)
    else:
        choise = int(input('Введите число: '))
        if choise == num:
            print('Молодец!')
            print('Начинаем заново')
            current = 0
            num = randint(0, 100)
            recursion(num, current)
        elif choise < num:
            print('Загаданное больше')
            current += 1
            recursion(num, current)
        else:
            print('Загаданное меньше')
            current += 1
            recursion(num, current)


if __name__ == '__main__':
    # cycle()
    current = 0
    num = randint(0, 100)
    recursion(num, current)