"""Local scope: A variable created inside a function
 belongs to the local scope of that function, and can only be used inside that function"""

def myfunc():
    x=300
    print(x)
myfunc()

"""Function iside function: In above x is not available
outside the function, but it is available for any function inside the func"""

def myfunc():
    x=300
    def myinnerfunc():  print(x)
    myinnerfunc()
    myfunc()

"""Global scope: A vaiable created outside of a function is global and can be 
used by anyone"""
x=300
def myfunc():
    print(x)
    myfunc()
    print(x)
    print(x)

"""If you want to use same variable of different values ,
then one should be global scope and other should be in local scope"""

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

"""If you want to make a local scooe a global one"""
def myfunc():
    global x
x=300
myfunc()
print(x)