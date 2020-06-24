class MyZeroDivisionError(Exception):

    def __init__(self, text):
        self.text = text

    @classmethod
    def IsZero(cls,nom):
        return nom == 0

try:
    nom_sub = float(input("Введите делитель для 1 000 : "))
    if MyZeroDivisionError.IsZero(nom_sub):
        raise MyZeroDivisionError("На ноль не делем!")
    print(f"Результат {1000 / nom_sub}")
except MyZeroDivisionError as Err:
    print(Err)
except TypeError:
    print("Требуется ввести любое число!")
finally:
    print("Программа завершена!")
