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
        x = getIdfromDescr(record.description)
        if x in geneIDs:
            if x in seqDic:
                if len(seqDic.get(x)) > len(record.seq):
                    continue
                else:
                    seqDic.update({x: str(record.seq)})
            else:
                seqDic.update({x: str(record.seq)})
        else:
            continue



for x in seqDic:
    print(x + "\n" + seqDic.get(x))

