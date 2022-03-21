import pandas as pd

test = pd.read_csv("/Users/rieke/Desktop/testen.txt", delim_whitespace=",")

test = test.drop(columns=test.columns[[2,3,4,5,6,9,10,11,13,14]], axis='columns')

path = "/Users/rieke/Desktop/testen_clean.csv"

test.to_csv(path)