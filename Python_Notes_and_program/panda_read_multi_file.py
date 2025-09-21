import pandas as pd
import glob
import zipfile
import rarfile

files_list_rel = glob.glob(
    "F:/Studies/Big_Data/Inceptez/Azure_AI_Class/python_notes_learnings/trainings/github/data_engineering/Python_Notes_and_program/sample_data/*.csv"
)
print("files_list (relative):", files_list_rel)


print("files_list=",files_list_rel)
all_df=[]
for csvfile in files_list_rel:
    df=pd.read_csv(csvfile)
    all_df.append(df)

print(all_df)

final_df= pd.concat(all_df,ignore_index=True)

print(final_df)

##zip file
zip_path = "F:/Studies/Big_Data/Inceptez/Azure_AI_Class/python_notes_learnings/trainings/github/data_engineering/Python_Notes_and_program/sample_data_zip.rar"

all_df = []

with rarfile.RarFile(zip_path, "r") as z:
    for filename in z.namelist():
        if filename.endswith(".csv"):
            with z.open(filename) as f:
                df = pd.read_csv(f)
                all_df.append(df)

