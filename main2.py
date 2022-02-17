import database
import FastaScanner
# !!! need to change species name !!!
connection_own = database.create_connection_own()

#use script FastaScanner to load stable IDs of one species and find the corresponding peptide sequences in file
FastaScanner.loadgeneIDs("/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/liststableid/gasterosteus_aculeatus.txt")
FastaScanner.findID("/Users/rieke/Downloads/Gasterosteus_aculeatus.BROADS1.pep.all.fa")

query = ""

#Updates database with peptide sequence to corresponding id
for x in FastaScanner.seqDic:
    cursor = connection_own.cursor()
    query = "UPDATE gasterosteus_aculeatus SET seq = '" + FastaScanner.seqDic.get(x) + "' WHERE id = '"+ str(x) +"' ;"
    database.execute_query(connection_own, query)
    connection_own.commit()
