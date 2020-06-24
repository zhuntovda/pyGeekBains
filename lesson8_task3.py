class NotInteger(Exception):

    def __init__(self, text):
        self.text = text

    @classmethod
    def IsNum(cls, text):
        for i in range(0, 9):
            text = text.replace(str(i), "")
        return len(text) == 0

list_nom = list()
while True:
    sym = input("Введите число для продолжения последовательности, или пустую строку, как стоп символ: ")
    if len(sym) == 0:
        break
    try:
        if not NotInteger.IsNum(sym):
            raise NotInteger(f"Ошибка значения, повторите ввод {sym}")
        list_nom.append(sym)
    except NotInteger as err:
        print(err)
print(list_nom)