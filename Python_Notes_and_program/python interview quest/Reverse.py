"""
✅ 2. Reverse each word in a sentence 
Input: "hello world" 
Output: "olleh dlrow" 
"""
s = "hello world" 
words=s.split(" ")
res_list=[]
for word in words:
    res_list.append(word[::-1])

print(res_list)

result = " ".join(res_list)
print(result)
    
t= " ".join(word[::-1] for word in words)

print(t)

"""
 3. Find first non-repeating character 
Input: "aabbcddde" 
Output: c 
"""

s = "aabbcddde" 
d=set(s)
print(f"d:{d}")
for i in d:
    c= s.count("i")
    if c == 1:
        break
    print(f"i:{i}")
print(f"count= {s.count("a")}")

"""
✅
 4. Count vowels in a string 
Input: "engineering" 
Output: e=3, i=2 
"""
s = "engineering" 
vowels = "aeiou" 
freq = {} 

for i in s:
    if i in vowels:
        freq[i]= freq.get(i,0)+1

print(f"freq:{freq}")

"""
✅
 5. Remove duplicates but keep order 
Input: "banana" 
Output: "ban" 
"""

s = "banana" 
result = "" 
d=[]
for i in s:
    if i not in d:
        d.append(i)

f="".join(d)
print(f)

"""

 6. Check if two strings are anagrams 
Input: "silent", "listen" 
Output: True 
"""
s1 = "silent" 
s2 = "listen" 

if sorted(s1) == sorted(s2):
    print("True")

"""
✅
 7. Frequency of each character 
Input: "malayalam" 
Output: {'m':2,'a':4,'l':2,'y':1} 
"""
s = "malayalam" 
freq = {} 

for i in s:
    freq[i]=freq.get(i,0)+1

print(f"freq:{freq}")

"""

 8. Find max occurring character 
Input: "success" 
Output: s 
"""
s = "success" 
freq = {} 
for i in s:
    freq[i] = freq.get(i,0)+1

print(max(freq,key=freq.get))

"""
✅
 10. Reverse a string using loop (interview favourite) 

"""
s = "suresh" 
rev = "" 
for i in s:
    rev= i+rev
print(rev)