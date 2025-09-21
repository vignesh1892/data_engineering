import pandas as pd
import glob
import zipfile

files_list_rel = glob.glob("F:/Studies/Big_Data/Inceptez/Azure_AI_Class/python_notes_learnings/trainings/github/data_engineering/Python_Notes_and_program/*.csv")
print("files_list (relative):", files_list_rel)

print("files_list=",files_list_rel)
all_df=[]
for csvfile in files_list_rel:
    df=pd.read_csv(csvfile)
    all_df.append(df)

print(all_df)

##zip file
with zipfile.ZipFile("Python_Notes_and_program/sample_data.zip","r") as z:
    for filename in z.namelist:
        print("filename",filename)

