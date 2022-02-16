import database

peptides = {}
tablenames = []

connection = database.create_connection_own()

def gettablenames():
    query = "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = 'interleukine'"
    result = database.execute_query(connection, query)
    for x in result:
        tablenames.append(str(x).replace("'","").replace(",","").replace("(","").replace(")",""))
    return tablenames


def writefile(tablenames):
    for name in tablenames:
        path ="/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/liststableid/" + name + ".fasta"
        getseqs(name)
        file = open(path, 'w')
        for x in peptides:
            file.write(">" + str(x) + "\n" + str(peptides.get(x)) + "\n")
        peptides.clear()

def getseqs(name):
    id = []
    seq = []
    query = "SELECT id, seq FROM " + name + ";"
    result = database.execute_query(connection,query)
    for x in result:
        a,b = x
        id.append(a)
        seq.append(b)
    i=0
    for x in id:
        peptides.update({x:seq[i]})
        i = i+1

writefile(gettablenames())