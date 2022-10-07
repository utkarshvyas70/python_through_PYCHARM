f=open("demofile.txt","r")
print(f.read())

#you want to read certain number of characters only
f=open("demofile.txt","r")
print(f.read(24))

#want to read only first line
f=open("demofile.txt","r")
print(f.readline())
f.close()

#want to read many lines
f=open("demofile.txt","r")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()