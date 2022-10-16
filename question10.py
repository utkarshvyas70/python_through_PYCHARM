first_side=int(input("Enter first side:"))
second_side=int(input("Enter second side:"))
third_side=int(input("Enter third side:"))
if first_side+second_side>third_side:
    print("You can form a triangle")
elif first_side+third_side>second_side:
    print("You can form a triangle")
elif second_side+first_side>third_side:
    print("You can form a triangle")
elif second_side+third_side>first_side:
    print("You can form a triangle")
else:
    print("This cant form triangle")