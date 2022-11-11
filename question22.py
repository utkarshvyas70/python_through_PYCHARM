"""Write a program to display all prime numbers within a range
Take the user input for start and end of range.

Note: A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers

Examples:

6 is not a prime number because it can be made by 2×3 = 6
37 is a prime number because no other whole numbers multiply together to make it."""

minimum=int(input('min'))
maximum=int(input('max'))
for n in range(minimum,maximum+1):
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                break
        else:
            print(n)