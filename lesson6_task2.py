class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_value(self, weight, thickness):
        print(
            f"Масса асфальта, необходимого для покрытия всего дорожного полотна {(self._length * self._width * weight * thickness) / 1000} тонн")


try:
    OurRoad = Road(float(input("Введите длинну дороги в метрах ")), float(input("Введите ширину дороги в метрах ")))
    OurRoad.calc_value(
        float(input("Введите массу асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см ")),
        float(input("Введите число см толщины полотна ")))
except:
    print("Наверное параметры дороги заданы не верно =(")
