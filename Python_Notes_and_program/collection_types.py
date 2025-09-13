"""
List:
    collection type of ordered and muttable datatype
    Support hetrogenous datatypes => e.g. ["spark",1,True]
"""
list1=[1,2,4,5,100,54]
#Adding a element to list at last
list1.append(88)
print(list1)
#Adding a element to list to a specific index
list1.insert(1,333)
print(list1)
#update existing element:
list1[0]=3
print(list1)
#Delete option
list1.pop(0)#using index
print(list1)
list1.remove(333)#using value
print(list1)
del list1[0]#using index
print(list1)
#clear all elements
list2=[2,4]
list2.clear()
print(list2)

#integer functions:
    #max,min,sum
#total no. of elements:
print(len(list1))

#sort function
print(sorted(list1,reverse=True))

"""Tuple:
        Immutable datatype(append,insert,remove,etc not supported)
        Accessing,hetro datatypes are same as list
        sort function will create another function
"""
#converting list to tuple and vice-versa
tuple1=tuple(list1)
print(tuple1)
list3=list(tuple1)
print(list3)

"""
Dict:
    Muttable datatype
    Key-value format json format
    key must be unique, immuttable and diff datatypes
    value can be dups, muttable and diff datatypes
    e.g. dict1={"name":"Vignesh",90:100}

"""
#Create dict :
#Using curly braces {}
student = {"name": "Vignesh", "age": 25}
#Using dict() constructor
stud=dict(name="vignesh",age=23)
print(stud)
#Using zip():
keys = ["name", "age"]
values = ["Vignesh", 25]
student = dict(zip(keys, values))
print(student)

print("✅ Accessing Values")
print(student["name"])
#Use get() to avoid errors if the key doesn’t exist
print(student.get("mobile"))

print("✅ Updating a Dictionary")
print("Add or update an item:")
print("Add element")
student["mobile"]=99900
print(student)
print("update element")
student["mobile"]=7789
print(student)
print("Using update(), used to update and add at one shot")
student.update({"city": "Chennai", "age": 27,"mobile":77899})
print(student)

print("✅ Removing Items")
student.pop("age")#using key 
student.update({"city": "Chennai", "age": 27,"mobile":77899})
print("Remove and return last inserted item using popitem():")
print(student.popitem())
print(student)
del student["mobile"]#using delete
print(student)
print("Clear all items:")
student.clear()

print("✅ Dictionary Operations")
student = {
    "name": "Vignesh",
    "age": 25,
    "course": "Data Engineering"
}

print("Check if key exists:")
if "name" in student:
    print("Name exists")
for key in student:
    print(key, student[key])
for key, value in student.items():
    print(key, value)

print("Creates a new dictionary with default values")
keys = ["a", "b", "c","a"]
new_dict=dict.fromkeys(keys)
print(new_dict)


