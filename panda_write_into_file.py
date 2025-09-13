import pandas as pd

df= pd.read_csv("transactions.csv",names =["Txn_ID","User_ID","Product_ID","Amount","Txn_Date","State","City"])

print(df)

df.sort_values(["Amount","State"],ascending=[True,True],inplace=True)

##save without index
df.to_csv("panda_txnx_op.csv",index=False)
df.to_excel("panda_txnx_op.xlsx",index=False)
df.to_json("panda_txnx_op.json",index=False)
df.to_html("panda_txnx_op.html",index=False)
df.to_string("panda_txnx_op.txt",index=False)

## sql