from abc import abstractmethod
from random import randint


class ClothesProject:

    def __init__(self):
        self.clothes_list = list()

    def add_clothes(self, clothes):
        self.clothes_list.append(clothes)

    def del_clothes(self, clothes):
        self.clothes_list.pop(self.clothes_list.count(clothes))

    @property
    def sum_clothes(self):
        sum = 0
        for el in self.clothes_list:
            sum += el.HowClothNeed
        return round(sum, 3)

    def add_new_Clothes(self, type, size):
        return Coat(size) if type == "coat" else Suit(size)


class Clothes:

    def __init__(self, size, type):
        self.typeClothes = type
        self.sizeClothes = size

    @property
    def type(self):
        return self.typeClothes

    @property
    def size(self):
        return self.sizeClothes

    @abstractmethod
    def HowClothNeed(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        super().__init__(size, "coat")
        print(f"add coat size: {size}")

    @property
    def HowClothNeed(self):
        return self.size/6.5 + 0.5


class Suit(Clothes):

    def __init__(self, size):
        super().__init__(size, "suit")
        print(f"add suit size: {size}")

    @property
    def HowClothNeed(self):
        return 2 * self.size + 0.3


ClothesP = ClothesProject()
for i in range(randint(1,40)):
    ClothesP.add_clothes(ClothesP.add_new_Clothes("coat" if randint(0,1) == 1 else "suit", randint(45, 100)))

print(f"summary clothes: {ClothesP.sum_clothes}")