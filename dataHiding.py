class Persons:
    def __init__(self,name,age):
        self.__name=name
        self.__age = age

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

person1 = Persons("ABC",22)
print(person1._Persons__name)
print(person1._Persons__age)