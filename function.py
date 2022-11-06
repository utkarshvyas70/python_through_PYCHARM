"""#defining a fucction
def boy():
    print("Hey")
    print("Girl")
#calling a function
boy()"""


"""def add(num1,num2):
    subtract=num1-num2
    print(subtract)
add()"""


"""def multiply(num1,num2):
    multiply=num1*num2
    return multiply
x=multiply(1,2)
print(x)"""


"""def name(firstname):
    print("My name is",firstname)
name("Fati")
name("Bhosdi")"""

"""def name(firstName, lastName):
    print("my name is",firstName + " " + lastName)
name("Utkarsh", "Vyas")"""

"""def name(*args):
    print(args)
name("Utkarsh", "Vyas")"""


"""def name(name, *args):
    print(name)
    print(args)
name("Utkarsh","Vyas")"""

"""def info(name, **data):
    print(name)
    print(data)
    


info("Utkarsh",age=19,place="Kota",num=432443232424234)"""


def info(name, **data):
    print(name)
    print(data)
    for i, j in data.items():
        print(i, j)

info("Utkarsh", age=19, place="Kota", num=432443232424234)



