class Phone:

    def __init__(self,price,brand,camera):
        print('Parent class Constructor')

        self.price = price
        self.brand = brand
        self.camera = camera

        print('Phone')

class SmartPhone(Phone):

    def __init__(self,price,brand,camera,os,ram):
        print('Here')
        super().__init__(price, brand, camera)

        self.os = os
        self.ram = ram

        print('SmartPhone')

s = SmartPhone(21000,'ViVo','64px','Mac',8)
p = Phone(15000,'Samsung','16px')
print(s.price)
print(p.camera)

