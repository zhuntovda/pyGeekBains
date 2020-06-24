from random import randint


class MyComplexNumber:

    def __init__(self, a, b):
        self.__complex_num = complex(a, b)
        self.__complex_txt = f"({a} + {b}i)"
        self.a = a
        self.b = b

    def __str__(self):
        return self.__complex_txt

    def __add__(self, other):
        return MyComplexNumber((self.a + other.a), (self.b + other.b))

    def __mul__(self, other):
        return MyComplexNumber((self.a * other.a - self.b * other.b), (self.a * other.b + self.b * other.a))

    def complex(self):
        return self.__complex_num


complex1 = MyComplexNumber(randint(-100, 100), randint(-100, 100))
complex2 = MyComplexNumber(randint(-100, 100), randint(-100, 100))
complex3 = complex1 + complex2
complex4 = complex1 * complex2

print(f"{complex1} + {complex2} = {complex3}")
print(f"{complex1} * {complex2} = {complex4}")

