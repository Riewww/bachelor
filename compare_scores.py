import pandas as pd

interleukin = pd.read_csv("/Users/rieke/Desktop/Nerophis_int2.csv")
uniprot = pd.read_csv("/Users/rieke/Desktop/Nerophis_uni2.csv")
liste = []
file = open("/Users/rieke/Desktop/Nerophis_ids.txt", 'r')
for line in file:
    liste.append(line.strip())
#def delete_rows(dataframe, id):
   # for index, row in dataframe.iterrows():
   #     if(row['queryid'] == id):
       #     continue
      #  else:
        #    dataframe.drop(index, inplace=True)
    #return dataframe


#d1 = delete_rows(interleukin)
#d2 = delete_rows(uniprot)
#interleukin.sort_values('bitscore')
d3 = pd.DataFrame(columns= ['id','uni', 'int'])
a = {}


for id in liste:
    for index, row in interleukin.iterrows():
        if(row[1] == id):
            for index2, row2 in uniprot.iterrows():
                if(row2[1] == id):
                    if ( row[1]  in a ):
                        temp_int =  a.get(row[1])[0]
                        temp_uni = a.get(row2[1])[0]
                        if (abs(row['bitscore']) > a.get(row[1])[0]):
                            temp_int = row['bitscore']
                        if (abs(row2['bitscore']) > a.get(row[1])[1]):
                            temp_uni = row2['bitscore']
                        else:
                            continue
                        a[row[1]].clear()
                        a[row[1]].extend([temp_int,temp_uni])

                    else:
                        a[row[1]] = list()
                        a[row[1]].extend([row['bitscore'],row2['bitscore']])
                else:
                    continue
            else:
                continue


for i in a:
    for b in range(1, len(a.get(i))):
        temp = pd.DataFrame({'id':[i],'uni':[a.get(i)[0]],'int':[a.get(i)[b]]})
        d3 = pd.concat([d3,temp], ignore_index=True, axis=0)
        temp.drop(index=0, axis=0,inplace=True)

d3.to_csv("/Users/rieke/Desktop/bits.csv")