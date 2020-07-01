"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import timeit
import cProfile


def resh(num):
    n = 10000
    sieve = [x for x in range(n)]
    sieve[1] = 0    # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return [p for p in sieve if p != 0][num - 1]


def notresh(el):
    n = 10000
    l = [i for i in range(n)]
    fin = []
    for i in l:
        j = 2
        x = 0
        if i == 0 or i == 1:
            continue    # без этой строки итоговый список будет содержать ноль и единицу
        while j < i:
            if l[i] % l[j] == 0:
                x = 1
            j += 1
        if x == 0:
            fin.append(l[i])
        i += 1
        if len(fin) == el:
            return fin[el - 1]


def main():
    try:
        el = int(input('Введите i-ый элемент: '))
    except ValueError:
        print('Ты пидор')
        main()
    print(resh(el))
    print(notresh(el))
    print(timeit.timeit('resh(161)', setup='from __main__ import resh', number=1000))
    print(timeit.timeit('notresh(161)', setup='from __main__ import notresh', number=1000))
    cProfile.run('resh(161)')
    cProfile.run('notresh(161)')


if __name__ == '__main__':
    main()

