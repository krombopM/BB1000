'''

class Person:

    number = 0

    def __init__(self, GivenName, SurName):
        self.Givenname = GivenName
        self.SurName = SurName

        Person.number += 1

pa = Person('John', 'Smith')

pb = Person('John', 'Doe')

#print('The number of persons are: ', Person.number)



class yearData:
    def __init__(self, Year, Month, Day):
        self.Year = Year
        self.Month = Month
        self.Day = Day


class Employee(Person, yearData):

    def __init__(self, GivenName, SurName, Year, Month, Day, Company):
        Person.__init__(self, GivenName, SurName)
        yearData.__init__(self, Year, Month, Day)
        self.Company = Company



import math


class Vector3D(object):
    def __init__(self, x, y, z):
        self.vector = [x, y, z]
        self.coordX = x
        self.coordY = y
        self.coordZ = z
        print(self.vector)

    def length(self):
        l = math.sqrt((self.coordX**2) + (self.coordY**2) + (self.coordZ**2))
        return(l)

    def norm(self):
        l = self.length()
        self.coordX = self.coordX/l
        self.coordY= self.coordY/l
        self.coordZ = self.coordZ/l


    def __add__(self, other):
        x, y, z = self.vector
        x2, y2, z2 = other.vector
        return Vector3D(x+x2, y+y2, z+z2)


    def __sub__(self, other):
        x ,y, z = self.vector
        x2, y2, z2 = other.vector
        return Vector3D(x-x2, y-y2, z-z2)





vector = Vector3D(1.0, 2.0, 4.0)
assert vector.coordX == 1.0
assert vector.coordY == 2.0
assert vector.coordZ == 4.0

vector = Vector3D(1.0, 2.0, 4.0)
assert vector.length() == math.sqrt(21.0)

vector = Vector3D(1.0, 2.0, 4.0)
vector.norm()
assert vector.length() == 1.0

avector = Vector3D(1.0, 2.0, 4.0)
bvector = Vector3D(2.0, 3.3, 0.9)
cvector = avector + bvector
assert cvector.coordX == 3.0
assert cvector.coordY == 5.3
assert cvector.coordZ == 4.9

avector = Vector3D(1.0, 2.0, 4.0)
bvector = Vector3D(2.0, 0.2, 0.9)
cvector = avector - bvector
assert cvector.coordX == -1.0
assert cvector.coordY ==  1.8
assert cvector.coordZ ==  3.1

'''


class Money:
    """A class for manipulation of different currencies"""
    conversion_rate = 10

    def __init__(self, amount, currency):
        self.currency = currency
        self.amount = amount

    def set_conversion_rate(self, new_conversion_rate):
        Money.conversion_rate = new_conversion_rate

    def __add__(self, other):
        if (self.currency == 'EURO'):
            self.amount = self.amount*Money.conversion_rate
            self.currency = 'SEK'

        if (other.currency == 'EURO'):
            other.amount = other.amount*Money.conversion_rate
            other.currency = 'SEK'

        amount = self.amount + other.amount
        currency = 'SEK'
        return Money(amount, currency)


    def __sub__(self, other):
        if (self.currency == 'SEK'):
            self.amount = self.amount/Money.conversion_rate
            self.currency = 'EURO'

        if (other.currency == 'SEK'):
            other.amount = other.amount/Money.conversion_rate
            other.currency = 'EURO'

        amount = self.amount - other.amount
        currency = 'EURO'
        return Money(amount, currency)



assert Money.conversion_rate == 10.0


ma = Money(100, 'SEK')
mb = Money(50, 'EURO')
assert ma.amount == 100
assert ma.currency == 'SEK'
assert mb.amount == 50
assert mb.currency == 'EURO'


ma = Money(100, 'SEK')
mb = Money(50, 'EURO')
mc = ma + mb
assert mc.amount == 600
assert mc.currency == 'SEK'



ma = Money(100, 'SEK')
mb = Money(50, 'EURO')
md = mb - ma
assert md.amount == 40
assert md.currency == 'EURO'


ma = Money(100, 'SEK')
mb = Money(50, 'EURO')
ma.set_conversion_rate(20)
assert ma.conversion_rate == 20
assert mb.conversion_rate == 20





















