import re

txt="the rain in spain"
x= re.findall("ai",txt)
print(x)

#search
import re
txt="the rain in spain"
x=re.search("s",txt)
print("The first white space character is loacated in position:",x.start())

#split
import re
txt="The rain in spain"
x=re.split("\s",txt)
print(x)

#if you want to split at a certain position
import re
txt="The rein in spain"
x=re.split("\s",txt,2)