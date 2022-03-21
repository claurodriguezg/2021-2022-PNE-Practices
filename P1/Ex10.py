import Seq1
print("----| Exercise 1, Exercise 10 |-----")

gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for g in gene_list:
    FOLDER = "../P0/sequences/"
    filename = FOLDER + g + ".txt"
    s = Seq1.Seq()
    s.read_fasta(filename)
    ordered, d = s.genes_bases()
    print("Gene", g, ": Most frequent Base: ", d[ordered])



