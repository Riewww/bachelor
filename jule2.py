import os

files = os.listdir("")
r1 =[]
r2 = []

for file in files:
    if(file.endswith("R2_001.fastq.gz")):
        r2.append(file.strip())
    if (file.endswith("R1_001.fastq.gz")):
        r1.append(file.strip())

filer1 = open("", 'w')

filer2 = open("", 'w')

for a in r1:
    filer1.write(a)

for b in r2:
    filer2.write(b)
