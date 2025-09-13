import pandas as pd

df = pd.read_csv("emp.csv",sep=",",names=["EMPLOYEE_ID","FIRST_NAME","LAST_NAME","EMAIL","PHONE_NUMBER","HIRE_DATE","JOB_ID","SALARY","COMMISSION_PCT","MANAGER_ID","DEPARTMENT_ID"])

print(df)
## select "EMPLOYEE_ID","FIRST_NAME","LAST_NAME","SALARY","COMMISSION_PCT","MANAGER_ID","DEPARTMENT_ID"
df1=df[["EMPLOYEE_ID","FIRST_NAME","LAST_NAME","SALARY","COMMISSION_PCT","MANAGER_ID","DEPARTMENT_ID"]]
print(df1)
## conver FN LN to Name
df1["Name"]=df1["FIRST_NAME"]+" "+df1["LAST_NAME"]
df1.drop(["FIRST_NAME","LAST_NAME"],axis=1,inplace=True)
print(df1)
## select highest sal
print(df1["SALARY"].max())
max_sal=df1["SALARY"].max()
max_df=df1.query("SALARY==@max_sal")
print(max_df)
## select lowest sal
print(df1["SALARY"].min())
min_sal=df1["SALARY"].min()
min_df=df1.query("SALARY==@min_sal")
print(min_df)
## dept wise sum of sal
df3=(df1.groupby(["DEPARTMENT_ID"]).agg(total_sal=("SALARY","sum")).reset_index().sort_values(by="total_sal",ascending=True))
print(df3)
## join with dept df and save into another csv
dept_df=pd.read_csv("dept.csv",names=["DEPARTMENT_ID","DEPARTMENT_NAME","MANAGER_ID","LOCATION_ID"])
print(dept_df)

df4=df3.merge(dept_df,on="DEPARTMENT_ID",how="inner")
print(df4)



