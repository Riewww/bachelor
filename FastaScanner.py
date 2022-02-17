from Bio import SeqIO

# list of stable IDs and dictionary for stable Ids : peptide sequence
seqDic = {}
geneIDs = []


# opens file with stable Ids and loads them into geneIDs
def loadgeneIDs(path):
    file = open(path, 'r')
    for x in file:
        geneIDs.append(x.strip())


# filters in all.peptides.fasta the header for the gene ID
def getIdfromDescr(description):
    start = description.index("gene:")
    end = description.index("transcript:")
    return str(description[start+5:end-3])

# searches for gene ID in all peptides file
# if its found, check if the gene already has a sequence
# if not insert gene id + sequence into seqDic
# if already exists -> only updates sequence if longer than existing one
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



