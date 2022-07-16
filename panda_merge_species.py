import gc

import pandas
import pandas as pd
import os



ognames = os.listdir("/Users/rieke/Desktop/OG_ids/")

for name in ognames:
    pd0 = pd.DataFrame()
    pd1 = pd.DataFrame()
    pd2 = pd.DataFrame()
    if(os.path.exists("/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/compare_score/nerophis/OG_best_hits/" + name.replace('txt','csv'))):
        pd0 = pd.read_csv("/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/compare_score/nerophis/OG_best_hits/" + name.replace('txt','csv'))
        pd0['species']='nerophis'
    if(os.path.exists("/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/compare_score/razorfish/OG_best_hits/" + name.replace('txt','csv'))):
        pd1 = pd.read_csv("/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/compare_score/razorfish/OG_best_hits/" + name.replace('txt','csv'))
        pd1['species'] = 'razorfish'
    if(os.path.exists("/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/compare_score/typhle/OG_best_hits/typhle_" + name.replace('txt','csv'))):
        pd2 = pd.read_csv("/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/compare_score/typhle/OG_best_hits/typhle_" + name.replace('txt','csv'))
        pd2['species'] = 'typhle'

    if(pd0.notnull and pd1.notnull and pd2.notnull):
        temp1 = pd0.append(pd1)
        final = temp1.append(pd2)
    elif(pd0.notnull and pd1.notnull and pd2.isnull):
        final = pd0.append(pd1)
    elif(pd0.notnull and pd1.isnull and pd2.notnull):
        final = pd0.append(pd2)
    elif(pd0.isnull and pd1.notnull and pd2.notnull):
        final = pd1.append(pd2)
    elif (pd0.isnull and pd1.isnull and pd2.notnull):
        final = pd2
    elif(pd0.isnull and pd1.notnull and pd2.isnull):
        final = pd1
    elif(pd0.notnull and pd1.isnull and pd2.isnull):
        final = pd0

    final.drop_duplicates(inplace=True)
    final.to_csv("/Users/rieke/Desktop/OG_best_hits_all_spec/" +name.replace('txt','csv'))

    del pd0
    del pd1
    del pd2
    del temp1
    del final
    gc.collect()


