"""

Pandas DataFrame
Two-dimensional labeled data structure.

Like a table with rows and columns.

Each column is actually a Series.
"""

import pandas as pd
import os
import logging
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
"""
sdata={"Name":["Varun","Karthik"],"Age":[25,30]}
s=pd.DataFrame(sdata)
print(s)

#list of dict
data=[{'Name':'Varun','Age':25},{'Name':'Karthik','Age':30}]
s=pd.DataFrame(sdata)
print(s)

#DF from multiple series
# Series 1
names = pd.Series(["Alice", "Bob", "Charlie"])

# Series 2
ages = pd.Series([25, 30, 35])

# Create DataFrame
df = pd.DataFrame({
    "Name": names,
    "Age": ages
})
print(df)
"""
##reading csv file
custdf=pd.read_csv("custs.csv",sep=",",header=None,names=["Customer_id","Name","Age","Profession"])
print(custdf)


#First five lines:
custdf.head()

#Top 3:
custdf.head(3)

#bottom5 :
custdf.tail()

#bottom 4 :
custdf.tail(4)
#ignore last 4 rows
custdf.head(-4)

### save to xl
"""
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("sample.xlsx", index=False)  # index=False so no extra index column
print("Sample Excel file created: sample.xlsx")
"""
#read xl
df=pd.read_excel("sample.xlsx",sheet_name=None)
print(df)
"""
df-pd.read_json("sample.json")
print(df)
"""
#read from mysql
conn= mysql.connector.connect(host = os.getenv("MYSQL_HOST"),
                              user = os.getenv("MYSQL_USER"),
                              password = os.getenv("MYSQL_PASSWORD"),
                              database = os.getenv("MYSQL_DATABASE")
                              )

df =pd.read_sql("SELECT * FROM tblcustomer",conn)
print(df)
