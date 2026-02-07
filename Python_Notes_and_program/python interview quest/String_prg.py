s = "aaabbca" 
result = "" 
count = 1 
o="3a2b1c1a"

for i in range(len(s)):
    if i < len(s)-1 and s[i] == s[i+1]:
        count += 1
    else:
        result = result+str(count)+s[i]
        count = 1
print(f"result={result}")

"""
19. Count words in sentence 
Input: "hello hello world" — Output: {'hello':2,'world':1} 
"""
s = "hello hello world"
d={}
lst=s.split(" ")
print(lst)
for i in lst:
    print(i)
    d[i]=d.get(i,0)+1
print(d)

"""
23. Rotate string by k (left rotate) 
Input: s="abcdef", k=2 — Output: "cdefab" 
"""
s = "abcdef"
k = 2 
print(s[k:])
print(s[:k])
print(s[k:]+s[:k])

"""
26. Count Frequency of Elements in a List Using a Dictionary 
"""

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple'] 

f={}
for i in data:
    f[i]=f.get(i,0)+1

print(f)

"""
✅
27. Variable = ‘suresh’ reverse a string with out using reverse and use for loop  
Ans. 
"""

variable = 'suresh' 
reversed_string = '' 

for char in variable:
    reversed_string = char+reversed_string

print(reversed_string)

"""
sort without sort function
"""
num = [15, 50, 5, 9, 20]
sort_num=[]
n=len(num)

for i in range(n):
    for j in range(0,n-i-1):
        if num[j] > num[j+1]:
            num[j],num[j+1] = num[j+1],num[j]
print(num)
print(num[2])

"""
31. Find Duplicatess Elements in a List 
"""

data = [1, 2, 3, 4, 2, 3, 5, 1] 

f={}

for i in data:
    f[i]=f.get(i,0)+1
print(f)
g=[]
for i,v in f.items():
    if v >1 and  i not in g:
        g.append(i)

print(g)

"""

33.write a Python program to conduct match one country with other countries  
Ans . countries = ['USA', 'India', 'Australia', 'Pakistan', 'South Africa'] 

"""
countries= ['USA','India','Australia','Pakistan','South frica']
for i in range(len(countries)): 
    for j in range(len(countries)): 
        if i != j:     # avoid matching the same country with itself 
            print(countries[i], "matches with", countries[j]) 

"""
Q. Sorting a list of dictionaries in Python: 
"""
students = [ 
{"name": "Alice", "age": 20, "grade": "A"}, 
{"name": "Bob", "age": 22, "grade": "C"}, 
{"name": "Charlie", "age": 19, "grade": "B"}, 
{"name": "David", "age": 20, "grade": "A+"}, 
{"name": "Eve", "age": 21, "grade": "B-"}, 
] 
# --- Sorting by 'age' (ascending order) – 

std=sorted(students,key= lambda x : x["age"])
print("std:",std)

"""
✅
35. Check if a String is a Palindrome 
"""
word = "madam" 
print(word[::-1])
if word == word[::-1]:
    print("yes")

"""
 36. Count Vowels in a String 
 """
text = "hello world" 
vowels = "aeiou" 
d={}
for i in text:
    if i in vowels:
        d[i]=d.get(i,0)+1
print(d)
c=0
for i in text:
    if i in vowels:
        c+=1
print(c)

"""
 37. Find Even and Odd Numbers in a List 
"""
numbers = [1, 2, 3, 4, 5, 6] 
num1=[i for i in numbers if i%2==0]
print(num1)

num1=[i for i in numbers if i%2!=0]
print(num1)

"""
 38. Remove Duplicates from a List 
"""
data = [1, 2, 3, 2, 4, 3, 5]

lst=list(set(data))
print(lst)

lst=list(dict.fromkeys(data))
print(lst)

"""
 39. Swap Two Variables Without a Temp Variable 
"""
a, b = 10, 20
b,a=a,b

"""
�
�✅
 68: Remove Empty Strings from a List 
"""
data = ["apple", "", "banana", "", "orange"] 

not_null=list(filter(None,data))
print(not_null)

"""
�
�✅
 69: Find Employee with Highest Salary 
"""
employees = [ 
{"name": "Ravi", "salary": 45000}, 
{"name": "Kiran", "salary": 52000}, 
{"name": "Anil", "salary": 48000} 
]

max_sal= max(employees,key=lambda x : x["salary"])
print(max_sal)

"""
 71: Find Unique Words from a Sentence 
"""

sentence = "Python is powerful and Python is easy" 
print(set(list(sentence.lower().split(" "))))

"""
 72: Create a Dictionary from Two Lists (Only Even Numbers) 
"""
keys = [1, 2, 3, 4] 
values = [10, 20, 30, 40] 

dict_c={k:v for k,v in zip(keys,values) if k%2 ==0}

print(dict_c)

"""
�
�✅
 73 Handle Division by Zero Error 
"""
try: 
    result = 10 / 0 
except ZeroDivisionError as e: 
    result = None 
    print("Cannot divide by zero.") 

"""
 74: Calculate Average Value from a Dictionary
"""
marks = {"Math": 80, "Science": 90, "English": 70} 
avg_val=sum(marks.values())/len(marks)
print(avg_val)
print(len(marks))
print(sum(marks.values()))

"""
 75:Find Top N Elements from a List 
"""
nums = [10, 50, 20, 80, 30, 90] 
t=3
gt=sorted(nums,reverse=True)[:t]
print(gt)

"""
 84.Count Vowels in a String 
"""
s = "interview" 
e= "aeiou"

g={}

for i in s:
    if i in e:
        g[i] = g.get(i,0)+1

print(g)

"""
 103.Count Frequency of Words in a Sentence 
"""
s = "this is a test this is only a test" 
k=s.split(" ")
print(k)
d={}
for i in k:
    d[i]=d.get(i,0)+1

print(d)

"""
 104.Check if String is Pangram (contains all alphabets) 
"""
import string 
s = "The quick brown fox jumps over the lazy dog" 

print(set(string.ascii_lowercase).issubset(s.lower()))
print(sorted(set(s.lower().replace(" ",""))))

"""
 107.Check if Two Strings are Rotation of Each Other
"""
s1 = "abcde" 
s2 = "deabc" 
print(len(s1) == len(s2) and s2 in s1 + s1) 

print(s1+s1)

"""
 108.Print Duplicate Elements from a List 
"""
nums = [1, 2, 3, 2, 4, 1, 5] 

j=[k for k in nums if nums.count(k) > 1]
print(j)


"""
 112.Remove Special Characters from a String
"""
import re 
s = "Hello@World#2025!" 
print(re.sub(r'[^A-Za-z0-9]+',"",s))

"""
 116. Merge Two Dictionaries 
"""
d1 = {'a': 1, 'b': 2} 
d2 = {'c': 3, 'd': 4} 

print({**d1,**d2})

"""
 117. Find First Non-Repeating Character 
"""
s = "aabbcde" 

for i in s:
    if s.count(i) == 1:
        print(i)
        break
"""
 119. Flatten a Nested List 
"""

nested = [[1, 2], [3, 4], [5, 6]] 

flat = [j for i in nested for j in i]
print(flat)
flat=[]
for i in nested:
    if isinstance(i,list):
        flat.extend(i)
    else:
        flat.append(i)

print(flat)

"""
 120 . Count uppercase, lowercase, digits, special characters 
"""
Input= "HeLLo123@" 

Upper=0
Lower=0 
Digits=0 
Special=0

for i in Input:
    if i.isupper():
        Upper+=1
    elif i.islower():
        Lower+=1
    elif i.isdigit():
        Digits+=1
    else:
        Special+=1
print(Upper)
print(Lower)
print(Digits)
print(Special)

"""
124. Print characters that appear more than once 
Input: "programming" 
Output: r, g, m 
"""
Input= "programming"

j=set([i for i in Input if Input.count(i) > 1])
print(j)

"""
125. Longest word in a sentence
"""
input= "Python is super powerful"

print(max(input.split(), key=len)) 
"""
127. Remove all vowels from string 
Input: "beautiful" 
Output: "btfl"
"""    
Input= "beautiful" 
r="aeiou"
k=""
for i in Input:
    if i not in r:
        k+=i 
print(k)

"""
136. Reverse words but keep order 
Input: "I love Python" 
Output: "I evol nohtyP" 
"""
Input= "I love Python" 

s=Input.split(" ")

d=str("".join(i[::-1]) for i in s)
print(d)





