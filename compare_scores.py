import gc

import pandas as pd
import os

file1 = pd.read_csv("/Users/rieke/Desktop/augustus_2/typ_tseb_clean.csv")

file1.sort_values(by='queryid',ascending=True,inplace=True)
a = {}
for index,row in file1.iterrows():
    if(row[1] not in a):
        a.update({row[1]:row[3]})
    elif(row[1] in a):
        if(row[3] > a.get(row[1])):
            a.update({row[1]:row[3]})
        else:
            continue


file2 = pd.read_csv("/Users/rieke/Desktop/augustus_2/typhle/files/typhle_int_clean_2.csv")

file2.sort_values(by='queryid',ascending=True,inplace=True)
b = {}
for index,row in file2.iterrows():
    if(row[1] not in b):
        b.update({row[1]:row[3]})
    elif(row[1] in b):
        if(row[3] > b.get(row[1])):
            b.update({row[1]:row[3]})
        else:
            continue

for x in a:
    print(x, a.get(x))
print("\n")
for y in b:
    print(y, b.get(y))