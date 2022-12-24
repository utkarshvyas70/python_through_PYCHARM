import re
value = 'This is a srting'
ouput = re.search("^This. *string$",value)
print(ouput)

out = re.findall("T..s",value)
print(out)


out = re.findall("T.*s",value)
print(out)

out = re.search("is",value)
print(out)

out = re.split('\s',value)
print(out)

# out = re.search('list',value)
# print(out)
4