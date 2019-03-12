# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

a, b, c = input('Введите числа через пробел: ').split()
a, b ,c = float(a), float(b), float(c)

if a > b and a > c:
    if b > c:
        print(b)
    else:
        print(c)
elif b > a and b > c:
    if a > c:
        print(a)
    else:
        print(c)
elif c > a and c > b:
    if a > b:
        print(a)
    else:
        print(b)
else:
    print('Среднего нет!')