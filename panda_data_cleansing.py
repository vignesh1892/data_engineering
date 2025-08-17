import pandas as pd
df=pd.read_csv("custs.csv")

print(df["profession"].unique)

#count of each value
print(df["profession"].value_counts())

#max value
df["age"].max()

##remove null values
df.dropna()

#replace null values
df.fillna(0)
fvalue={"age":"0","Profession":"NA"}

df.fillna(value=fvalue)