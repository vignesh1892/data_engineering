"""
 61: Read a File and Count Number of Lines 
# Suppose "sample.txt" has some text lines
"""
with open ("F:\Studies\Big_Data\Inceptez\Azure_AI_Class\Interview Prep\Panda and Python DE\data_engineering\customers.csv","r") as prg:
    file_p=prg.readlines()
    print(len(file_p))
"""
 62: Write a List of Strings to a File 


lines = ["apple\n", "banana\n", "orange\n"] 
with open("weite_test","w") as wrt:
    wrt.writelines(lines)
"""

"""
 63: Read JSON Data from a File 
 """
import json 
file_="F:\Studies\Big_Data\Inceptez\Azure_AI_Class\Interview Prep\Panda and Python DE\data_engineering\sample.json"

with open(file_, "r") as file_1:
    file_json=json.load(file_1)
print(file_json[0]["Name"])

"""
 66: Handle File Not Found Exception
"""

try:
    with open ("test.py",'r') as testr:
        re=testr.readlines()
except FileNotFoundError as e:
    print(f"file not found provided location ,{e}")

"""
 67: Count Each Word’s Frequency in a File
"""
with open(r"F:\Studies\Big_Data\Inceptez\Azure_AI_Class\Interview Prep\Panda and Python DE\data_engineering\texts\fileA.txt", "r") as prg:
    file_p = prg.read().split()
    print(file_p)
    d={}
    for i in file_p:
        d[i]=d.get(i,0)+1
print(d)





