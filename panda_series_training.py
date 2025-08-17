"""
Pandas Series
One-dimensional labeled array.

Holds data of a single column (any data type).

Has index and values.
"""

import pandas as pd

##coverting list to series
vdata =[1,2,3,4]
s=pd.Series(vdata)
print(s)

# access data
print(s[3])

#define custom index
s=pd.Series(vdata,index=[1,2,3,4])
print(s)

# access data
print(s[3])

#define custom index
s=pd.Series(vdata,index=["A","B","C","D"])
print(s)

#get Value
print(s.values)
#get index
print(s.index)

#accessing loc (label based)
print(s.loc['B'])
#if we need to access multiple elements to access use list of values
print(s.loc[['B','C']])

#accessing iloc (position based)
print(s.iloc[1])
#if we need to access multiple elements to access use list of values
print(s.iloc[[1,2]])

##slicing in list
print(s[0:2])

#manipulation
s = 1+s#for every element it will add value 1
print(s)
#filter
s=s[s>2]
print(s)

s = pd.Series(["INDIA", "PAK", 10, 20])
print(s)

## from dict
# Dictionary
data = {
    'a': 10,
    'b': 20,
    'c': 30
}

# Convert dict to Series
s = pd.Series(data)

print("Series from dictionary:")
print(s)
print("Index:", s.index)
print("Values:", s.values)

#sort values
print(s.sort_values())
print(s.sort_values(ascending=False))

# series can be created from all collection python datatypes (list,tuple,dict,set)
