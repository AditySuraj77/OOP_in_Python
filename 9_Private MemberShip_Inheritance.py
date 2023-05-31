

class Phone:
    def __init__(self,price,brand):
        print('Parent Class Constructor')

        self.__price = price
        self.brand = brand


class Smartphone(Phone):
    pass

                           # Child class not inheritance User class Private Membership variables
s = Smartphone(11999,'ViVo')

print(s.__price)


