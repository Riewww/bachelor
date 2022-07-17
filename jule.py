import os
ids= []

files = os.listdir("/INTENSO/")

fileid = open("/Users/arsenydubin/Desktop/test.txt", 'r')

for id in fileid:
    ids.append(id.strip())


for file in files:
    if(file in ids):
        if(file.endswith(".fastq.gz")):
            os.replace(file, "/Users/arsenydubin/Desktop/Jule/a")