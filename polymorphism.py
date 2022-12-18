# def add(a,b,c = 0):
#     return a+b+c
# print(add(1,2))
# print(add(1,2,3))

# class Rect:
#     def calcArea(self,length=None,breadth=None):
#         if length != None and breadth != None:
#             return length * breadth
#         elif length != None:
#              return length * length
# Rectangle = Rect()
# print(Rectangle.calcArea(2,3))
# print(Rectangle.calcArea(2))


# class bird:
#     def category(self):
#         print("this is a category of bird")
#     def fly(self):
#         print("I can fly")
# class crow(bird):
#     pass
# class sparrow(bird):
#     def sizeparameter(self):
#         print("I am small in size")
# class ostrich(bird):
#     def fly(self):
#         print("I cannot fly, sorry!")
#
# objbird=bird()
# objsparrow=sparrow()
# objcrow=crow()
# objbird.category()
# objbird.fly()
# objostrich=ostrich()
# objsparrow.category()
# objsparrow.fly()
# objsparrow.sizeparameter()
# objcrow.category()
# objcrow.fly()
# objostrich.category()
# objostrich.fly()

class vehicle:
    def seatingcapacity(self):
        print("Seating capacity is 4")
class car1(vehicle):
    pass
class car2(vehicle):
    pass
class bus(vehicle):
    def seatingcapacity(self):
        print("Seating capacity is 50")

objvehicle=vehicle()
objcar1=car1()
objcar2=car2()
objbus=bus()
objcar1.seatingcapacity()
objcar2.seatingcapacity()