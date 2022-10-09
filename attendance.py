Total_number_of_classes=10
Your_classes=int(input("How many classes you have attended:"))
Attendance=(Your_classes/Total_number_of_classes)*100
if Attendance > 75:
    print("The percentage is:",Attendance,"you are eligible for exams")
else:
    print("The percentage is:",Attendance,"you are not eleigible")
