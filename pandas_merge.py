import gc

import pandas as pd
import os

ognames = os.listdir("/Users/rieke/Desktop/typhle/0/bits2")

for name in ognames:
    pd0 = pd.read_csv("/Users/rieke/Desktop/typhle/0/bits2/" + name).drop(columns=['Unnamed: 0'])
    pd1 = pd.read_csv("/Users/rieke/Desktop/typhle/1/bits2/" + name).drop(columns=['Unnamed: 0'])
    pd2 = pd.read_csv("/Users/rieke/Desktop/typhle/2/bits2/" + name).drop(columns=['Unnamed: 0'])
    pd3 = pd.read_csv("/Users/rieke/Desktop/typhle/3/bits2/" + name).drop(columns=['Unnamed: 0'])


    temp1 = pd0.append(pd1)

    temp2 = pd2.append(pd3)

    final = temp1.append(temp2)

    final.drop_duplicates(inplace=True)

    final.to_csv("/Users/rieke/Desktop/typhle/bits2/typhle_" + name)

    del pd0
    del pd1
    del pd2
    del pd3
    del temp2
    del temp1
    del final
    gc.collect()


