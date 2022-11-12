colors=["Red","Blue","Red","Black",55]
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