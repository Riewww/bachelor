import database
import peptidfasta

geneID = []
connection = database.create_connection_own()

def write_file():
    for name in peptidfasta.tablenames:
        path = "/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/liststableid/" + name +".txt"
        getid(name)
        f = open(path, 'w')
        i = 0
        for x in geneID:
            f.write(geneID[i] + '\n')
            i = i + 1
        geneID.clear()

def getid(name):
    query = "SELECT id FROM " + name
    database.save_queryresult(database.execute_query(connection,query))
    for x in database.res:
        a = x
        geneID.append(''.join(filter(str.isalnum, str(a))))


write_file()