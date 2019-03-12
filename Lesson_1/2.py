# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др.
# над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево на два знака.

a = 5
b = 6

print('Bin a:', bin(a))
print('Bin b:', bin(b))
print('Bitwise AND:', bin(a & b))
print('Bitwise OR:', bin(a | b))
print('Bitwise EXC OR:', bin(a ^ b))
print('Bitwise shift left:', bin(a << 2))
print('Bitwise shift right:', bin(a >> 2))