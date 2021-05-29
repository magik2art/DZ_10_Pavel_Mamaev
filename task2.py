from abc import abstractmethod


class Clothes():

    def __init__(self, param):
        self.param = param
        self.cloth_for_coat = self.param / 6.5 + 0.5
        self.cloth_for_costume = 2 * self.param + 0.3

    @property
    def all_consumption(self):
        return f'Всего метров затраченной ткани: {self.cloth_for_coat + self.cloth_for_costume :.2f}'

    @abstractmethod
    def abstract(self):
        return 'Спасибо!\n'


class Coat(Clothes):
    def consumption(self):
        return f'Из них на пошив пальто: {self.cloth_for_coat :.2f} метров ткани'


class Costume(Clothes):
    def consumption(self):
        return f'Из них на пошив костюма: {self.cloth_for_costume :.2f} метров ткани'


coat = Coat(100)
costume = Costume(35)
print(f'{coat.all_consumption}\n{costume.consumption()}\n{coat.consumption()}\n{coat.abstract()}')
costume = Costume(75)
print(f'{coat.all_consumption}\n{costume.consumption()}\n{coat.consumption()}\n{coat.abstract()}')
