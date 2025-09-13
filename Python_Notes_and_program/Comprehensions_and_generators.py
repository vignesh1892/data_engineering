"""
✅ 1. What are Comprehensions?

Comprehensions are compact, elegant ways to create collections like lists, sets, or dictionaries in a single line of code. They are more readable and efficient than using loops.

Types of comprehensions:

List comprehension

Set comprehension

Dictionary comprehension

✅ List Comprehension

Syntax:

[expression for item in iterable if condition]
"""
#Example – Squares of numbers:
sq=[i**2 for i in range(4) if i>0]
print(sq)
#find odd numbers
od=["old" if i%2 != 0 else "even" for i in sq]
print(od)
##same logic for set
## Dict:
oddict = {i: "odd" if i % 2 != 0 else "even" for i in sq}
print("oddict:",oddict)
square_dict = {x: x**2 for x in range(5)}
print(square_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

"""
✅ 2. What are Generators?

A generator is a special type of iterator that produces items one at a time as needed, instead of storing them all in memory.

Generators are more memory-efficient, especially for large datasets or infinite sequences.

➤ Creating Generators

Generator expressions (similar to comprehensions but with parentheses).

Generator functions (using yield instead of return).

✅ Generator Expressions

Syntax:

(expression for item in iterable if condition)


Example:

gen = (x**2 for x in range(5))
"""


