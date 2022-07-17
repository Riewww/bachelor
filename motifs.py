from Bio import SeqIO
file = open("/Users/rieke/Desktop/Aeolis_real_2.txt", 'r')
file2 = open("/Users/rieke/Desktop/Aeolis_real_3.txt", 'w')


for lines in file:
    file2.write(lines.strip())
