import seq0
gene_list = ["U5", "ADA", "FRAT1", "FXN"]
print("------| Exercise 3 |------")
for g in gene_list:
    FOLDER = "./sequences/"
    f = open(FOLDER + g + ".txt", "r").read()
    full_f = f[f.find("\n") + 1:].replace("\n", "")
    length = seq0.seq_len(gene_list, full_f)
    print("Gene", g, "----> Length: ", len(full_f))

