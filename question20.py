"""x=lambda a,b:a-b
num=x(5,10)
print(num)"""



def name(x):
    return lambda a:a+x
num=name(10)
print(num(5))