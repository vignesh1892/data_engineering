import pandas as pd
df=pd.read_csv("custs.csv")
print(df)
# one column
dfname=df["fullname"]
print(dfname)## retrun series
print(type(dfname))

#multiple columnsf

df_multi_cols=df[["custid","fullname"]]
print(df_multi_cols)
print("=================")
#by index loc label based
df1=df.loc[0]
print(df1)
#by pos using index
df1=df.iloc[0]
print(df1)
print("=================")
#slicing 
df1=df[1:4]#rows 1 to 4
print(df1)
##iat and at
#filter
df1=df[df["age"]>25]
print(df1)
#query
df1=df.query('age == 28 and profession =="Data Analyst"')
print(df1)

# access few columns:
df1=df[["custid","age"]]
print(df1)

##loc and iloc and corresponding row that we're providing in the first param:
df2=df.loc[2,"custid"]
print(df2)
df2=df.iloc[2,0]
print(df2)

##query part 
df2=df.query("age > 28")
print(df2)

df2=df[["custid","age"]].query("age > 28")
print(df2)