# a="gggg"
# print(type(a))
# class Laptop:
#     def config(self):
#         print("hp" , "r7" , "1TB")
#
# laptop1=Laptop()
# laptop2=Laptop()
#
# print(id(laptop1))
# print(id(laptop2))
#
# laptop1.config()
# laptop2.config()


# class Laptop:
#     def __init__(self):
#         self.name = "hp"
#         self.processor = "r5"
#
#     def bhoot(self):
#         print("My laptop name is :",self.name, "and processor is: ",self.processor )

# class person:
#     def __init__(self,name,rollNum):
#         self.person=name
#         self.rollNum=rollNum
#     def printoutput(self):
#         print("My name is: ",self.person,"and my roll no. is:",self.rollNum)
#
# a=person("ramesh",775675)
# b=person("suresh",757575)
# a.printoutput()
# b.printoutput()


# class Persons:
#     def __init__(self):
#         self.name="Utkarsh"
#         self.age=18
#     def updateName(self,name):
#         self.name=name
#
#     def compareage(self,other):
#         if self.age==other.age:
#             return True
#         else:
#             return False
#
# person1=Persons()
# person2=Persons()
#
# person2.name="Vyas"
#
# if person1.compareage(person2):
#     print("They are of same age")
# else:
#     print("They are of different age")
# print(person1.name,person1.age)
# print(person2.name,person1.age)

# class Car:
#     wheels=4
#     def __init__(self,brand,mil):
#         self.brand=brand
#         self.mil=mil
#
# car1=Car("Maruti Suzuki",18.6)
# car2=Car("BMW",9.6)
#
# Car.wheels=3
# print(car1.brand,car1.mil,car1.wheels)
# print(car2.brand,car2.mil,car2.wheels)


class Student:
    def __init__(self, marks1, marks2, marks3):
        self.web=marks1
        self.python=marks2
        self.map=marks3

    def averageCalc(self):
        print(self.web+self.python+self.map/3)

    def getMarks(self):
        return self.map


student1 = Student(5, 4, 3)
student2 = Student(7, 8, 9)
student3 = Student(1, 6, 9)


student1.averageCalc()
student2.averageCalc()
student3.averageCalc()