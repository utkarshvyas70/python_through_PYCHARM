#Write a program to check if a year is leap year or not.
#If a year is divisible by 4 then it is leap year
# but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.
Year=int(input("Enter the year:"))
if Year%4==0:
    print("It is a leap year")
elif  Year%400==0:
    print("It is a leap year")

else:
    print("Invalid input")