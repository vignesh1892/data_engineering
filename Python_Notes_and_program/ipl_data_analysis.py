import pandas as pd
import glob
files_list_rel = glob.glob(
    "F:/Studies/Big_Data/Inceptez/Azure_AI_Class/python_notes_learnings/trainings/github/data_engineering/Python_Notes_and_program/sample_data/ipl/*.csv"
)

print("files_list_rel:",files_list_rel)

all_df = pd.concat((pd.read_csv(f) for f in files_list_rel), ignore_index=True)
print(all_df)
all_df.fillna(0)
all_df1=all_df.query('team1 == "KKR" or team2 == "KKR"')

all_df1["Total"]=all_df1["first_ings_score"]+all_df1["second_ings_score"]

#1. Highest individual score (highscore) by each batsman
all_df2=all_df1.groupby("venue")["first_ings_score"].agg(["max", "min", "mean"]).reset_index()
print(all_df2)



