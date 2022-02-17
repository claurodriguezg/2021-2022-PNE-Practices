import seq0
gene_list = ["U5", "ADA", "FRAT1", "FXN"]

print("------| Exercise 4 |------")
for g in gene_list:
    FOLDER = "./sequences/"
    f = open(FOLDER + g + ".txt", "r").read()
    full_f = f[f.find("\n") + 1:].replace("\n", "")
    dict_bases = seq0.seq_count_base(gene_list, full_f)

    print("Gene", g, ":")
    print(" A: ", dict_bases["A"], "\n", "C: ", dict_bases["C"], "\n", "T: ", dict_bases["T"], "\n", "G: ", dict_bases["G"] )


