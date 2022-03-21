import os
pathlist = os.listdir("/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/ortho_seqs_sorted/real2/")
geneids = []
for name in pathlist:
    file = open("/Users/rieke/Desktop/ortho/OrthoFinder/Results_Feb25_6/Orthogroups/Orthogroups.txt")
    for line in file:
        if(line.split()[0].replace(":","") == name.replace(".txt", "")):
            for id in line.split():
                if(id.replace(":","") == name.replace(".txt", "")):
                    continue
                else:
                    geneids.append(id.strip() + "\n")
        else:
            continue
    file2 = open("/Users/rieke/Desktop/" + name.replace(".txt","") + "_ids.txt", 'w')
    for ids in geneids:
        file2.write(ids)
    geneids.clear()

