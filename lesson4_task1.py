from MyPythonSub import ImportInt
from sys import argv

dictF = [8, 100, 300]

argv.pop(0)

if len(argv) == 0:
  print("Скрипт работает по параметрам пар1 (выработка в часах), пар2 (ставка в час), пар3 (премия)")
else:
    for i in range(len(argv)):
        if i >= len(dictF):
            print("Лишние параметры скошены")
            break
        else:
            FlagInt, IntValue = ImportInt(argv[i])[0], ImportInt(argv[i])[1]
            if FlagInt:
                dictF[i] = IntValue

print(dictF[0] * dictF[1] + dictF[2])
