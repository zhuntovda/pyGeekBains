from MyPythonSub import return_exist_path
from math import fsum

f_path = return_exist_path()
list_price = []
with open(f_path, "r", encoding="UTF-8") as f_obj:

    for f_str in f_obj.readlines():
        f_str_list = f_str.split()
        s_name = ""
        s_summ = 0

        for f_word in f_str_list:
            try:
                s_summ = float(f_word)
            except ValueError:
                s_name = (s_name + " " + f_word if len(s_name) != 0 else f_word)

        list_price.append(s_summ)

        if s_summ < float(20000):
            print(f"Беда у {s_name} оклад меньше 20 000")

    print(f"Средний доход = {fsum(list_price)/len(list_price)}")
