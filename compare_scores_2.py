import gc

import pandas as pd
import os
zahl = 0
interleukin = pd.read_csv("/Users/rieke/Desktop/testen_clean.csv")
uniprot = pd.read_csv("/Users/rieke/Desktop/Nerophis_uni2.csv")
liste = []
liste_genes = []
id_list = os.listdir("/Users/rieke/Desktop/OG_ids/")

for name in id_list:
    file_id = open("/Users/rieke/Desktop/OG_ids/" + name, 'r')
    file = open("/Users/rieke/Desktop/Nerophis_ids.txt", 'r')
    for line in file:
        liste.append(line.strip())
    for lines in file_id:
        liste_genes.append(lines.strip())


    d3 = pd.DataFrame(columns= ['id','uni', 'int'])
    a = {}


    for id in liste:
        for index, row in interleukin.iterrows():
            if(row[1] == id):
                for genes in liste_genes:
                    if(row[2]==genes):
                        for index2, row2 in uniprot.iterrows():
                            if(row2[1] == id):
                                if ( row[2]  in a ):
                                    temp_int =  a.get(row[2])[0]
                                    temp_uni = a.get(row[2])[0]
                                    if (abs(row['bitscore']) > a.get(row[2])[0]):
                                        temp_int = row['bitscore']
                                    if (abs(row2['bitscore']) > a.get(row[2])[1]):
                                        temp_uni = row2['bitscore']
                                    else:
                                        continue
                                    a[row[2]].clear()
                                    a[row[2]].extend([temp_int,temp_uni])

                                else:
                                    a[row[2]] = list()
                                    a[row[2]].extend([row['bitscore'],row2['bitscore']])
                            else:
                                continue
                        else:
                            continue


    for i in a:
        for b in range(1, len(a.get(i))):
            temp = pd.DataFrame({'id':[i],'uni':[a.get(i)[0]],'int':[a.get(i)[b]]})
            d3 = pd.concat([d3,temp], ignore_index=True, axis=0)
            del temp
            gc.collect()

    d3.to_csv("/Users/rieke/Desktop/bits/" + name.replace(".txt","") + ".csv")
    del d3
    gc.collect()
    a.clear()
    liste.clear()
    liste_genes.clear()
