import pandas as pd

test = pd.read_csv("/Users/rieke/Desktop/typhle_dedup.txt", delim_whitespace=",", names=["queryid", "subjectid", "subject sci names","% identity", "alignment length", "mismatches"," gap opens", "q.start", "q.end", "s.start", "s.end", "evalue", "bitscore", "% query coverage per subject", "% query coverage per hsp"])

test = test.drop(columns=test.columns[[2,3,4,5,6,7,8,9,10,11,13,14]])

path = "/Users/rieke/Desktop/typhle_dedup.csv"

test.to_csv(path)