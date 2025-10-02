"""
What is Inheritance in Python

Inheritance is an object-oriented programming (OOP) concept where a class (child/subclass) derives properties and methods from another class (parent/superclass). It allows code reuse, modularity, and extensibility.

Parent/Superclass: The class whose properties/methods are inherited.

Child/Subclass: The class that inherits properties/methods from the parent.
"""

"""
Types of Inheritance in Python
a) Single Inheritance

A child class inherits from only one parent class.
"""

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet_child(self):
        print("Hello from Child")

c = Child()
c.greet()       # Parent method
c.greet_child() # Child method

"""
b) Multiple Inheritance

A child class inherits from more than one parent class.
"""
class Father:
    def father_skill(self):
        print("Programming")
class Mother:
    def mother_skill(self):
        print("cooking")
class Child(Father,Mother):
    pass

c= Child()
c.father_skill()
c.mother_skill()
"""
Multilevel Inheritance

A chain of inheritance where Child inherits from Parent, and Grandchild inherits from Child.
"""

class Grandparent:
    def method1(self):
        print("Grandparent method")

class Parent(Grandparent):
    def method2(self):
        print("Parent method")

class Child(Parent):
    def method3(self):
        print("Child method")

c = Child()
c.method1()
c.method2()
c.method3()


