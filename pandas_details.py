import pandas as pd
df=pd.read_csv("custs.csv")

#to know info (structure of data)
print(df.info())

###structure datatypes
print(df.dtypes)

#rows and cols
rows,cols =df.shape

print(f"rows:{rows} columns:{cols}")

#no.of rows
print(len(df))
print(df.shape[0])

#no. of columns
print(df.shape[1])
##columns
print(df.columns)

#get index
print(df.index)

#sats info for integer
print(df.describe(include="all"))

#memory usage
print(df.memory_usage())

#unique values
print(df['custid'].unique())

##null checks
print(df.isnull().sum())
