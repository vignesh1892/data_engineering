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
new_dict=dict.fromkeys(keys,7)
print(new_dict)
"""
| Method                       | Description                                                       |
| ---------------------------- | ----------------------------------------------------------------- |
| `dict.get(key)`              | Safely get a value                                                |
| `dict.keys()`                | Returns all keys                                                  |
| `dict.values()`              | Returns all values                                                |
| `dict.items()`               | Returns all key-value pairs                                       |
| `dict.update()`              | Updates the dictionary with another dictionary or key-value pairs |
| `dict.pop(key)`              | Removes the key and returns its value                             |
| `dict.popitem()`             | Removes and returns the last inserted item                        |
| `dict.clear()`               | Removes all items                                                 |
| `dict.copy()`                | Returns a shallow copy                                            |
| `dict.fromkeys(keys, value)` | Creates a new dictionary with default values                      |

"""

"""
set: 
    unordered collections, unindexed
    muttable
    unique value
    can't put list or dict inside set, can put tuple, number and string basically it can have immutable dataypes.
"""


print("✅ Create a Set")
my_set = {1, 2, 3, 4}
myset=set(1,3,3)#Using the set() constructor

print("✅ Set Operations")
my_set.add(9)#Adds 9 to the set
print(my_set)
#Updating with Multiple Elements
my_set.update([6, 7, 8])
print(my_set)
#Removing Elements
#remove(): Raises an error if the element is not found.
my_set.remove(2)
#discard(): Does not raise an error if the element is not found.
my_set.discard(10)
#pop(): Removes and returns a random element.
item = my_set.pop()

print("✅ Set Operations (Mathematical)")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

#Union

#All elements from both sets.

print(A | B)  # Output: {1, 2, 3, 4, 5, 6}
print(A.union(B))

#Intersection

#Elements common to both sets.

print(A & B)  # Output: {3, 4}
print(A.intersection(B))

#Difference

#Elements in A but not in B.

print(A - B)  # Output: {1, 2}
print(A.difference(B))

#Symmetric Difference

#Elements in either A or B but not both.

print(A ^ B)  # Output: {1, 2, 5, 6}
print(A.symmetric_difference(B))


""""
| Method                        | Description                                  |
| ----------------------------- | -------------------------------------------- |
| `add(x)`                      | Adds element `x`                             |
| `update(iterable)`            | Adds multiple elements                       |
| `remove(x)`                   | Removes `x`, error if not found              |
| `discard(x)`                  | Removes `x`, no error if not found           |
| `pop()`                       | Removes and returns an arbitrary element     |
| `clear()`                     | Removes all elements                         |
| `union(other)`                | Returns union set                            |
| `intersection(other)`         | Returns intersection set                     |
| `difference(other)`           | Returns difference set                       |
| `symmetric_difference(other)` | Returns symmetric difference set             |
| `issubset(other)`             | Checks if current set is subset of `other`   |
| `issuperset(other)`           | Checks if current set is superset of `other` |

"""