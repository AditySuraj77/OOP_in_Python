


class Phone:
    def __init__(self,price,brand):
        print('Parent Class Constructor')

        self.price = price
        self.brand = brand

    def buy(self):
        print('Buying a Phone')


class Smartphone(Phone):

    def buy(self):
        print('Buying a SmartPhone')
        super().buy()  # if you fetch Parent class attribute so you will use SuperMethod   super()   to Call Parent Class Method


s = Smartphone(11999,'ViVo')

print(s.buy())