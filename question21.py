"""Write a program to print the following number patterns using a loop.
a)
	1
	1 	2
	1	2	3
	1	2	3	4
	1	2	3	4	5

b)
	5	4	3	2	1
	4	3	2	1
	3	2	1
	2	1
	1
"""
a=5
for rows in range(1,a+1):
    for column in range(1,rows+1):
        print(rows,end='  ')
    print(' ')

