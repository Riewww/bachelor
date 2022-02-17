import database
import os

#temporary lists for query result and stable ids
listID = []
result = []
#loads all file names of directory into one list
pathlist = os.listdir("/Users/rieke/Desktop/ortho/OrthoFinder/Results_Feb16/Orthogroup_Sequences/")

connection = database.create_connection_own()


# method to get a new txt file with description of stable id for each OrthoGroup file
def getdescriptionofOG():
    for OGname in pathlist:
        file = open("/Users/rieke/Desktop/ortho/OrthoFinder/Results_Feb16/Orthogroup_Sequences/" + OGname, 'r')
        for line in file:
            if line.startswith('>'):
                listID.append((line.replace(">", "")).strip())
            else:
                continue

        for id in listID:
            query = "SELECT descr FROM description WHERE id ='" + id + "';"
            result.append(str(database.execute_query(connection,query)))

        filenew = open("/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/liststableid/OG" + (OGname.replace(".fa", "")) + ".txt", 'w')
        for desc in result:
            filenew.write(desc.replace("(","").replace(")","")+ "\n")
        listID.clear()
        result.clear()

getdescriptionofOG()



