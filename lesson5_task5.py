from random import randint
from math import fsum

f_path = input("Введите имя файла без расширения") + ".txt"
list_sum = []
for i in range(1, randint(1,100)):
    list_sum.append(randint(1,100))


str_sum = ""
with open(f_path, "w", encoding="UTF-8") as f_obj:
    for el in list_sum:
        str_sum = str_sum + (" " if len(str_sum) != 0 else "") + str(el)
    f_obj.writelines(str_sum)

print(fsum(list_sum))
