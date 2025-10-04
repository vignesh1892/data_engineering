import pandas as pd
df1 = pd.read_csv("sample_data\AlphaCorp.csv",parse_dates=["date"])
df1["year"]=df1["date"].dt.year
df2_high_volume=df1.groupby(["year"])["volume"].max()
df3_high_volume=df1.merge(df2_high_volume,on="volume",how="inner")[["date","close"]]
print(df3_high_volume)
df2_high_close=df1.groupby(["year"])["close"].max()
df3_high_close=df1.merge(df2_high_close,on="close",how="inner")[["date","close"]]
print(df3_high_close)

belt_df1 = pd.read_csv("sample_data\BetaLtd.csv",parse_dates=["date"])
belt_df1["year"]=belt_df1["date"].dt.year
belt_df2_high_volume=belt_df1.groupby(["year"])["volume"].max()
belt_df3_high_volume=belt_df1.merge(belt_df2_high_volume,on="volume",how="inner")[["date","close"]]
print(belt_df3_high_volume)
belt_df2_high_close=belt_df1.groupby(["year"])["close"].max()
belt_df3_high_close=belt_df1.merge(belt_df2_high_close,on="close",how="inner")[["date","close"]]
print(belt_df3_high_close)

combined_df = pd.concat([df3_high_volume, df3_high_close, belt_df3_high_volume,belt_df3_high_close], axis=1)
print(combined_df)





