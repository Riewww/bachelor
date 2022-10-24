import gc
import pandas as pd
import os

# results forward BLAST search
interleukin = pd.read_csv("/Users/rieke/Desktop/cod_all_blast.csv", sep=";")
# results backward BLAST search
uniprot = pd.read_csv("/Users/rieke/Desktop/cod_uni_com.csv")

# lists to store ids and genes
liste = []
liste_genes = []
# list of files in this directory
id_list = os.listdir("/Users/rieke/Desktop/OG_ids/")

# for each Orthogroup it saves ids of genes scoring in forward BLAST and saves ids of genes in OG group
for name in id_list:
    file_id = open("/Users/rieke/Desktop/OG_ids/" + name, 'r')
    file = open("/Users/rieke/Desktop/cod_ids.txt", 'r')
    for line in file:
        liste.append(line.strip())
    for lines in file_id:
        liste_genes.append(lines.strip())

# initation of new data frame
    d3 = pd.DataFrame(columns= ['id','uni', 'int'])
    a = {}

# goes through all genes saved in liste
    for id in liste:
        #goes trough all results of forward BLAST search
        for index, row in interleukin.iterrows():
            # if active gene id is in forward BLAST results next step is executed
            if(row[1] == id):
                # goes through all genes of activated OG
                for genes in liste_genes:
                    # if activated OG gene id is in forward BLAST results next step is executed
                    if(row[2]==genes):
                        # goes through reverse BLAST results
                        for index2, row2 in uniprot.iterrows():
                            # if active gene id is in reverse BLAST results next step is executed
                            if(row2[1] == id):
                                # a = temporary dictionary, if active gene id is already in next steps are executend,
                                # if not jump to else
                                if ( row[1]  in a ):
                                    # gets already save bitscores forward and reverse BLAST
                                    temp_int =  a.get(row[1])[0]
                                    temp_uni = a.get(row[1])[1]
                                    # compares already saved score with new ones and replaces old one if greater
                                    if (abs(row['bitscore']) > a.get(row[1])[0]):
                                        temp_int = row['bitscore']
                                    if (abs(row2['bitscore']) > a.get(row[1])[1]):
                                        temp_uni = row2['bitscore']
                                    else:
                                        continue
                                    # empty entry in a for acitve id and saves new bitscores
                                    a[row[1]].clear()
                                    a[row[1]].extend([temp_int,temp_uni])

                                else:
                                    # creates entry of active id in a and saves corresponding bitscores
                                    a[row[1]] = list()
                                    a[row[1]].extend([row['bitscore'],row2['bitscore']])
                            else:
                                continue
                        else:
                             continue

    # saves all entries in a (for one OG) in new dataframes and saves it as csv file
    if(len(a) !=0):
        for i in a:
            for b in range(1, len(a.get(i))):
                temp = pd.DataFrame({'id':[i],'uni':[a.get(i)[0]],'int':[a.get(i)[b]]})
                d3 = pd.concat([d3,temp], ignore_index=True, axis=0)
                del temp
                gc.collect()
                d3.to_csv("/Users/rieke/Desktop/cod/" + name.replace(".txt", "") + ".csv")
    del d3
    gc.collect()
    a.clear()
    liste.clear()
    liste_genes.clear()
