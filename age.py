#take input of age from three people, determine the oldest and youngest.
person1=int(input("Enter your age:"))
person2=int(input("Enter your age:"))
person3=int(input("Enter your age:"))

if person1>person2 and person1>person3:
    print("oldest is",person1)
elif person2>person1 and person2>person3:
    print("oldest is",person2)
elif person3>person1 and person3>person2:
    print("oldest is",person3)
else:
    print("All have same age")

if person1<person2 and person1<person3:
    print("youngest is",person1)
elif person2<person1 and person2<person3:
    print("youngest is",person2)
elif person3<person1 and person3<person2:
    print("youngest is",person3)
else:
    print("All have same age")
