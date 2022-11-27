# Wedding code
Groom=str(input("Enter the name of the Groom: \n"))
Bride=str(input("Enter the name of the Bride: \n"))
print(f"Congratulations Mr.{Groom} and Mrs.{Bride}, you are now happily married ")

tuple2=("fkjefij",1,2,3,4,5)
print(len(tuple))
print(tuple[:3])
list1=list(tuple2)
list1.append(5)
print(list1)
tuple1=tuple(list1)
print(tuple1)

tuple1=(10,20,30,40)
list1=list(tuple1)
list1.reverse()
tuple2=tuple(list1)
print(tuple2)

tuple1=("Utkarsh" ,"Vyas")
print(tuple1)
del tuple1

tuple1=(1,2,3,[6,7],4,5)
tuple1[3][0]=8
print(tuple1)

tuple1=(10,20)
tuple2=(30,40)
tuple1,tuple2=tuple2,tuple1
print(tuple1)
print(tuple2)








