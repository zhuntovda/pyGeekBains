from MyPythonSub import return_exist_path

with open(return_exist_path(), "w", encoding="UTF-8") as f_obj:
    while True:
        text_int = input("Введите строчку текста:")
        if len(text_int) == 0:
            break
        print(text_int, file=f_obj)