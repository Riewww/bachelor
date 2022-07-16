from Bio.Seq import Seq
from Bio import SeqIO
import pandas as pd
infos = []
info_file = open("/Users/rieke/Desktop/il_double_check_typhle.txt", 'r')
for x in info_file:
    infos.append(x.strip())
cds = {}

myseq = SeqIO.parse("/Users/rieke/Desktop/typhle_check_genes.augustus.aa.1", "fasta")
file = open("/Users/rieke/Desktop/genes_check.fasta_il",'w')
for seq_record in myseq:
    if((seq_record.id) in infos):
        cds.update({seq_record.id:seq_record.seq})

for entry in cds:
    file.write(">" + entry + "\n" + str(cds.get(entry)) + "\n")