from MyPythonSub import InputIntList

listNum = InputIntList("Найдем не повторяющиеся числа")

print([el for el in listNum if listNum.count(el) == 1])