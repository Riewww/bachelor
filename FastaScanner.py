from Bio import SeqIO


seqDic = {}
geneIDs = []


def loadgeneIDs(path):
    file = open(path, 'r')
    for x in file:
        geneIDs.append(x.strip())

def getIdfromDescr(description):
    start = description.index("gene:")
    end = description.index("transcript:")
    return str(description[start+5:end-3])


def findID(path):
    for record in SeqIO.parse(path, "fasta"):
        if getIdfromDescr(record.description) in geneIDs:
            seqDic.update({getIdfromDescr(record.description) : str(record.seq)})
        else:
            continue

loadgeneIDs("/Users/rieke/OneDrive - stud.hs-emden-leer.de/takifugu.txt")
findID("/Users/rieke/OneDrive - stud.hs-emden-leer.de/ivana/data")

for x in seqDic:
    print(x + "\n" + seqDic.get(x))

