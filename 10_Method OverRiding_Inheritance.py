


class Phone:
    def __init__(self,price,brand):
        print('Parent Class Constructor')

        self.price = price
        self.brand = brand

    def buy(self):
        print('Buying a Phone')


class Smartphone(Phone):

                             # This is Method OverRiding if you have method in Parent Class and Same method
                             # are in Child Class so python excute child class method and this is called
    def buy(self):           # Method Overriding
        print('Buying a SmartPhone')


s = Smartphone(11999,'ViVo')

print(s.buy())