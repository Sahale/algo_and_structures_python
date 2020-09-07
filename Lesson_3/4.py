# 4.	Определить, какое число в массиве встречается чаще всего.
import random


def often():
    length = 10
    a = [random.randrange(1, 5, 1) for _ in range(length)]
    print(a)
    num = max(a, key=a.count)
    print(num)


if __name__ == '__main__':
    often()
