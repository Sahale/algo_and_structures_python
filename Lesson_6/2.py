"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""
from pympler import asizeof

class NoSlots:
    def __init__(self, num, data):
        self.tracknum = num
        self.qata = data


class Slots:
    __slots__ = ['num', 'data']

    def __init__(self, num, data):
        self.tracknum = num
        self.data = data


numone = NoSlots('1', 'Data')
numtwo = Slots('2', 'Data')

print(numone.__dict__)
print(numtwo.tracknum)

print(asizeof.asizeof(numone))
print(asizeof.asizeof(numtwo))