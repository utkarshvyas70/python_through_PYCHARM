#Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place
# of service.

#if employee is female, then she will work only in urban areas.

#if employee is a male and age is in between 20 to 40 then he may work in anywhere

#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

#And any other input of age should print "ERROR".
M="Male"
F="Female"
Y="Yes"
N="No"
enter_age=float(input("Enter your age:"))
sex=str(input("Your sex M/F:"))
marital_status=str(input("Married or not Y/N:"))
if sex=="Female" and enter_age>=20 and enter_age<=60:
    print("You will work in urban areas")
else:
    print("Sleep")

if sex=="Male" and enter_age>=20 and enter_age<=40:
    print("You can work anywhere")
elif sex=="Male" and enter_age>40 and enter_age<=60:
    print("You will work in urban areas only")
else:
    print("Error")


