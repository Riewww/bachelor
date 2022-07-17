
from Bio import SeqIO
import pandas as pd
stirng = []

infos = pd.read_csv("/Users/rieke/Desktop/Mappe1 Kopie.csv", sep=";")
myseq = SeqIO.parse("/Users/rieke/Desktop/test.txt", "fasta")
for seq_record in myseq:
    if("000018F" == seq_record.id.replace("ctg.","")):
        stirng.append(str(seq_record.seq[3311206:3332068]).strip())
        print(seq_record.id)
        print(stirng)
