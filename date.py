#import the datetime module and display the current date

import datetime
x=datetime.datetime.now()
print(x)

#Returns the year and name of weekday
import datetime
x=datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

#if you want a specific date
import datetime

x= datetime.datetime(2003, 8, 20)

print(x)


