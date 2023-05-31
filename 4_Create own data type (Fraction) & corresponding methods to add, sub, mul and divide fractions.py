class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __add__(self, other):
        tem_num = self.num * other.den + other.num * self.den
        tem_den = self.den * other.den
        return '{}/{}'.format(tem_num, tem_den)

    def __sub__(self, other):
        tem_num = self.num * other.den - other.num * self.den
        tem_den = self.den * other.den
        return '{}/{}'.format(tem_num, tem_den)

    def __mul__(self, other):
        tem_num = self.num * other.num
        tem_den = self.den * other.den
        return '{}/{}'.format(tem_num, tem_den)

    def __truediv__(self, other):
        tem_num = self.num * other.den
        tem_den = self.den * other.num
        return '{}/{}'.format(tem_num, tem_den)


x = Fraction(2, 5)
y = Fraction(2, 5)

print('Addition of Fraction = ', x + y)
print('Substraction of Fraction = ', x - y)
print('Multiplication of Fraction = ', x * y)
print('Division of Fraction = ', x / y)
