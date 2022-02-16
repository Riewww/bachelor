import database
import FastaScanner

connection_own = database.create_connection_own()

FastaScanner.loadgeneIDs("/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/liststableid/gasterosteus_aculeatus.txt")
FastaScanner.findID("/Users/rieke/Downloads/Gasterosteus_aculeatus.BROADS1.pep.all.fa")

query = ""

for x in FastaScanner.seqDic:
    cursor = connection_own.cursor()
    query = "UPDATE gasterosteus_aculeatus SET seq = '" + FastaScanner.seqDic.get(x) + "' WHERE id = '"+ str(x) +"' ;"
    database.execute_query(connection_own, query)
    connection_own.commit()
