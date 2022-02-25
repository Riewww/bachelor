import database

# dictionary to store peptide sequences and id temporary
peptides = {}
# list of names from all existing tables
tablenames = []

connection = database.create_connection_own()


# method to get all table names
def gettablenames():
    query = "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = 'interleukine'"
    result = database.execute_query(connection, query)
    for x in result:
        tablenames.append(str(x).replace("'","").replace(",","").replace("(","").replace(")",""))
    return tablenames
import database

# dictionary to store peptide sequences and id temporary
peptides = {}
# list of names from all existing tables
tablenames = []

connection = database.create_connection_own()


# method to get all table names
def gettablenames():
    query = "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = 'interleukine'"
    result = database.execute_query(connection, query)
    for x in result:
        tablenames.append(str(x).replace("'","").replace(",","").replace("(","").replace(")",""))
    return tablenames


# method to all peptides and id (header) into fasta file
def writefile(tablenames):
    for name in tablenames:
        path ="/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/liststableid/" + name + ".fasta"
        getseqs(name)
        file = open(path, 'w')
        for x in peptides:
            file.write(">" + str(x) + "\n" + str(peptides.get(x)) + "\n")
        peptides.clear()


# getting all ids and corresponding sequences from one table and load them into peptides
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

# method to all peptides and id (header) into fasta file
def writefile(tablenames):
    for name in tablenames:
        path ="/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/liststableid/" + name + ".fasta"
        getseqs(name)
        file = open(path, 'w')
        for x in peptides:
            file.write(">" + str(x) + "\n" + str(peptides.get(x)) + "\n")
        peptides.clear()


# getting all ids and corresponding sequences from one table and load them into peptides
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