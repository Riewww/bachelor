import pandas as pd
import os

directory = os.listdir("/Users/rieke/Desktop/hippo/OG")

new_file_path = "/Users/rieke/Desktop/hippo/all_best_hits.csv"
new_file_pd = pd.DataFrame(columns=['id','uni','int','OG'])


for files in directory:
    temp = pd.read_csv("/Users/rieke/Desktop/hippo/OG/" + files, index_col=[0])
    temp['OG'] = files.replace("_ids.csv", "")
    temp2 = pd.DataFrame(columns=['id','uni','int','OG'])
    new_file_pd = new_file_pd.append(temp, ignore_index=True)
    del temp
    del temp2
new_file_pd.to_csv(new_file_path, sep=",")