a=int(input("Enter your number:"))
b=int(input("Enter your number:"))

operator=(input("Your operator:"))
if operator=="+":
    print("Your sum is:",a+b)
elif operator=="-":
    print("Your subtration is:",a-b)
elif operator=="*":
    print("Your multiplication is:",a*b)
else:
    print("Invalid operator")

