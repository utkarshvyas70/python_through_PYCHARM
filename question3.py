#company will give bonus based on different criteria
#time spent in company                       bonus
#     greater than 10 years                  10%
#     more than 6 and less than 10            8%
#     less than                               5%
#ask the salary and time spent from the user
#print the net bonus amount accordingly

years=float(input("Enter your years:"))
salary=float(input("Enter your current salary:"))

if years>10:
    print("Your salary after bonus",salary+salary*0.1)
elif years>6 and years<10:
    print("your salary after bonus", salary+salary*0.08)
elif years<6:
    print("Your salary after bonus",salary+salary*0.05)
else:
    print("You are fired!")