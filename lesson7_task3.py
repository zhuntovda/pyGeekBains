from random import randint


class AntiCell:

    def __str__(self):
        return "Опасно! Антиматерия! Возмоожен коллапс!"

    @property
    def number(self):
        return 0

    def make_order(self,number_str):
        return f"Опасно! Антиматерия! Возмоожен коллапс через {number_str} секунд!"


class Cell:

    def __init__(self, number=None):
        self.__number = number if number is not None else randint(1, 30)

    @property
    def number(self):
        return self.__number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if (self.number - other.number) < 0:
            return AntiCell()
        else:
            return Cell(self.number - other.number)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(round(self.number * other.number))

    def make_order(self,number_str):
        cell_text = ""
        for i in range(self.__number):
            cell_text += "*" + ("\n" if i%number_str == 0 else "")
        return cell_text


list_cell = list()
for i in range(20):
    list_cell.append(Cell())

add = list_cell[randint(0, 19)] + list_cell[randint(0, 19)]
sub = list_cell[randint(0, 19)] - list_cell[randint(0, 19)]
mul = list_cell[randint(0, 19)] * list_cell[randint(0, 19)]
truediv = list_cell[randint(0, 19)] / list_cell[randint(0, 19)]

print(add.make_order(randint(3, 10)))
print(sub.make_order(randint(3, 10)))
print(mul.make_order(randint(3, 10)))
print(truediv.make_order(randint(3, 10)))
