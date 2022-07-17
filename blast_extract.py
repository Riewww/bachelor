matches=[]
info = ""
hits ={}
key = ""

file = open("/Users/rieke/Downloads/sequenceserver-std_tsv_report (5).tsv", 'r')
file_new = open("/Users/rieke/Desktop/typhle_dedup.txt", 'w')
for line in file:
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





