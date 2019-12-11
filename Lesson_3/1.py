# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


def division():
    num = [i for i in range(2, 100)]
    div = [i for i in range(2, 10)]
    for x in div:
        z = 0
        for y in num:
            if y % x == 0:
                z += 1
        print('В диапазоне 2-99 {} цифр кратны {}'.format(z, x))

if __name__ == '__main__':
    # cycle()
    division()