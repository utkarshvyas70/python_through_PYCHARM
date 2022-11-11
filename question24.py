'''Using a for loop and .append() method append each item with a Dr. prefix to the lst.

list1=["Phil", "Oz", "Seuss", "Dre"]'''
a=int(input("number:"))
c=[]
for i in range(0,a):
    b=str(input("string: "))
    if "Dr." in b:
        c.append(b)
print(c)
