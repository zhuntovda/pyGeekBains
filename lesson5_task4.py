from MyPythonSub import return_exist_path

googleTrans = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_words_list = []
f_path = return_exist_path()
with open(f_path, "r", encoding="UTF-8") as f_obj:
    for f_str in f_obj.readlines():
        new_str = ""
        for el in f_str.split():
            try:
                new_str = new_str + ("" if len(new_str) == 0 else " ") + googleTrans[el]
            except KeyError:
                new_str = new_str + ("" if len(new_str) == 0 else " ") + str(el)
        new_words_list.append(new_str)

with open("new_" + f_path, "w", encoding="UTF-8") as fw_obj:
    for el in new_words_list:
        fw_obj.writelines(el)