from MyPythonSub import return_exist_path
from MyPythonSub import ImportInt
import json

list_firms =[]
sum_list = []
f_path = return_exist_path()
count_firm = 0
with open(f_path, "r", encoding="UTF-8") as f_obj:
    for f_str in f_obj.readlines():
        list_firm = f_str.split()
        real_profit = ImportInt(list_firm[2])[1] - ImportInt(list_firm[3])[1]
        if real_profit > 0:
            sum_list.append(real_profit)
            count_firm += 1
        list_firms.append(
            {"name": list_firm[0], "type": list_firm[1], "profit": real_profit, "cost": ImportInt(list_firm[3])[1]})

sum_middel = sum(sum_list)/count_firm
dict_firms =dict()
for el in list_firms:
    dict_firms[el["name"]] = el["profit"]

list_json = [dict_firms, {"average_profit":sum_middel}]

with open("json_firms_1.json", "w", encoding="UTF-8") as write_f:
    json.dump(list_json, write_f, ensure_ascii=False)