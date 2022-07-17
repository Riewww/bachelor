import os

list = os.listdir("/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/Typhle")

for name in list:
    if name.endswith(".bam"):
        print("/" + name + ",")