from Bio.Seq import Seq
from Bio import SeqIO
import pandas as pd

infos = pd.read_csv("/Users/rieke/Desktop/Mappe1 Kopie.csv", sep=";")
cds = {}

myseq = SeqIO.parse("/Users/rieke/Desktop/test.txt", "fasta")
file = open("/Users/rieke/Desktop/newseqs_extra.fasta",'w')
for seq_record in myseq:
    if((seq_record.id.replace("ctg.","")) in infos.values):
        inde =infos.index[infos["contig"]==seq_record.id.replace("ctg.","")].to_numpy()
        index = inde[0]
        cds.update({seq_record.id:seq_record.seq[(infos.at[int(index),"start"])-100:(infos.at[int(index),"stop"])+100]})

for entry in cds:
    file.write(">" + entry + "\n" + str(cds.get(entry)) + "\n")