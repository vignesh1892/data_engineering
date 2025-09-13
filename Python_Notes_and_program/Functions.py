"""
✅ Functions in Python – Detailed Notes

A function is a block of reusable code that performs a specific task. 
Functions help organize code, avoid repetition, and make programs more readable and maintainable.
"""
#Anonymous Functions (Lambda Functions)
#Syntax: lambda arguments: expression

add = lambda x,y : x+y
print(add(1,2))
#Use case – with map()
nums = [1, 2, 3]
squared = list(map(lambda x: x**2, nums))
print(squared)
#Recursive Functions: A function that calls itself.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

"""
Variable-length Arguments

*args → for non-keyword arguments.

**kwargs → for keyword arguments.
"""
def fun(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

fun(1, 2, 3, name="Vignesh", age=25)

print("✅ Docstrings")
def greet(name):
    """Returns a greeting message for the given name."""
    return f"Hello, {name}!"
print(greet.__doc__)

"""
| Type         | Description                                   |
| ------------ | --------------------------------------------- |
| Built-in     | Predefined functions in Python                |
| User-defined | Functions created by programmers              |
| Lambda       | Anonymous, single-expression functions        |
| Recursive    | Functions that call themselves                |
| Higher-order | Functions taking or returning other functions |
✅ 2. Closure Functions – In-depth
➤ Definition

A closure is a function object that “remembers” 
values from its enclosing scope, even after that scope has finished executing.
"""
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

my_counter = counter()
print(my_counter())  # Output: 1
print(my_counter())  # Output: 2
"""
✅ 1. Higher-Order Functions – In-depth
➤ Definition

A Higher-Order Function (HOF) is a function that:

Accepts one or more functions as arguments, and/or

Returns a function as its result.

This means that functions in Python 
are first-class objects — you can pass them around just like any other value.
"""
def greet(name):
    return f"Hello, {name}!"

def call_func(func, value):
    return func(value)

print(call_func(greet, "Vignesh"))

def outer():
    def inner():
        return "This is the inner function"
    return inner

fn = outer()
print(fn())



 



