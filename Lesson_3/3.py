#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.


def minmax():
    a = [8, 3, 15, 6, 4, 2, 8]
    maxi = 0
    mini = 100
    for i in a:
        if i > maxi:
            maxi = i
        elif i < mini:
            mini = i
    a_max = a.index(maxi)
    a_min = a.index(mini)
    a[a_max], a[a_min] = mini, maxi
    print(a)


if __name__ == '__main__':
    # cycle()
    minmax()