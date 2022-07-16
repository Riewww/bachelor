from Bio import SeqIO
genes = []
OG = {}

gene_file = open("/Users/rieke/Desktop/g1706_genes_for_OG.txt", 'r')
OG_file_path = "/Users/rieke/Desktop/ortho/OrthoFinder/Results_Feb25_6/Orthogroup_Sequences/"
path_aa_seq = "/Users/rieke/OneDrive - stud.hs-emden-leer.de/bachelorarbeit/braker/augustus.ab_initio.aa"

def get_genes(line):
    list = line.split()
    for word in list:
        if (word.startswith("OG")):
            continue
        else:
            genes.append(word)

def get_gene_seq(path, gene):
    for record in SeqIO.parse(path, "fasta"):
        if((gene + ".t1") ==  record.name):
            return record
for group in gene_file:
    get_genes(group)
    new_file = open("/Users/rieke/Desktop/OG_best_hits/g1706_group_" + group.split()[0] + ".fasta", 'w')
    for gene in genes:
        new_file.write(">" + str(get_gene_seq(path_aa_seq,gene).id) + "\n" + str(get_gene_seq(path_aa_seq,gene).seq) + "\n")
    for record in SeqIO.parse(OG_file_path + group.split()[0] + ".fa", "fasta"):
        OG.update({str(record.id):str(record.seq)})
    for items in OG:
        new_file.write(">" + items + "\n" + OG.get(items) + "\n")
    genes.clear()
    OG.clear()

