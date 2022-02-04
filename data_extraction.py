
id = []
seq = []
seqcut = []
start = []
end = []



def get(results):
    split_results(results)
    cut_sequence(seq,start,end)



def split_results(result):
    for x in result:
        a, b, c, d = x
        id.append(str(a))
        seq.append(b)
        start.append(c)
        end.append(d)

def cut_sequence(seq,start,end):
    i = 0
    for x in seq:
        seqcut.append(str(x)[int(str(start[i])):int(str(end[i]))])
        i+1
    return seqcut



