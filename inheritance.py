class A:
    def __init__(self):
        print("This is init method of A")
    def method1(self):
        print("This is method 1")
class B:
    def method2(self):
        print("This is a method 2")
# class B(A):
#     def method2(self):
#         print("This is a inherited method")
# class C(B):
#     def method3(self):
#         print("This is method 3")
class C(A,B):
    def method4(self):
        print("This is a multiple inheritance")


obj1=A()
obj2=B()
obj3=C()