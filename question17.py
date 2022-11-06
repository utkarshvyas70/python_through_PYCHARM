"""create a function using following condition


it should accept employee name and salary and display both


it the salary is missing in the function the assign the default value 10000 to salary


ben(9000) mike(15000) bob()"""

def hungama(employee,salary=10000):
    print(employee,salary)
hungama("ben",9000)
hungama("mike",15000)
hungama("bob")