import database
import FastaScanner

#dictionary to save id and description
descrip = {}

#loads stable IDs
FastaScanner.loadgeneIDs("/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/liststableid/oryzias_latipes.txt")
#connects to ensembl database
connection = database.create_connection_ensembl()
query_ensembl = ""

#dowloads corresponding description and cleans the string
for x in FastaScanner.geneIDs:
    results = []
    query_ensembl = "SELECT description FROM gene WHERE stable_id = '" + x + "';"
    result = database.execute_query(connection,query_ensembl)
    results = str(result).replace("(","").replace(")","")[2:len(result)-4]
    descrip.update({x : results})


#connects to own database
connection_own = database.create_connection_own()
query = ""

#loads desription into database where id is
for x in descrip:
    cursor = connection_own.cursor()
    query = "UPDATE oryzias_latipes SET descr = '" + str(descrip.get(x)) + "' WHERE id = '"+ str(x) +"' ;"
    database.execute_query(connection_own, query)
    connection_own.commit()