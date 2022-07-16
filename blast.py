contigs = []

#file = open("/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/BLAST/forward(dataset)/sequenceserver-std_tsv_report_Nerophis_after_augustus.tsv", 'r')
file = open("/Users/rieke/Downloads/sequenceserver-std_tsv_report (5).tsv", 'r')

#for line in file:
   # for x in line.split():
        #if(x.startswith("ctg.")):
          # contigs.append(x)

for line in file:
    if(line.startswith("#")):
        continue
    else:
        for x in line.split(sep="	"):
            if (x.startswith("g")):
                contigs.append(x)
                break

unique_contigs = list(dict.fromkeys(contigs))


file2 = open("/Users/rieke/Desktop/tyhple_dedup_id.txt", 'w')

for x in unique_contigs:
  file2.write(x + "\n")