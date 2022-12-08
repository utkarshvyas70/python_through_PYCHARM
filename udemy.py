 # Band name Generator
print("Band name generator!!")
city=input("What is the name of your city?\n")
pet=input("What is the name of your pet?\n")
print("Your band name is "+city+" "+pet)
#
#BMI Calculator
#
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
#
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
# else:
#     print(f"Your BMI is {bmi_int}, you are clinically obese.")
#
# # Leap year.
# year = int(input("Which year do you want to check? "))
#
# if year % 4 == 0:
#     print("Leap year.")
#
# elif year % 400 == 0:
#     print("Leap year.")
#
# elif year % 100 != 0:
#     print("Not leap year.")
#
# else:
#     print("Not leap year.")
#
# # Pizza Boy
#
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
#
# bill=0
# if size=="S":
#     bill+=15
# elif size=="M":
#     bill+=20
# else:
#     bill+=25
#
# if add_pepperoni=="Y":
#     if size=="Y":
#         bill+=2
#     else:
#         bill+=3
#
# if extra_cheese == "Y":
#     bill+=1
# print(f"Your final bill is: ${bill}.")
#
#
# #Love Calculator
#
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
#
#
#
# string=name1+name2
# upper_case=string.upper()
#
# t=upper_case.count("T")
# r=upper_case.count("R")
# u=upper_case.count("U")
# e=upper_case.count("E")
#
# true=t+r+u+e
#
# l=upper_case.count("L")
# o=upper_case.count("O")
# v=upper_case.count("V")
# e=upper_case.count("E")
#
# love=l+o+v+e
#
# score=int(str(true)+str(love))
#
# if (score<10) or (score>90):
#     print(f"Your score is {score}, you go together like coke and mentos.")
#
# elif (score>=40) and (score<=50):
#     print(f"Your score is {score}, you are alright together.")
#
# else:
#     print(f"Your score is {score}.")
#
# #Treasure game.
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
#
#
# a = str(input("Where you want to go left or right?\n"))
# if a == "right":
#     print("Fall into a hole\n Game over")
# elif a == "left":
#     b = str(input("swim or wait?\n"))
#     if b == "swim":
#         print("Attacked by trout\n Game over")
#     elif b == "wait":
#         print("Which door(red,yellow,blue)?\n")
#         c = str(input(""))
#         if c == "red":
#             print("Burned by fire.\n Game over")
#         elif c == "yellow":
#             print("You Win!")
#         elif c == "Blue":
#             print("Eaten by beasts!\n Game over.")
#         else:
#             print("Game over.")
#
# # Heads or Tails.
# import random
# coin=random.randint(0,1)
# if coin == 1:
#     print("Tails")
# elif coin == 0:
#     print("Heads")
#
#
# #Treasure map
#
# row1 = ["⬜️","️⬜","️⬜"]
# row2 = ["⬜️","⬜️","️⬜"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure?")
# horizontal=int(position[0])
# vertical=int(position[1])
# row=map[vertical-1]
# row[horizontal-1]='X'
# print(f"{row1}\n{row2}\n{row3}")
#
# #rockpaperscissors
# import random
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
#
# images=[rock,paper,scissors]
# user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n Your choice:"))
# print(images[user_choice])
# computer_choice=random.randint(0,2)
# print(f"Computer chose {computer_choice}")
# print(images[computer_choice])
# if user_choice>=3:
#   print("invalid")
# elif user_choice==0 and computer_choice:
#   print("You win!")
# elif user_choice==2 and computer_choice==0:
#   print("You loose 1")
# elif user_choice > computer_choice:
#   print("You win!")
# elif computer_choice > user_choice:
#   print("You loose.")
# elif computer_choice==user_choice:
#   print("It's a draw")
#
# #average height

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

value = 0
for height in student_heights:
    value += height
count = 0
for i in student_heights:
    count += 1
average_height = round(value/count)
print(average_height)

# # # maximum value
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score=0
for score in student_scores:
    if score>highest_score:
        highest_score=score
print(f"The highest score in the class is: {highest_score}")

#even sum
for i in range(2,101,2):
    summ=summ+i
print(summ)
#

# FizzBuzz game

 for i in range(1, 101):
     if i % 3 == 0 and i % 5 == 0:
         print("FizzBuzz")
     elif i % 3 == 0:
         print('Fizz')
     elif i % 5 == 0:
         print('Buzz')

     else:
         print(i)
