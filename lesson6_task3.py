class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        sum = 0
        for key in self._income.keys():
            sum += self._income[key]
        print(sum)


income_dict = {"wage": 1000, "bonus": 100}
Person = Position("Ivan", "Ivanov", "hardworker", income_dict)

Person.get_full_name()
Person.get_total_income()