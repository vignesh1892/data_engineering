"""
�
�✅
 64: Sort List of Dictionaries by a Key 
"""
employees = [ 
{"name": "Ravi", "age": 28}, 
{"name": "Anil", "age": 22}, 
{"name": "Kiran", "age": 35} 
] 
sorted_val=sorted(employees,key= lambda x :x["age"])
print(sorted_val)

"""
 65: Filter Records Using lambda and filter() 
"""
numbers = [10, 25, 30, 45, 50, 60] 

x=list(filter(lambda x : x % 10 ==0,numbers))
print(x)