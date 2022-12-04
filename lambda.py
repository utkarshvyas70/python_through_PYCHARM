#The power of lambda is better shown when you use them as an anonymous function inside another function.
#Say you have a funtion definition that takes one argument, and that argument will be multiplied with an unkown number
def myfunc(n):
    return lambda a:a*n
    mydoubler =myfunc(2)
    mytripler=myfunc(3)
    print(mydoubler(11))
    print(mytripler(11))
# ---------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------
# 4dec
def iseven(i):
    return i%2==0
def isodd(i):
    return i%2!=0
# ------------------------------------------------------------------------------------------------------------------------------------
# list1=[3,2,8,16,11,34,17]
# # out=list(filter(lambda i:i%2==0,list1))
# # print(out)
# # put=list(filter(lambda i : i>15,list1))
# # print(put)
# -----------------------------------------------------------------------------------------------------------------------------------
