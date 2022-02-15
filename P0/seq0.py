def seq_ping():
    print("Ok")

def get_file():
    exit = False
    while not exit:
        filename = input("What file do you want to open?: ")
        try:
            seq = open("./sequences/" + filename, "r")
            exit = True
            return filename
        except FileNotFoundError:
            print("File not found. Try again.")



def seq_read_fasta(filename):
    seq = open("./sequences/" + filename, "r").read()
    seq = seq[seq.find("\n"):].replace("\n", "")
    return seq

def seq_len():
    genes_dict = ["U5": 0, "ADA": 0, "FRAT1": 0, "FXN": 0]
    for g in genes_dict:
        FOLDER = "./sequences/"
        f = open(FOLDER + g + ".txt", "r").read()
        full_f = f[f.find("\n"):].replace("\n", "")

        for g in genes_dict:
            result = seq(g)
        return list_genes, result, g

