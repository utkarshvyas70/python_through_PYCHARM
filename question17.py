"""create a function using following condition


it should accept employee name and salary and display both


it the salary is missing in the function the assign the default value 10000 to salary


ben(9000) mike(15000) bob()"""

a=input("Name")
def hungama(employee,salary=10000):
    x=input("Enter your Name:")
    print(employee,"salart=",salary)
hungama(a,9000)
hungama(a,15000)
hungama(a)