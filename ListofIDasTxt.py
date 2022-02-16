import database

path = "/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/liststableid/gasterosteus_aculeatus.txt"
geneID = []



def write_file(path, header):
    f = open(path, 'w')
    i = 0
    for x in header:
        f.write(header[i] + '\n')
        i = i + 1


connection = database.create_connection_own()
database.save_queryresult(database.execute_query(connection, "SELECT id FROM gasterosteus_aculeatus"))

for x in database.res:
    a = x
    geneID.append(''.join(filter(str.isalnum, str(a))))


write_file(path, geneID)