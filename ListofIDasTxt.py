import database
import peptidfasta

#list to store stable Id temporary
geneID = []
tablenames = []


connection = database.create_connection_own()

def gettablenames():
    query = "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = 'interleukine'"
    result = database.execute_query(connection, query)
    for x in result:
        tablenames.append(str(x).replace("'","").replace(",","").replace("(","").replace(")",""))
    return tablenames

#method to create a new file to write geneIds into
def write_file(tablenames):
    for name in tablenames:
        path = "/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/OG/" + name +".txt"
        getid(name)
        f = open(path, 'w')
        i = 0
        for x in geneID:
            f.write(x + '\n')
            i = i + 1
        geneID.clear()


#method to query all gene ids from one table(name)
def getid(name):
    query = "SELECT id FROM " + name
    database.save_queryresult(database.execute_query(connection,query))
    for x in database.res:
        a = x
        geneID.append(''.join(filter(str.isalnum, str(a))))
    database.res.clear()


write_file(gettablenames())