# file with gene ids that scored in forward BLAST search
file = open("/Users/rieke/Desktop/cod_ids.txt", 'r')
# new file with only ids that scored in forward BLAST search
file3 = open("/Users/rieke/Desktop/cod_inter_com.txt", 'w')

# iterates trough all ids in file
for line in file:
    # file with reverse BLAST results
    file2 = open("/Users/rieke/Desktop/cod_inter.txt", 'r')
    for line2 in file2:
        # if active gene id exists in both files, results are saved into file3
        if((line2.split())[0].strip() == line.strip()):
            file3.write(line2)
            continue

