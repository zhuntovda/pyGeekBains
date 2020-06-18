from random import randint

def str_full(value, num):
    str_full = str(value)
    for _ in range(num - len(str_full)):
        str_full = " " + str_full
    return str_full

class MatrixParam:

    def __init__(self):
        self.height = randint(2, 10)
        self.width = randint(2, 10)


class Matrix:

    def __init__(self, MatrixParam=None, value=None):
        if MatrixParam is not None:
            self.value = list()
            for h in range(MatrixParam.height):
                wvalue = list()
                for w in range(MatrixParam.width):
                    wvalue.append(randint(-99, 199))
                self.value.append(wvalue)
        else:
            self.value = value

    def __add__(self, other):
        new_value = list()
        for h in range(len(self.value)):
            wvalue = list()
            for w in range(len(self.value[h])):
                wvalue.append(self.value[h][w] + other.value[h][w])
            new_value.append(wvalue)
        return new_value

    def __str__(self):
        str_prew = ""
        for str_list in self.value:
            for el in str_list:
                str_prew += str_full(el, 3 if len(str(el)) == 0 else 5)
            str_prew += "\n"
        return str_prew

    def print_str(self, index_str=0):
        str_list = self.value[index_str]
        str_prew = ""
        for el in str_list:
            str_prew += str_full(el, 3 if len(str_prew) == 0 else 5)
        return str_prew


MParam = MatrixParam()
M1 = Matrix(MatrixParam=MParam)
M2 = Matrix(MatrixParam=MParam)
M3 = Matrix(value=(M1 + M2))

print(M3)

for i in range(MParam.height):
    flag_center = (MParam.height//2 == i)
    print(M1.print_str(i-1) + ("  +  " if flag_center else "     ") + M2.print_str(i) + (" === " if flag_center else "     ") + M3.print_str(i))
