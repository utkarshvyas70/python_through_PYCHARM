from math import sqrt
#first command
firstSide=int(input("Enter your first side"))
#second command
secondSide=int(input("Enter your second side"))
#third command
thirdSide=int(input("Enter your third side"))
#perimeter
perimeter=firstSide+secondSide+thirdSide
#semi perimeter
semiPerimeter=perimeter/2
#process
areaUsingHerons=sqrt(semiPerimeter-firstSide)*(semiPerimeter-secondSide)*(semiPerimeter-thirdSide)
#printing
print("the area of triangle is",areaUsingHerons)

#class type herons
a=float(input("Enter your fisrt side"))
b=float(input("Enter your second side"))
c=float(input("Enter your third side"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of triangle is:",area)