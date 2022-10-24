
# array to save lines of matches
matches=[]
# saves gene ids
key = ""

# opens file with results of forward BLAST search
file = open("/Users/rieke/Downloads/sequenceserver-std_tsv_report (18).tsv", 'r')
# new file were gene ids of hits are stored
file_new = open("/Users/rieke/Desktop/cod_inter.txt", 'w')
#iterates over all lines of result file
for line in file:
    # if line starts with '#' (no hit)
    if (line.startswith('#')):
        if (len(matches) != 0):
            for x in matches:
                file_new.write(x)
            matches.clear()
        continue
    else:
        if (key == line.split()[0]):
            matches.append(line)

        else:
            key = line.split()[0]
            matches.append(line)





#file_new = open("/Users/rieke/Desktop/test.txt", 'w')





