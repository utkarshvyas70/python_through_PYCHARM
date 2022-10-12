#Take input of age of 3 people by user and determine oldest and youngest among them
age1=float(input("Enter your age:"))
age2=float(input("Enter your age:"))
age3=float(input("Enter your age:"))
if age1>age2 and age1>age3:
    print("Age1 is greater")
elif age2>age1 and age2>age3:
    print("Age2 is greater")
elif age3>age1 and age3>age1:
    print("Age3 is greater")
if age1<age2 and age1<age3:
    print("Age1 is youngest")
elif age2 < age1 and age2 <age3:
    print("Age2 is youngest")
elif age3 < age1 and age3 < age2:
    print("Age3 is youngest")
else:
    print("Age is same")