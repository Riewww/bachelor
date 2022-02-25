import database
import os
import peptidfasta

#loads all file names of directory into one list
listreal = os.listdir("/Users/rieke/Desktop/real/")
listall = os.listdir("/Users/rieke/Desktop/ortho/OrthoFinder/Results_Feb16/Orthogroup_Sequences/")

#ids that are not interleukins and need to be dropped
drop = []

connection = database.create_connection_own()


# checks if OrthoGroup name is in directory with "real ones"
# if not in there, saves all stable ids in drop
# drops all entrys with stable id in drop from all existing tables
def removefiles():
    for names in listall:
        if (names.replace('.fa','.txt')) in listreal:
            continue
        else:
            file = open("/Users/rieke/Desktop/ortho/OrthoFinder/Results_Feb16/Orthogroup_Sequences/" + names.replace('.txt',".fa"), 'r' )
            for lines in file:
                if lines.startswith('>'):
                    drop.append((lines).replace(">","").strip())
    for table in peptidfasta.gettablenames():
        for ids in drop:
            database.execute_query(connection, "DELETE FROM " +table+" WHERE id = '" + str(ids) + "';")
            connection.commit()


removefiles()