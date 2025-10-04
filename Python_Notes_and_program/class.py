"""
What is a Class?

A class is a blueprint for creating objects.

Objects are instances of classes.

Classes bundle together data (attributes) and functions (methods).
"""
class profile:
    age = 32
    def __init__(self,name,place):
        self.name = name
        self.place = place
    def intro(self):
        print(f"Im {self.name} living at {self.place} and age:{self.age}")

#Creating Objects
pro= profile("vignesh","saidapet")
pro.intro()
"""
__init__ → special method (constructor) called when an object is created.

self → refers to the current object.

age → class attribute (same for all objects).

name, place → instance attributes (unique per object).
"""

"""
Types of Methods in a Class

1. Instance Method
    Works with instance data (self).
    Most common method type.
"""
print("Example of instance method:")
class profile:
    age = 32
    def __init__(self,name,place):
        self.name = name
        self.place = place
    def intro(self):
        print(f"Im {self.name} living at {self.place} and age:{self.age}")
#intro => is the instance method

"""
2.Class method:
    Works with class data (cls).
    Can modify class-level attributes.
"""
print("Example of class method:")
class profile:
    age = 32
    def __init__(self,name,place):
        self.name = name
        self.place = place
    def intro(self):
        print(f"Im {self.name} living at {self.place}")
    @classmethod
    def addinfo(cls):
        cls.age = 30
        print(f"My age:{cls.age}")

pr=profile("vignesh","chennai")
pr.addinfo()
#here addinfo is the class method and age is class variable, its getting updated here

"""
Static Method (@staticmethod)
    Independent utility function inside class.
    Does not use self or cls.
"""
print("Example of class method:")
class profile:
    age = 32
    def __init__(self,name,place):
        self.name = name
        self.place = place
    def intro(self):
        print(f"Im {self.name} living at {self.place}")
    @classmethod
    def addinfo(cls):
        cls.age = 30
        print(f"My age:{cls.age}")
    @staticmethod
    def mydream(dream):
        print(f"My dream:{dream}")

pr=profile("vignesh","chennai")
pr.mydream("Product which will speak for years and years")
#here addinfo is the class method and age is class variable, its getting updated here




