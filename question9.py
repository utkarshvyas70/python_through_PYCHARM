#you have to take a user input check divisible by 3 and 2 both
a=int(input("Enter your number:"))
if a%2==0 :
    print("yes it is divisible by 2")
elif a%3==0:
    print("yes it is divisible 3")
elif a%2==0 and a%3==0:
    print("It is divisible by both")
else:
    print("invalid error")