import database
import FastaScanner
import os
# !!! need to change species name !!!
connection_own = database.create_connection_own()

#use script FastaScanner to load stable IDs of one species and find the corresponding peptide sequences in file
FastaScanner.loadgeneIDs("/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/liststableid/all_orthos.txt")

listreal = os.listdir("/Users/rieke/Desktop/real/")

for name in listreal:
    FastaScanner.findID("/Users/rieke/Downloads/" + name.replace('.txt',".fa"))

query = ""

for x in FastaScanner.seqDic:
    query_own = "INSERT IGNORE INTO all_species (id, seq) VALUES (\"" + str(x) + "\", \" " + str(FastaScanner.seqDic.get(x))+ "\");"
    cursor = connection_own.cursor()
    cursor.execute(query_own)
    connection_own.commit()
    cursor.fetchall()


#Updates database with peptide sequence to corresponding id
#for x in FastaScanner.seqDic:
  #  cursor = connection_own.cursor()
   # query = "UPDATE all_species SET seq = '" + FastaScanner.seqDic.get(x) + "' WHERE id = '"+ str(x) +"' ;"
  #  database.execute_query(connection_own, query)
  #  connection_own.commit()
