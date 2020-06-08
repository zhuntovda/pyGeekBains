from itertools import cycle
from itertools import count
from itertools import islice
from MyPythonSub import ImportInt
from sys import argv

if len(argv) != 4:
    print(f"Введено не верное количество аргументов! \n"
          f"Для работы скрипта, нужно три аргумента: \n"
          f"1. Тип обработки (1 - итератор, генерирующий целые числа, 2 - итератор, повторяющий элементы списка) \n"
          f"2. Последовательность, начальное число \n"
          f"3. Количество итераций")
    exit()

FlagInt, TypeOper = ImportInt(argv[1])
if not FlagInt or 0 > TypeOper > 1:
    print("Ошибка 1-ого параметра (не 1 или 2)")
    exit()

if TypeOper == 1:
    FlagInt, ValueIt = ImportInt(argv[2])
    if not FlagInt:
        print("Ошибка 2-ого параметра (для генератора целых чисел, должно быть число)")
        exit()
else:
    ValueIt = argv[2]

FlagInt, NumIt = ImportInt(argv[3])
if not FlagInt:
    print("Ошибка 3-ого параметра (Количество итераций должно быть целым)")
    exit()

if TypeOper == 1:
    for el in islice(count(ValueIt), NumIt):
        print(el)
else:
    for el in islice(cycle(ValueIt), NumIt):
        print(el)
