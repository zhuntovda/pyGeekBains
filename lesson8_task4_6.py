from uuid import uuid4

def ValueGood(value, list_value=None, txt_type="str"):
    if len(value) == 0:
        return False
    if txt_type == "int":
        for el in value:
            if not "0" <= el <= "9":
                return False
        value = int(value)
        if not list_value is None:
            return list_value.count(value)
        return True


class Menu:

    def __init__(self):
        self.__dict__ = {"Основное меню": {"Оформить движение оргтехники": {"Принять оргтехнику на склад": "takeEq",
                                                                            "Переместить оргтехнику со склада": "giveEq"},
                                           "Отчеты": {"Отчет по заполнености склада": "reportFull",
                                                      "Отчет по последним движениям": "lastMovements"},
                                           "Выход": "exit"}}
        self.__menulevel = ["Основное меню"]
        self.__now_change = dict()

    def GoOut(self):
        if input("Вы точно хотите выйти (y): ") == "y":
            exit()
        self.__menulevel = ["Основное меню"]

    @property
    def BuilMenu(self):
        dictMenu = self.__dict__
        for el in self.__menulevel:
            dictMenu = dictMenu[el]
        str_menu = ""
        self.__now_change = dict()
        for key in dictMenu:
            i = len(self.__now_change) + 1
            str_menu += f"\n\t{str(i)}. {key}"
            self.__now_change[i] = key
        return f"{el} (назад - 0) {str_menu}"

    def ChoiceMenu(self, Storage, nom):
        if not ValueGood(nom, list(range(0, len(self.__now_change) + 1)), "int"):
            print(f"Значение {nom} не может быть выбрано (требуется число в пределе значений пунктов меню)!")
            return
        int_nom = int(nom)
        if int_nom == 0:
            self.__menulevel.pop()
            if len(self.__menulevel) == 0:
                self.GoOut()
            return
        dictMenu = self.__dict__
        for el in self.__menulevel:
            dictMenu = dictMenu[el]
        if type(dictMenu[self.__now_change[int_nom]]) == str:
            do_str = dictMenu[self.__now_change[int_nom]]
            if do_str == "exit":
                self.GoOut()
                return
            Storage.DoThisStorage(do_str)
            self.__menulevel = ["Основное меню"]
        else:
            self.__menulevel.append(self.__now_change[int_nom])


class Storage:

    def __init__(self, name, volume, structure):
        self.volume = volume
        self.__name = name
        self.__structure = structure
        self.__history = list()
        self.__equipment = dict()

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if self.StorageListVolume(other.volume)["is_full"]:
            self.__add_history("Отказ в приемке (склад переполнен): " + str(other))
            return
        self.__equipment[other.ID] = other
        self.__add_history("Принят на склад: " + str(other))

    def __sub__(self, other):
        for key in self.__equipment.keys():
            if key == other.ID:
                self.__add_history("Со склада удален:" + str(other))
                self.__equipment.pop(key)
                break

    def __add_history(self, text):
        self.__history.append(text)
        print(text)

    def StorageListVolume(self, volume_eq=0):
        volume = 0
        for key in self.__equipment.keys():
            volume += self.__equipment[key].volume
        volume += volume_eq
        return {"free": self.volume - volume, "cloust": volume, "is_full": volume > self.volume}

    def DoThisStorage(self, command):
        if command == "takeEq":
            eq_type = input(f" Введите тип принимаемого устройства из списка\n{OfficeEquipment.ListOfType()}:\n")
            if OfficeEquipment.ListOfType().count(eq_type) == 0:
                print("Нет такого типа")
                return
            brand = input("Введите брэнд устройства: ")
            color = input("Введите цвет устройства: ")
            volume = input("Введите объем устройства в м^3: ")
            if not ValueGood(volume, None, "int"):
                print("Не верный формат объема!")
                return
            originaltype = "ups"
            self + OfficeEquipment.add_OfficeEquipment(eq_type, brand, color, originaltype, int(volume))
        elif command == "giveEq":
            txt_choice = "Выбирете устройство для удаления со склада:"
            if len(self.__equipment.keys()) == 0:
                print(f"{str(self)} пуст!")
                return
            for key in self.__equipment.keys():
                txt_choice += f"\n\t{list(self.__equipment.keys()).count(key)}. {str(self.__equipment[key])}"
            nom = input(txt_choice)
            if not ValueGood(nom, list(range(1, len(self.__equipment.keys()))), "int"):
                print("Устройство не найдено!")
                return
            nom_int = int(nom)
            self - self.__equipment[list(self.__equipment.keys())[nom_int - 1]]
        elif command == "reportFull":
            txt_report = "ОТЧЕТ ОБ ОСТАТКАХ"
            for key in self.__equipment.keys():
                txt_report += f"\n\t\t{str(self.__equipment[key])}"
            txt_report += "\n-------------------------------------------------------------"
            txt_report += f"\nЗаполне на {self.StorageListVolume()['cloust']}, осталось {self.StorageListVolume()['free']} м^3"
            print(txt_report)
        elif command == "lastMovements":
            txt_report = "ОТЧЕТ О ПОСЛЕДНИХ ДВИЖЕНИЯХ"
            for el in self.__history:
                txt_report += f"\n\t\t{el}"
            print(txt_report)

class OfficeEquipment:

    def __init__(self, eq_type, brand, color, volume):
        self.eq_type = eq_type
        self.brand = brand
        self.color = color
        self.volume = volume
        self.ID = uuid4()

    @classmethod
    def add_OfficeEquipment(cls, eq_type, brand, color, originaltype, volume):
        if eq_type == "Printer":
            return Printer(brand, color, originaltype, volume)
        elif eq_type == "Scan":
            return Scan(brand, color, originaltype, volume)
        elif eq_type == "CopyMachine":
            return CopyMachine(brand, color, originaltype, volume)

    @classmethod
    def ListOfType(cls):
        return list(["Printer", "Scan", "CopyMachine"])


class Printer(OfficeEquipment):

    def __init__(self, brand, color, printertype, volume):
        super().__init__("Printer", brand, color, volume)
        self.printertype = printertype

    def __str__(self):
        return f"Принтер {self.brand} ({self.color}) тип печати {self.printertype} занимает {self.volume} м^3 (ID:{self.ID})"


class Scan(OfficeEquipment):

    def __init__(self, brand, color, scantype, volume):
        super().__init__("Scan", brand, color, volume)
        self.scantype = scantype

    def __str__(self):
        return f"Сканер {self.brand} ({self.color}) разрешение {self.scantype} занимает {self.volume} м^3 (ID:{self.ID})"


class CopyMachine(OfficeEquipment):

    def __init__(self, brand, color, copytype, volume):
        super().__init__("CopyMachine", brand, color, volume)
        self.copytype = copytype

    def __str__(self):
        return f"Копировальный аппварат {self.brand} ({self.color}) разрешение {self.copytype} занимает {self.volume} м^3 (ID:{self.ID})"


M = Menu()
S = Storage("Основной склад", 100, ["Магазин", "Выдача"])

while True:
    print(M.BuilMenu)
    M.ChoiceMenu(S, input("\n Введите пункт меню:"))
