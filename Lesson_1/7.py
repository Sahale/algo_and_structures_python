"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""

a, b, c = (input('Введите через пробел значения длин отрезков: ').split())
a, b, c = float(a), float(b), float(c)

if a + b > c and a + c > b and b + c > a:
    if a == b and a == c:
        print('Треугольник существует, равносторонний')
    elif a == b or a == c or b == c:
        print('Треугольник существует, равнобедренный')
    else:
        print('Треугольник существует, разносторонний')
else:
    print('Не существует')
