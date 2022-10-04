from math import sqrt
firstSide=int(input("Enter your first side"))
secondSide=int(input("Enter your second side"))
thirdSide=int(input("Enter your third side"))
perimeter=firstSide+secondSide+thirdSide
semiPerimeter=perimeter/2
areaUsingHerons=sqrt(semiPerimeter-firstSide)*(semiPerimeter-secondSide)*(semiPerimeter-thirdSide)
print("the area of triangle is",areaUsingHerons)