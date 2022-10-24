import pandas as pd

# read csv file as panda dataframe
test = pd.read_csv("/Users/rieke/Desktop/cod_inter_com.txt", delim_whitespace=",", names=["queryid", "subjectid", "subject sci names","% identity", "alignment length", "mismatches"," gap opens", "q.start", "q.end", "s.start", "s.end", "evalue", "bitscore", "% query coverage per subject", "% query coverage per hsp"])
# drops unneccessary columns
test = test.drop(columns=test.columns[[2,3,4,5,6,7,8,9,10,11,13,14]])
# path of new csv file
path = "/Users/rieke/Desktop/cod_inter_com.csv"
# saves cleaned panda dataframe as csv
test.to_csv(path)