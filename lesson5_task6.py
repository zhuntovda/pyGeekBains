from MyPythonSub import return_exist_path
from MyPythonSub import ImportInt

num_str = "1234567890"
dict_clock = dict()

f_path = return_exist_path()
with open(f_path, "r", encoding="UTF-8") as f_obj:
    for f_str in f_obj.readlines():
        key = ""
        for el in f_str.split():
            if el[len(el) - 1] == ":":
                key = el[:len(el) - 1]
                if not key is dict_clock.keys():
                    dict_clock[key] = 0
            elif key != "":
                str_clock = ""
                for sym in el:
                    if num_str.find(sym) != -1:
                        str_clock = str_clock + sym
                    else:
                        break
                if len(str_clock) != 0:
                    list_el = ImportInt(str_clock)
                    if list_el[0]:
                        dict_clock[key] = dict_clock[key] + list_el[1]
            else:
                print("Нарушение алгоритма!")
                exit()

print(dict_clock)
