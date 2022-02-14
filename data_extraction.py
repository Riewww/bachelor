id = []
seq = []
seqcut = []
start = []
end = []
description = []

#uses method split and cut results
def get(results):
    split_results(results)
    cut_sequence(seq, start, end)


#splits results tuple and saves it into id, seq, start and end
def split_results(result):
    for x in result:
        a, b, c, d, e = x
        id.append(str(a))
        seq.append(b)
        start.append(c)
        end.append(d)
        description.append(e)


#uses information from start and end to cut seq and saves the cut sequence into seqcut
def cut_sequence(seq, start, end):
    i = 0
    for x in seq:
        seqcut.append(str(x)[(int(str(start[i]))-1):(int(str(end[i]))+1)])
        i = i + 1
    return seqcut
