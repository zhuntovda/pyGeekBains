from random import choice


class Car:

    def __init__(self, speed=60, color="black", name="bug", is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.list_drive = ["front", "revers", "left", "right"]

    def go(self):
        print("ДрымДымДым")

    def stop(self):
        print("ТрымПымПых")

    def turn_direction(self):
        print(choice(self.list_drive))

    def show_speed(self):
        print(f"Скорость {self.speed}")


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение допустимой скорости на {self.speed - 60}")
        super().show_speed()


class SportCar(Car):

    def __init__(self):
        super().__init__(140, "red", "ferrary")


class WorkCar(Car):

    def __init__(self):
        super().__init__(50, "blue", "zil")

    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение допустимой скорости на {self.speed - 40}")
        super().show_speed()


class PoliceCar(Car):

    def __init__(self):
        super().__init__(120, "white", "poliz", True)


TCar = TownCar()
SCar = SportCar()
WCar = WorkCar()
PCar = PoliceCar()

TCar.show_speed()
WCar.show_speed()
PCar.show_speed()

print(WCar.speed)
print(SCar.color)
print(PCar.is_police)

PCar.go()
PCar.turn_direction()
PCar.turn_direction()
PCar.turn_direction()
PCar.stop()