# Band name Generator
print("Band name generator!!")
city=input("What is the name of your city?\n")
pet=input("What is the name of your pet?\n")
print("Your band name is "+city+" "+pet)

#BMI Calculator

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)
bmi_int = int(bmi)
if bmi_int < 18.5:
    print(f"Your BMI is {bmi_int}, you are underweight.")
elif bmi_int < 25:
    print(f"Your BMI is {bmi_int}, you have a normal weight.")
elif bmi_int < 30:
    print(f"Your BMI is {bmi_int}, you are slightly overweight.")
elif bmi_int < 35:
    print(f"Your BMI is {bmi_int}, you are obese.")
else:
    print(f"Your BMI is {bmi_int}, you are clinically obese.")

# Leap year.
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    print("Leap year.")

elif year % 400 == 0:
    print("Leap year.")

elif year % 100 != 0:
    print("Not leap year.")

else:
    print("Not leap year.")