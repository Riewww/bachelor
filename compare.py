contigs = []
x = 0
file = open("/Users/rieke/Desktop/augustus_2/razor/razor_id.txt", 'r')
file3 = open("/Users/rieke/Desktop/augustus_2/razor/razor_uni_com.txt", 'w')

for line in file:
    file2 = open("/Users/rieke/Desktop/augustus_2/razor/razor_uni.txt", 'r')
    for line2 in file2:
        if((line2.split())[0].strip() == line.strip()):
            file3.write(line2)
            continue

