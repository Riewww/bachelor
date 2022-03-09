contigs = []
x = 0
file = open("/Users/rieke/Desktop/Nerophis_ids.txt", 'r')
file3 = open("/Users/rieke/Desktop/Nerophis_double.txt", 'w')

for line in file:
    file2 = open("/Users/rieke/Desktop/Nerophis_Uniprot.txt", 'r')
    for line2 in file2:
        if((line2.split())[0].strip() == line.strip()):
            file3.write(line2)
            continue

