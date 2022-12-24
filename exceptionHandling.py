# try:
#     f=open('demofile.txt.py')
#     try:
#         f.write('ABC')
#     except:
#         print('Error in file')
#     finally:
#         f.close()
try:
    a=10/0
    print(a)
except ArithmeticError:
    print('this statement is raising an arithmetic progregession')
else:
    print('Success.')
# a = 5
# if a <10:
 #     raise Exception('Value is less than 5')

