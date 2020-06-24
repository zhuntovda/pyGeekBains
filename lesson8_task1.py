import calendar


class Date:

    @classmethod
    def IntDictDate(cls,text):
        list_date = text.split("-")
        try:
            list_date = list(map(int, list_date))
        except ValueError:
            print("Ошибка формата даты все вводимые данные должны легко преобразовываться к целому числу!")
            exit()
        Date.ValidDateParte(day=list_date[0], month=list_date[1], year=list_date[0])

    @staticmethod
    def ValidDateParte(day, month, year):
        try:
            if not 1 <= day <= calendar.monthrange(year, month)[1]:
                print("День месяца не подходит!")
        except calendar.IllegalMonthError:
            print("Месяц не вписывается в концепцию!")


print("Введите дату")
Date.IntDictDate(input("Введите число даты: ") + "-" + input("Введите месяц даты: ") + "-" + input("Введите год даты: "))