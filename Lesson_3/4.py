# 4.	Определить, какое число в массиве встречается чаще всего.
import random


def often():
    length = 10
    a = [random.randrange(1, 5, 1) for _ in range(length)]
    print(a)
    total = 1
    x = a[0]
    for i in range(0, length):
        current = 1
        for j in range(i + 1, length):
            if a[i] == a[j]:
                current += 1
        if current > total:
            total = current
            x = a[i]
    print(x, total)


if __name__ == '__main__':
    often()