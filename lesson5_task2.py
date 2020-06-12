from MyPythonSub import return_exist_path

f_path = return_exist_path()
#можно дополнить программно файл, а можно не дополнять
with open(f_path, "a", encoding="UTF-8") as f_obj:

     while True:
        text_int = input("Введите строчку текста:")
        if len(text_int) == 0:
            break
        print(text_int, file=f_obj)

with open(f_path, "r", encoding="UTF-8") as f_obj:

    str_count = 0
    for f_str in f_obj.readlines():
        f_str_list = f_str.split()
        str_count += 1
        print(f"В строке {str_count} слов {len(f_str_list) if f_str_list.count('/n') == 0 else len(f_str_list) - 1}")

    print(f"Количество строк в файле {str_count}")