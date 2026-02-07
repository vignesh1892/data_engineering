"""
12. Check if number is prime 
Input: 29 — Output: True 
"""
n = 29

if n <= 1:
    print(False)
else:
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            print(False)
            break
        else:
            print(True)

"""
13. Fibonacci (n-th) using iteration 
Input: n=7 — Output: 13 (sequence: 0,1,1,2,3,5,8,13)
"""
n=7
a,b=0,1
for _ in range(n):
    a,b = b,a+b
print(a)
"""

14. Remove duplicates from list (preserve order) 
Input: [1,2,2,3,1,4] — Output: [1,2,3,4] 
 
"""
lst = [1,2,2,3,1,4] 
seen = set(lst) 
res = [] 
for x in seen: 
    res.append(x) 
print(res)

"""
✅
15. Two-sum (indices) — O(n) 
Input: nums=[2,7,11,15], target=9 — Output: [0,1] 

"""
nums = [2,7,11,15]; target = 9 
d = {} 
c={}

for i,v in enumerate(nums):
    if target-v in d:
        c[v]=target-v
        break 
    d[v]=i
print(d)
print(c)

"""
✅
16.  Merge two sorted lists (like merge step) 
Input: [1,3,5], [2,4,6] — Output: [1,2,3,4,5,6] 
"""
a, b = [1,3,5], [2,4,6] 
i,j=0,0
out=[]

while i<len(a) and j<len(b):
    if a[i] < b[j]:
        out.append(a[i])
        i+=1
    else:
        out.append(b[j])
        j+=1 
out.extend(b[j:]) 
print(f"out{out}")
print(j)
print(i)
print(b[j:])
print(a[:i])
print(a[::-1])


"""
18. Flatten nested list (single level) 
Input: [[1,2],[3,4],5] — Output: [1,2,3,4,5] 
"""
nested = [[1,2],[3,4],5] 
flat = [] 
for i in nested:
    if isinstance(i,list):
        flat.extend(i)
    else:
        flat.append(i)
print("flat=",flat)

"""
✅
21. Find kth largest (using heapq) 
Input: nums=[3,2,1,5,6,4], k=2 — Output: 5 
"""
import heapq 
nums=[3,2,1,5,6,4]; k=2 
print(heapq.nlargest(k, nums)[1]) 

"""
22. Generate primes up to n (Sieve of Eratosthenes) 
Input: n=15 — Output: [2,3,5,7,11,13] 
"""
n = 15 

output=[]
for i in range(15):
    if i % 2 != 0:
        output.append(i)

print(output)

"""
 41. Find Common Elements Between Two Lists
 """ 
list1 = [1, 2, 3, 4] 
list2 = [3, 4, 5, 6] 

list3 = list(set(list1) & set(list2))
print(list3)

"""
 41. Find differnt Elements Between Two Lists
 """ 
list3 = list(set(list1) ^ set(list2))
print(list3)

"""
 42: Print Fibonacci Sequence 
 """
n = 10 
a, b = 0, 1 

for _  in range(n):
    #print(a,end=" ")
    a,b=b,a+b

"""
�
�✅
 43: Find Factorial of a Number 
"""
num = 5 
fact = 1 
for i in range(1, num + 1):
    fact*=i

print("fac:",fact)
def find_fact(n):
    if n == 0 or n == 1:
        return 1
    return n*find_fact(n-1)

"""
 45: Merge Two Dictionaries 
"""
dict1 = {'a': 10, 'b': 20} 
dict2 = {'c': 30, 'd': 40}

dict3={**dict1,**dict2}
print(dict3)

"""
 46.Count Words in a Sentence 
"""

sentence = "Python is fun and Python is powerful"
d=sentence.split(" ")
print(d)
c={}
for i in d:
    c[i]=c.get(i,0)+1
print(c)

"""
47: Find the Second Highest Number in a List 
"""
data = [10, 35, 50, 20, 35]
st=sorted(set(data))
stt=(set(data))
print(st[-2])

"""
48. Sort Dictionary by Its Values 
"""

data = {'apple': 3, 'banana': 1, 'orange': 2}

dt=dict(sorted(data.items(),key=lambda x:x[1] ))
print(dt)

"""
✅
49. Merge Two Lists into a Dictionary 
"""
keys = ['name', 'age', 'city'] 
values = ['John', 25, 'Hyderabad']
dt=dict(zip(keys,values))
print(dt)
dt=(zip(keys,values))
print(dt)
"""
✅
50. Find All Prime Numbers Between 1 and 50 
"""
d=[]
for i in range(2,51):
    for j in (2,num):
        if i % j != 0:
            d.append(i)
print(d)

"""
✅
51.: Find Common Keys in Two Dictionaries 
"""
d1 = {'a': 1, 'b': 2, 'c': 3} 
d2 = {'b': 5, 'c': 7, 'd': 9}

print(d1.keys() & d2.keys())

"""
✅
52: Remove Punctuation from a String 
"""
import string 
text = "Hello, how are you?"

c="".join(ch for ch in text if ch not in string.punctuation)
print(c)

"""
✅
53: Find Numbers Divisible by Both 3 and 5
"""
num = [i for i in range(1,51) if i %3 == 0 and i%5 ==0]
print(num)

"""
✅
54: Find Maximum Occurring Character in a String 
"""
text = "mississippi" 
freq = {} 

for i in text:
    freq[i]=freq.get(i,0)+1
print(freq)

max_= max(freq,key=freq.get)
print(max_)

"""
✅✅
 55: Flatten a Nested List 
"""

nested = [[1, 2], [3, 4, 5], [6]] 
d=[]
for i in nested:
    if isinstance(i,list):
        d.extend(i)
print(d)

"""
✅
56:: Find Missing Numbers from a Sequence 
"""
nums = [1, 2, 4, 6, 7, 9] 

max_n=max(nums)
min_n=min(nums)
d=[]
for i in range(1,max_n+1):
    if i not in nums:
        d.append(i)
print(f"d:{d}")

"""
 57: Calculate the Sum of Digits of a Number 
"""
num = 12345
total = sum(int(i) for i in str(num))
print(total)

"""
 58: Count Uppercase and Lowercase Letters 
"""
text = "HelloWorld" 
d={}
for i in text:
    if i.isupper():
        d["upper"]=d.get("upper",0)+1
    else:
        d["lower"]=d.get("lower",0)+1
print(d)

"""
 59:Find Intersection of Two Sets 
"""
set1 = {1, 2, 3, 4} 
set2 = {3, 4, 5, 6}

print(set1&set2)
"""
 60:Find the Longest Word in a Sentence 
 """
sentence = "Python makes coding enjoyable and powerful"

sent_lst=sentence.split(" ")
j=0
for i in sent_lst:
    if j > len(i):
        j=j
    else:
        j=len(i)
print(j)

"""
 83. Reverse an Integer 
num = 12345
"""
n=""
for i in str(num):
    n=i+n
print(n)

"""
 85.Find Factorial of a Number 
"""
n = 5
def fact(n):
    n*fact(n-1)

"""
 101.Find the Largest of Three Numbers
"""
a, b, c = 10, 25, 15
print(max(a,b,c))

"""
 102.Sort a List Without Using sort() 
"""
nums = [5, 2, 9, 1, 3] 

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] > nums[j]:
            nums[i],nums[j] = nums[j],nums[i]
print(nums)


"""
25. Find All Prime Numbers up to N 
"""
n = 20

for i in range(2,n+1):
    for j in range(2,int(i**0.5+1)):
        if j % 2 == 0:
            break
        else:
            print(i,end=":")

"""
 105.Find Common Elements in Two Lists 
"""
a = [1, 2, 3, 4, 5] 
b = [4, 5, 6, 7] 

print(set(a)&set(b))

"""
106. Find the Sum of All Even Numbers in a List  
"""
nums = [1, 2, 3, 4, 5, 6]

n=[i for i in nums if i%2 == 0]
print(sum(n))

a, b = 12, 18 
while b: 
    a, b = b, a % b 
print(a) 
"""
121. Find second largest number 
"""
Input=[10, 20, 5, 30, 25] 
Output=25 

print(sorted(Input,reverse=True)[1])

"""
123. Move all zeros to end
"""
Input= [0,1,0,3,12] 

h=[i for i in Input if i != 0]+[i for i in Input if i == 0]
print(h)


"""
Input: n = 987 
Output: 24 
126. Sum of digits in a number 
"""
n=987
d=(sum(int(i)) for i in str(n))
print(d)
print(sum(int(d) for d in str(n))) 

"""
✅
131. Convert list of strings to integers 
Input: ["1","2","3"] 
Output: [1,2,3] 
lst = ["1","2","3"] 
"""
Input= ["1","2","3"] 
a=[int(i) for i in Input]
print(a)
print(list(map(int,Input)))

"""
132. Calculate factorial (loop)
"""
n=5
def find_fact(a):
    if a <=1:
        return 1
    else:
        return a*find_fact(a-1)
print(find_fact(5))

"""
✅
135. Find index of element (manual search) 
Input: [10,20,30], target=20 
Output: 1 
"""
arr = [10,20,30] 
target = 20 
print(arr.index(20))


