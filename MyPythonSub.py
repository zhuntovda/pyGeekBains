def ImportInt(Value):
    try:
        return True, int(Value)
    except ValueError:
        print(f"Не верный формат данных! Значение {Value} не может быть приобразовано к целочисленному!")
        return False, Value

def InputIntList(PrintStr = "Добро пожаловать"):

    print(PrintStr)

    listNum = input("Введите список целых чисел через пробел: ")
    listNum = listNum.split()

    sort_list = []

    if len(listNum) != 0:
        for el in listNum:
            FlagInt, ValueInt = ImportInt(el)
            if FlagInt:
                sort_list.append(ValueInt)

    return sort_list