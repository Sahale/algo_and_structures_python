# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

dig = int(input('Введите трехзначное число: '))

a = dig // 100
b = dig // 10 % 10
c = dig % 10

# Здесь
print('Сумма равна:', (a + b + c))
print('Произведение равно:', (a * b * c))