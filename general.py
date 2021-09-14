from enum import Enum

class Rol(Enum):
    '''ENUMERATORS'''
    STUDENT = 1
    PROFESSOR = 2
    DIRECTOR = 3


class Person():

    '''In python you cannot define multiple constructors, instead you have
    to use default values'''

    country = ['Colombia'] # Static attribute

    def __init__(self, rol, name: str = None, age=None, heigth=None):
        
        self.rol = rol
        self.__name = name # If i want private attributes, I should use __<attr_name>
        self.__age = age
        self.__heigth = heigth

    @property
    def name(self): # GETTER
        return self.__name

    @name.setter # SETTER
    def name(self, name):
        self.__name = name

    @name.deleter # DELETER
    def name(self):
        self.__name = None # Esto es algo que puedo hacer
        # del self.__name

    @property
    def heigth(self):
        return self.__heigth

    def sayHiToPerson(self):
        return 'Hi! {}'.format(self.__name)

    @staticmethod
    def sayHiToInputPerson(name):
        return 'Hi there! {}'.format(name)


p1 = Person(Rol.STUDENT, name=21, age=26, heigth=176)
print(p1.name) # getter

p1.name = 'Juan' # setter
print(p1.name)

del(p1.name) # deleter

print(p1.heigth)
print(p1.name)

print(p1.rol.name, p1.rol.value, type(p1.rol))

if p1.rol == Rol.STUDENT:
    print('same types!')

p1.name = 'Daniel'
print(p1.sayHiToPerson())

# using static method
print(Person.sayHiToInputPerson('Juan'))

# Print static attribute
print(p1.country)

p2 = Person(Rol.PROFESSOR)

p2.country.append('Russia')

print(p1.country)

