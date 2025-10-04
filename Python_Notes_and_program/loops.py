print("✅ 1. for loop with a List")#same approach for tuple and set
fruits = ["apple", "banana", "cherry"]
for val in fruits:
    print(val)
#enumerate
for i,val in enumerate(fruits):
    print(f"loop no: {i}, value: {val}")

print("✅ 2. for loop with a Dictionary")
student = {"name": "Vignesh", "age": 25}
for i in student.keys():
    print(i)
for i in student.values():
    print(i)
for k,v in student.items():
    print(f"Key: {k}, value: {v}")

print("✅ 3. Nested for Loops with Collections")
students = [
    {"name": "Vignesh", "age": 25},
    {"name": "Ravi", "age": 23}
]
for student in students:
    for key, value in student.items():
        print(f"{key}: {value}")
    print("------")


