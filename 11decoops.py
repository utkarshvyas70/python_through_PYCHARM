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

class person:
    def __init__(self,name,rollNum):
        self.person=name
        self.rollNum=rollNum
    def printoutput(self):
        print("My name is: ",self.person,"and my roll no. is:",self.rollNum)

a=person("ramesh",775675)
b=person("suresh",757575)
a.printoutput()
b.printoutput()