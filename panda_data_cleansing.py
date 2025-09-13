import pandas as pd
df=pd.read_csv("custs.csv")

print(df["profession"].unique())

#count of each value
print(df["profession"].value_counts())

#max value
df["age"].max()
#other functions
df["age"].mean()
df["age"].median()
df["age"].sum()
df["age"].min()

##remove null values
df.dropna()

#replace null values
#with 0
df.fillna(0)

#with sepcific values
fvalue={"age":"0","Profession":"NA"}
df.fillna(value=fvalue)

#####cleansing on an file:

df= pd.read_csv("transactions.csv",names =["Txn_ID","User_ID","Product_ID","Amount","Txn_Date","State","City"])

print(df)

## count of rows
print(df.shape[0])
print(len(df))

## select columns
df2=df[["Txn_ID","User_ID","Amount","Txn_Date"]]

##query data
df2=df2.query("Amount > 150")
print(df2)

## select User_ID,count(*) from txnx where amount > 150
df2=df2.groupby("User_ID").size().reset_index(name="cnt")
print(df2)


##sort single and multiple columns
df.sort_values("State")
df.sort_values("State",ascending=False)
df.sort_values(["State","City"],ascending=[True,False])
## inplace

##add column 
df["country"]="India"
print(df)

##rename column'
df.rename(columns={"country":"Country"},inplace=True)

print(df.columns)

# drop first row:
df3=df.drop(0)
#drop multiple rows
df4=df.drop([1,3])
print(df4)

# after drop row the index will not update, to update use reset_index()
df4=df.drop([1,3]).reset_index()
print(df4)

# drop columns axis=1 means columns
df5=df.drop("Country",axis=1)
print(df5)
#drop multiple columns:
df5=df.drop(["Country","State"],axis=1)
print(df5)

## trsnformation on column
df["State"]=df["State"].str.upper()
df["Txn_ID"]=df["Txn_ID"].apply(lambda x : x+1)

## based on state apply discount

def cal_discount(state):
    disc=0
    if state == "TAMIL NADU":
        disc=1
    elif state == "DELHI":
        disc=2
    else:
        disc=4
    return disc

df["discount"]=df["State"].apply(cal_discount)
print(df)

#select city,state,sum(amount) as total_count,count(txnid) as txn_count from txns group by city,state
df3=(df.groupby(["City","State"]).agg(txn_count=("User_ID","count"),total_amt=("Amount","sum"),avg_amt=("Amount","mean"))
     .query("txn_count>1")
     .reset_index()
     .sort_values(by="txn_count",ascending=False))
print(df3)




