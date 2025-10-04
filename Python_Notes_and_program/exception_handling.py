
"""
What are Exceptions?

An exception is an error that occurs during program execution and disrupts the normal flow.

Example:
"""
"""
Handling Exceptions

Use try–except-finally block.
"""
print("get input from user")
try:
    a=int(input(("Provide a input:")))

    b=int(input(("Provide b input:")))

    c=a+b
    print(f"sum of both {a} and {b} is {c}")
except ValueError as e:
    print(f"Invalid input! {e}")
finally:
    print("Execution completed!")

#Raising Exceptions
f=input("Provide your age")
f_age=int(f)
print(type(f_age))
if type(f_age) != "int":
    raise ValueError("Age cannot be negative!")



