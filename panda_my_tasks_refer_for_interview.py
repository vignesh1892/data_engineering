import pandas as pd
#Create a Pandas Series from a Python 
#list [10, 20, 30, 40, 50] and set custom index labels ['a', 'b', 'c', 'd', 'e']
"""
data=[10, 20, 30, 40, 50]
id=['a', 'b', 'c', 'd', 'e']

ps=pd.Series(data,index=id)
print(ps)

## access using loc (label)
ps1=ps.loc["a"]

print(ps1)

## access using iloc (index)
ps1=ps.iloc[1]

print(ps1)
"""
"""
Create a DataFrame from a dictionary:

{
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["NY", "London", "Paris", "Tokyo"]
}
and print only the Name and City columns.
"""
"""
dt={
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["NY", "London", "Paris", "Tokyo"]
}
df =pd.DataFrame(dt)
print(df)
df1=df[["Name","City"]]
print(df1)

#Read a CSV file students.csv and print the first 5 rows.

stud=pd.read_csv("students.csv")
print(stud)
stud1=stud[:5]
print(stud1)

#From the same CSV, select rows where Age is greater than 30.
stud2=stud[stud["Age"]>30]
print(stud2)
df1=stud.query('age > 30')
print(df1)

#Replace all missing values in a column Score with the value 0
fvalue={"Score":"0"}

stud_n=stud.fillna(fvalue)
print(stud_n)

"""
"""
Intermediate Level
Given a DataFrame with columns ['Name', 'Math', 'Science', 'English'],
calculate the average score for each student and store it in a new column Average.
"""
"""
markdf=pd.read_csv("marks.csv")
print(markdf)

markdf["Avgerage"]=(markdf["Math"]+markdf["Science"]+markdf["English"])/3
print(markdf)

#Sort a DataFrame by two columns — first by Age (ascending) and then by Score (descending).
stud1=stud.sort_values(by="Age",ascending=True)
print(stud1)
stud2=stud.sort_values(by="Score",ascending=False)
print(stud2)

#Filter a DataFrame to select rows where City is either "London" or "Paris"
stud1=stud[(stud["City"]=="London") | (stud["City"]=="Paris")]

print(stud1)
#Group a DataFrame by Department and calculate the average salary per department.
empdf=pd.read_csv("employees.csv")
print(empdf)
empdfavgsal=empdf.groupby("Department")["Salary"].mean()
print(empdfavgsal)

"""
"""
Merge two DataFrames:

df1: Employee ID and Name

df2: Employee ID and Salary
Keep only matching records.
"""
"""
df1=pd.read_csv("df1.csv")
print(df1)
df2=pd.read_csv("df2.csv")
print(df2)
df3=df1.merge(df2, on='EmployeeID', how='inner')
print(df3)

"""
#Given a column with dates as strings ('2025-08-14' format), 
# convert it to a Pandas datetime object and extract year and month into new columns.
schema = {"OrderID" :"int64","Customer":"string","Amount":"float64"}
saledf=pd.read_csv("sales_dates.csv",dtype=schema, parse_dates=["OrderDate"])
"""
Use dtype in read_csv to apply schema directly while loading.
Use astype() to enforce schema after DataFrame is created.
"""
print(saledf.dtypes)
print(saledf)

### another value of enforcing date:
saledf=pd.read_csv("sales_dates.csv")
saledf["OrderDate"]=pd.to_datetime(saledf["OrderDate"])
print(saledf.dtypes)
print(saledf)

saledf["Year"]=saledf["OrderDate"].dt.year
print(saledf)
saledf["Month"]=saledf["OrderDate"].dt.month
print(saledf)

#Pivot a DataFrame that contains ['Date', 'Product', 'Sales'] 
#so that each product becomes a column and sales are filled in accordingly.

prodsaldf=pd.read_csv("product_sales.csv")
print(prodsaldf)
prodsaldf=prodsaldf.pivot(index="Date",columns="Product",values="Sales")
print(prodsaldf)
##From a DataFrame with CustomerID, PurchaseAmount, and PurchaseDate, calculate:
##Total purchase amount per customer
##Number of purchases per customer
cuspurdf=pd.read_csv("customer_purchases.csv")
print(cuspurdf)
##Total purchase amount per customer
cuspuragg=cuspurdf.groupby("CustomerID")["PurchaseAmount"].sum()
print(cuspuragg)
##Number of purchases per customer
cuspuragg=cuspurdf.groupby("CustomerID")["PurchaseAmount"].count()
print(cuspuragg)

#Detect and remove duplicate rows based on Name and City columns.
cusdf=pd.read_csv("customers.csv")
print(cusdf)
cusdupdf=cusdf.drop_duplicates(subset=["Name","City"])
print(cusdupdf)

#Read a JSON file containing nested objects and flatten it into a DataFrame.
import json

with open("customers.json") as f:
    data = json.load(f)
cusdf=pd.json_normalize(data)
print(cusdf)

##Read a file and do some transformation and merge it with sql DF
with open("custs_2.txt") as f:
    custdt=f.readlines()
    print(custdt)
    custdata=[i.strip().split(",") for i in custdt[1:]]
    ##another way
    """
    custdata=[]
    for i in custdt[1:]:
        custdata.append(i.replace("\n","").split(","))
    """
    print(custdata)
import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
host = os.getenv("MYSQL_HOST")
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DATABASE")
try:
    # Connect to MySQL
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    if conn.is_connected():
        print("✅ Connected to MySQL!")

    cursor = conn.cursor()

    # Insert SQL
    insert_sql = """
        INSERT INTO tblcustomer_vignesh (custid, fullname, age, profession)
        VALUES (%s, %s, %s, %s)
    """

    # Insert multiple rows
    cursor.executemany(insert_sql, custdata)
    conn.commit()
    print(f" {cursor.rowcount} rows inserted.")

except Error as e:
    print(f" Error while working with MySQL: {e}")

finally:
    if cursor:
        cursor.close()
    if conn and conn.is_connected():
        conn.close()
        print("🔒 Connection closed.")
















