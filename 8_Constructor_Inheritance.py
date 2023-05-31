
class Phone:
    def __init__(self,price,brand):
        print('Parent Class Constructor')

        self.price = price
        self.brand = brand


class Smartphone(Phone):
    pass


s = Smartphone(11999,'ViVo')

print(s.price)
print(s.brand)

