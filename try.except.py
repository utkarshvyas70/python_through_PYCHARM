#TryExcept
try:
    print(x)
except:
    print("An Error Ocurred")

#TryExceptElse
try:
    print(x)
except:
    print("AN error can be ocurred because x is not defined yet")
else:
    print("Nothing went wrong")

#TryExceptFinally
try:
    print(x)
except:
    print("AN error can be ocurred")
finally:
    print("The'tryexcept'is finished")

#raiseException
x=-1
if x>0:
    raise Exception("Sorry , no numbers below zero")

