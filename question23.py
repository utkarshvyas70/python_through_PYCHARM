"""Display Fibonacci series up to 10 terms
The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it.
The first two numbers are 0 and 1.

For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.

Expected output:

Fibonacci sequence:
0  1  1  2  3  5  8  13  21  34"""
b=[0,1]
N=10
c=3
while c<N+1:
    vale=b[c-2]+b[c-3]
    b.append(vale)
    c=c+1
print("Your desired Fibonacci series: ", b)
