import pandas as pd
#Create a Pandas Series from a Python 
#list [10, 20, 30, 40, 50] and set custom index labels ['a', 'b', 'c', 'd', 'e']
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
Create a DataFrame from a dictionary:

python
Copy
Edit
{
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["NY", "London", "Paris", "Tokyo"]
}
and print only the Name and City columns.
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

#Replace all missing values in a column Score with the value 0
fvalue={"Score":"0"}

stud_n=stud.fillna(fvalue)
print(stud_n)

"""
Intermediate Level
Given a DataFrame with columns ['Name', 'Math', 'Science', 'English'],
calculate the average score for each student and store it in a new column Average.
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
Merge two DataFrames:

df1: Employee ID and Name

df2: Employee ID and Salary
Keep only matching records.
"""
df1=pd.read_csv("df1.csv")
print(df1)
df2=pd.read_csv("df2.csv")
print(df2)
df3=df1.merge(df2, on='EmployeeID', how='inner')
print(df3)


