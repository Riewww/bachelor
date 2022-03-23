import gc

import pandas as pd
import os

ognames = os.listdir("/Users/rieke/Desktop/nerophis/bits")

for name in ognames:
    pd0 = pd.read_csv("/Users/rieke/Desktop/nerophis/bits/" + name)
    pd0['species']='nerophis'
    pd1 = pd.read_csv("/Users/rieke/Desktop/aeolis/bits2/aeolis_" + name)
    pd1['species'] = 'aeolis'
    pd2 = pd.read_csv("/Users/rieke/Desktop/typhle/bits2/typhle_" + name)
    pd2['species'] = 'typhle'



    temp1 = pd0.append(pd1)

    final = temp1.append(pd2)

    final.drop_duplicates(inplace=True)

    final.to_csv("/Users/rieke/Desktop/all_species/bits2/" +name)

    del pd0
    del pd1
    del pd2
    del temp1
    del final
    gc.collect()


