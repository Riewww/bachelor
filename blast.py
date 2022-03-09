contigs = []

#file = open("/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/BLAST/forward(dataset)/sequenceserver-std_tsv_report_Nerophis_after_augustus.tsv", 'r')
file = open("/Users/rieke/Desktop/testen.txt", 'r')

#for line in file:
    #for x in line.split():
     #   if(x.startswith("ctg.")):
           # contigs.append(x)

for line in file:
    contigs.append((line.split())[0])
unique_contigs = list(dict.fromkeys(contigs))


file = open("/Users/rieke/Desktop/Nerophis_ids.txt", 'w')

for x in unique_contigs:
    file.write(x + "\n")