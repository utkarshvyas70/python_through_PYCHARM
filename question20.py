"""x=lambda a,b:a-b
num=x(5,10)
print(num)"""



def name(x,b):
    return lambda a:(a+x)*b
num=name(10,6)
print(num(5))