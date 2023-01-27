# class hfhf:
#
#     def __init__(self,cpu,ram):
#         self.cpu=cpu
#         self.ram=ram
#
#     def computer(self):
#         print("config is", self.cpu,self.ram)
#
# a=hfhf("i5","16")
# b=hfhf("Ryzen","8")
# # hfhf.computer(a)
# # hfhf.computer(b)
# a.computer()
# b.computer()

# class computer:
#
#     def __init__(self,fname,lname):
#         self.a=fname
#         self.b=lname
#
#     def c(self):
#         print("Full name is",self.a,self.b)
#
# a=computer("Utkarsh","Vyas")
# b=computer("Elvish","Yadav")
#
# a.c()
# b.c()


# class computer:
#     pass
#
#
# c1=computer()
# print(id(c1))

# a=4
# b="v fjv fv"
# if a==b

# def is_strong_number_(num):
# digits=[int(x) for x in str(num)]
# factorial_sum=sum([factorial] for x in digit)



# Prompt user for option
# import os
# option = input("Enter option (1, 2, or 3): ")
#
# if option == "1":
#     # Count number of lines in file
#     with open("Primary.txt", "r") as f:
#         lines = f.readlines()
#     print(f"Number of lines: {len(lines)}")
#
# elif option == "2":
#     # Move cursor to user-specified position and print rest of file
#     position = int(input("Enter position: "))
#     with open("Primary.txt", "r") as f:
#         f.seek(position)
#         print(f.read())
#
# elif option == "3":
#     # Copy file and print contents in uppercase
#     with open("Primary.txt", "r") as f1:
#         with open("Secondary.txt", "w") as f2:
#             f2.write(f1.read())
#     with open("Secondary.txt", "r") as f:
#         print(f.read().upper())
#
# else:
#     print("Invalid option.")


# a=input("a: ")
# b=input("b: ")
# if a==b:
#     for i in range(0,5):
#         squares=i**2
#         print("Square of",i,"is",squares)
# elif:
#     for i in range(int(a),int(b)):
#         multiply=i*2
#         print(multiply)
# elif a!=b:
#     for i in range(10,20):
#         sqrt=i**0.5
#         print("Square root",i,"is",sqrt)
#
# list1=['a','b','c','d','e','f','g','h','i']
# list2=[]
# print(len(list1))

#fibo
# n=int(input())
# x=0
# y=1
# z=0
# while z<=n:
#     print(z)
#     x=y
#     y=z
#     z=x+y

# pattern
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print()
#     i=i+1

# hybrid
# user=input("Enter the elements of a string seperated by a comma.")
#
# index1=(input())
# list1=user.split()
# print('list is: ',list1)
# try:
#     for i in range(len(list1)):
#         list1[i]=int(list1[i])
# except:
#     print("list index out of range")
# finally:
#     print("Error Handeled")
# n=int(input())
# def palindrome():
#     n_string=str(n)
#     size_n=len(n_string)
#     reversed_n=n_string[size_n::-1]
#     print(reversed_n)
# palindrome()
# def prime_no():
#     if n%1==0 and n%n==0:
#         print()
#
# def hybrid():
#     if n==palindrome() and n==prime_no():
#         print("It's an hybrid number.")
# if n==hybrid():
#     print("It's an hybrid number.")
# else:
#     print("gnb")





# fibo and fact
#
# n=int(input())
# class computation:

# def factorial1(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial1(n - 1)
#
#
# result = factorial1(n)
# print(result)
#          # prints 120






# def fibo(n):
#     n = int(input())
#     x = 0
#     y = 1
#     z = 0
#     while z <= n:
#         print(z)
#         x = y
#         y = z
#         z = x + y
#
#
# result1 = fibo(n)
# print(result1)







# jersy
# li=[int(i) for i in input().split(" ")]
# d={}
# d['2']=0
# d['3']=0
# d['5']=0
# for i in li:
#     if i%2==0:
#         d['2']+=1
#     if i%3==0:
#         d['3']+=1
#     if i%5==0:
#         d['5']+=1
# print(d)






# n=int(input())
# x=0
# y=1
# z=0
# while z<=n:
#     print(z)
#     x=y
#     y=z
#     z=x+y








# list1=[int(i) for i in input().split(" ")]
# d={}
# d['2']=0
# d['5']=0
# d['7']=0
# for i in list1:
#     if i%2==0:
#         d['2']+=1
#     if i%5==0:
#         d['5']+=1
#     if i%7==0:
#         d['7']+=1
# print(d)
# n=int(input("E: "))





# def factorial(n):
#
#     if n==0:
#         return 1
#     else:
#        return n*factorial(n-1)
# result=factorial(n)
# print(result)





# def fibo(n):
#     n = int(input("e: "))
#     x=0
#     y=1
#     z=0
#     while (z<=n):
#         print(z)
#         x=y
#         y=x
#         z=x+y
# result=fibo(n)
# print(result)







# n=int(input("F:\n"))
# def pal():
#     n_string=str(n)
#     n_siz=len(n_string)
#     n_reversed=n_string(n_siz[::-1])
#     print(n_reversed)
# pal()
# def palindrome():
# n=int(input())
# def palindrome():
#     n_string=str(n)
#     size_n=len(n_string)
#     reversed_n=n_string(size_n[::-1])
#     print(reversed_n)
# palindrome()





# n=int(input("E: "))
# def prime_no():
#     if n%1==0 and n%n==0:
#         print("It's a prime no.")
#     else:
#         print("NOT")
# prime_no()





# squares=[]
# m=int(input("Enter the list: "))
# string_m=str(m)
# for num in range(m+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#             else:
#                 print(num)
#                 squares.append(num**2)
# print(squares)






# squares=[]
# m=int(input("Enter the number: "))
# strin_m=str(m)
# for num in range(m+1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)
#            squares.append(num**2)
# print(squares)





# list1=[int(i) for i in input().split(" ")]
# d={}
# d['2']=0
# d['5']=0
# d['7']=0
# for i in list1:
#     if i%2==0:
#         d['2']+=1
#     if i%5==0:
#         d['5']+=1
#     if i%7==0:
#         d['7']+=1
# print(d)





# dictionary
# keys = input("Enter keys separated by commas: ").split(',')
# values = input("Enter values separated by commas: ").split(',')
# d = dict(zip(keys, map(int, values)))
# print(d)
# m=str(input("Enter a key."))
# for i in d:
#     if m in keys:
#         print("Yes")
#     else:
#         print("no")



# Elon musk

# n=eval(input("n:"))
# count=0
# l1=[]
# for i in range(n):
#     a=input()
#     l1.append(a)
# print(l1)
# for j in l1:
#     if j==j[-1::-1]:
#         count+=1
# print(count)









# 5
# class Parent:
#     def number(self,n):
#         if n==0:
#             print('Zero')
#             return
#         isPostive=False
#         if n>=0:
#             isPostive=True
#         x=2**5
#         if x==n or -x==n:
#             if isPostive:
#                 print(f'Postitve and perfect')
#             else:
#                 print(f'Negative and perfect')
#         else:
#             if isPostive:
#                 print(f'positive and perfect')
#             else:
#                 print(f'negative and perfect')

# class Child(Parent):
#     def number(self,n):
#         if n==0:
#             print('Zero')
#             return
#         isPostive=False
#         if n>=0:
#             isPostive=True
#         x=2**5
#         if x==n or -x==n:
#             if isPostive:
#                 print(f'Postitve and perfect')
#             else:
#                 print(f'Negative and perfect')
#         else:
#             if isPostive:
#                 print(f'positive and perfect')
#             else:
#                 print(f'negative and perfect')
#
# a=Child()
# num=int(input())
# a.number(num)








# computation
# class Computation:
#     def palindrome(self,n):
#         n_string=str(n)
#         n_size=len(n_string)
#         n_reversed=n_string(n_size[::-1])
#         print(n_reversed)
#
#     def fibonacci(self,n):
#         x=0
#         y=1
#         z=0
#         while z <= n:
#             print(z)
#             x=y
#             y=z
#             z=x+y
#
#     def factorial(self,n):
#         if n==0:
#             return 1
#         else:
#             return n*(n-1)
#
# a=Computation()
# num=int(input("Enter the number: "))
# a.fibonacci(num)
# a.factorial(num)








# strong number.
# import math
# a=int(input("Enter the number: "))
# b=[]
# for number in range(1,a+1):
#     temp=number
#     sum=0
#     while(temp>0):
#         reminder=temp%10
#         factorial=math.factorial(reminder)
#         sum=sum+factorial
#         temp=temp//10
#     if sum==number:
#         b.append(number)
# print(b)








# squares=[]
# n=int(input("Enter the number: "))
# n_string=str(n)
# for num in range(n+1):
#     if num > 1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)
#             squares.append(num ** 2)
#
# print(squares)









# list1=[int(i) for i in input().split(" ")]
# d={}
# d['2']=0
# d['5']=0
# d['7']=0
# for i in list1:
#     if i%2==0:
#         d['2']+=1
#     if i%5==0:
#         d['5']+=1
#     if i%7==0:
#         d['7']+=1
# print(d)





# keys=input("Enter the keys seperated by comma: ").split(",")
# values=input("Enter the values seperated by comma: ").split(",")
# d=dict(zip(keys,map(int,values)))
# # d = dict(zip(keys, map(int, values)))
# print(d)
# m=str(input("Enter a key value: "))
# for i in d:
#     if m in keys:
#         print("Yes")
#     else:
#         print("No")






# n=eval(input("Enter the number of string you want: "))
# li=[]
# count=0
# for i in range(n):
#     a=input()
#     li.append(a)
# print(li)
# for j in li:
#     if j==j[-1::-1]:
#         count+=1
# print(count)

# n=eval(input("n:"))
# li=[]
# count=0
# for i in range(n):
#     a=input()
#     li.append(a)
# print(li)
# for j in li:
#     j==j[-1::-1]
#     count+=1
# print(count)