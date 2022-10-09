year=float(input("How many years you worked:"))
salary=float(input("Your current salary you are getting: "))
if year > 5:
    print("You will get a bonus of 1000rs")
    print("Your salary after bonus",salary+1000)
else:
    print("you are not eligible for bonus ")