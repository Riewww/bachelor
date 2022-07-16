import gc
import pandas as pd
import os
interleukin = pd.read_csv("/Users/rieke/Desktop/typhle_dedup.csv")
a = {}
d3 = pd.DataFrame(columns=['id', 'bit', 'sub'])

for index, row in interleukin.iterrows():
    if (row[1] in a):
        temp_int = a.get(row[1])[1]
        if (abs(row['bitscore']) > a.get(row[1])[0]):
            temp_int = row['bitscore']
        else:
            continue
        a[row[1]].clear()
        a[row['queryid']].extend([row['bitscore'], row['subjectid']])
    else:
        a[row[1]] = list()
        a[row['queryid']].extend([row['bitscore'],row['subjectid']])

    if(len(a) !=0):
        for i in a:
            for b in range(1, len(a.get(i))):
                temp = pd.DataFrame({'id':[i],'bit':[a.get(i)[0]], 'sub':[a.get(i)[1]]})
                d3 = pd.concat([d3,temp], ignore_index=True, axis=0)
                del temp
                gc.collect()
                d3.to_csv("/Users/rieke/Desktop/typhle_check_dedup.csv")