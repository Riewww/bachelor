import database
import FastaScanner
descrip = {}

FastaScanner.loadgeneIDs("/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/liststableid/oryzias_latipes.txt")
connection = database.create_connection_ensembl()
query_ensembl = ""
for x in FastaScanner.geneIDs:
    results = []
    query_ensembl = "SELECT description FROM gene WHERE stable_id = '" + x + "';"
    result = database.execute_query(connection,query_ensembl)
    results = str(result).replace("(","").replace(")","")[2:len(result)-4]
    descrip.update({x : results})



connection_own = database.create_connection_own()

query = ""
for x in descrip:
    cursor = connection_own.cursor()
    query = "UPDATE oryzias_latipes SET descr = '" + str(descrip.get(x)) + "' WHERE id = '"+ str(x) +"' ;"
    database.execute_query(connection_own, query)
    connection_own.commit()