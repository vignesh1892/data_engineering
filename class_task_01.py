"""
Basic Class & Object Creation
Create a Car class with attributes: brand, model, and year.

Add a method display_info() that prints: "Brand: Toyota, Model: Corolla, Year: 2020".

Create two Car objects and display their info.
"""
class Car():
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

carobj1=Car("Toyota","Corolla","2020")
carobj1.display_info()

carobj2=Car("Ford","ecosports","2016")
carobj2.display_info()

"""
Class with Constructor
Create a BankAccount class with:

Attributes: account_holder, balance (default 0)

Methods: deposit(amount) and withdraw(amount)

Ensure withdrawal doesn't go below 0.

Test it with multiple transactions.
"""

class BankAccount:
    def __init__(self,account_holder,balance =0):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self,amount):
        print(f"successfully deposited: {amount}, new balance is {self.balance+amount}")
        return self.balance+amount
    def withdraw(self,amount):
        if self.balance > amount:
            print(f"successfully withdraw {amount}, new balance is {self.balance-amount}")
        else:
            print(f"Account with less balance: {self.balance}")

banktr=BankAccount("Vignesh",1000)
banktr.deposit(1000)
banktr.withdraw(100)
"""
Class with Class Variables
Create a Student class:

Instance variables: name, marks

Class variable: school_name

Method to display student details.

Change the class variable and see the effect on all objects.
"""

class Student:
    school_name ="ABC"
    def __init__(self,name,marks):
        self.marks = marks
        self.name =name
    def studinfo(self,calss):
        print(f"{self.name} studies {calss} in {Student.school_name} and with marks: {self.marks}")

stud=Student("Danvik",100)
stud.studinfo("12th")
"""
Inheritance
Create a Shape base class with a method area().

Create two child classes:

Rectangle → calculate area from width and height

Circle → calculate area from radius

Create objects and print their areas.
"""

    




