mydict={
    "name":"Utkarsh",
    "age":19,
    "class":13,
    "rollno.":8
}
a=mydict.get("name")
print(mydict)
print(len(mydict))
print((a))
key=mydict.keys()
value=mydict.values()
items=mydict.items()
mydict["age"]=22
mydict.update({"age":22})
a=mydict.pop("age")
print(f"keys are {key}")
print(f"values are {value}")

mydict2={
    "class":{
        "student":{
            "name":"abc",
            "marks":{
                "python":90,
                "web":95
            }
        }
    }
}
print(mydict2["class"]["student"]["marks"]["web"])