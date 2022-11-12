"""import sys
sys.setrecursionlimit(2000)

def hello():
    print("Hello World")
    hello()
hello()"""


"""def fact(n):
    if n==0:
        return 1

    return n * fact(n-1)

num=fact(4)
print(num)"""



def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)

a =int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
c=str(input("operator: "))

if c=="+":
    add(a,b)
elif c=="-":
    sub(a,b)
elif c=="/":
    div(a,b)
elif c=="*":
    mul(a,b)


