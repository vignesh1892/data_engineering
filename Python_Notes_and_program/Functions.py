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

"""
➤ Common Higher-Order Functions

✔ map() → Apply a function to all items in a list
✔ filter() → Filter items based on a condition
✔ reduce() → Aggregate values
✔ Custom decorators → Modify behavior of functions
"""
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)  # Output: [1, 4, 9, 16]

"""
➤ Closures vs Higher-Order Functions
| Aspect       | Higher-Order Functions          | Closures                             |
| ------------ | ------------------------------- | ------------------------------------ |
| What it does | Accepts/returns functions       | Remembers variables from outer scope |
| Focus        | Functional behavior abstraction | Maintaining state over time          |
| Use cases    | `map()`, `filter()`, decorators | Counters, data encapsulation         |
| Relationship | Closures can be used in HOFs    | Can be returned from HOFs            |

✅ Decorators in Python – Complete Explanation
➤ What is a Decorator?

A decorator is a special type of higher-order function that modifies or enhances the 
behavior of another function without changing its code. 
It “wraps” the original function, adding functionality before or after the function runs.
"""
#➤ Step 1 – Define a decorator function

def my_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper
#➤ Step 2 – Apply it to a function
@my_decorator
def say_hello():
    print("Hello!")

say_hello()





 



