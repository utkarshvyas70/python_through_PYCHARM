'''colors=["Red","Blue","Red","Black",55]
print(colors)

colors=["Red","Blue","Red","Black",55]
print(colors[1])

colors=["Red","Blue","Red","Black",55]
colors[2]="Green"
print(colors)

colors=["Red","Blue","Red","Black",55]
colors[0:2]=["Yellow","Orange"]
print(colors)

colors=["Red","Blue","Red","Black",55]
colors.insert(2,"Turqoise")
print(colors)

colors=["Red","Blue","Red","Black",55]
colors.append("Mercedes")
print(colors)

cars=["Tata","Bmw"]
cars.extend(colors)
print(cars)

colors=["Red","Blue","Red","Black",55]
colors.pop(1)
print(colors)

colors=["Red","Blue","Red","Black",55]
colors.remove("Red")
print(colors)

colors=["Red","Blue","Red","Black"]
cars=["Tata","Bmw"]
for x in range(len(cars)):
    print(cars[x])
while x<len(cars):
    print(cars[x])
    x+=1


colors=["Red","Blue","Red","Black"]
cars=["Tata","Bmw"]
[print(x) for x in cars]

list=[]
cars=["Tata","Bmw"]
for i in cars:
    if "a" in i:
        list.append(i)
print(list)

colors=["Red","Blue","Red","Black"]'''
cars=["Tata","Bmw"]

list=[x for x in cars if x=="Tata"]
print(list)

list=[x for x in cars if x!="Tata"]
print(list)

colors=["Red","Blue","Red","Black"]
cars=["Tata","Bmw"]
numbers=[1,4,6,8,10]
cars.sort()
numbers.sort()
print(cars)

colors=["Red","Blue","Red","Black"]
cars=["Tata","Bmw"]
numbers=[1,4,6,8,10]
cars.sort()
numbers.sort()
print(cars)


numbers=[1,2,3,4,5,6,7]
squares=[]
for i in numbers:
    squares.append(i**2)
print(squares)

numbers=[1,2,3,4,5,6,2,8,9]
for i in range(0,len(numbers)-1):
    if numbers[i]==2:
        numbers.pop(i)
        numbers.insert(i,200)
print(numbers)

indx=numbers.index(2)
numbers[indx]=200
print(numbers)

list1=["x","y","z"]
list2=[1,2,3]
for x in list2:
    list1.append(x)
list3=list1+list2
print(list3)