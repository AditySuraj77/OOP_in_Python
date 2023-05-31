class Calculator:

    def __init__(self,num):

        self.num = num

    #def __str__(self):
        #return '{}/{}'.format(self.num,self.num)

    def __add__(self, other):
        add = self.num + other.num
        return add

    def __sub__(self, other):
        sub = self.num - other.num
        return sub

    def __mul__(self, other):
        mul = self.num * other.num
        return mul

    def __truediv__(self, other):
        div = self.num /other.num
        return div


num1 = float(input('Enter a First Number : '))
num2 = float(input('Enter a Second Number : '))
choice = input('Select a Operation + - * / : ')
x = Calculator(num1)
y = Calculator(num2)

if choice == '+':
    print('Addition = ',x + y)
elif choice =='-':
    print('Substraction = ',x - y)
elif choice == '*':
    print('Multiply = ',x * y)
elif choice == '/':
    print('Division = ',x / y)

else:
    print('Invalid Operations')
#print(cal)

#y = Calculator(44,3)
#print(y)