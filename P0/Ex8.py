import seq0

gene_list = ["U5", "ADA", "FRAT1", "FXN"]

print("------| Exercise 8 |------")
for g in gene_list:
    FOLDER = "./sequences/"
    f = open(FOLDER + g + ".txt", "r").read()
    full_f = f[f.find("\n") + 1:].replace("\n", "")
    dict_bases = seq0.seq_count(gene_list, full_f)
    d = seq0.genes_bases(dict_bases)
    print(result)




