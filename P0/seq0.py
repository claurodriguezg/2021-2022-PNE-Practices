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

def seq_len(seq):
    list_genes = ["U5", "ADA", "FRAT1", "FXN"]
    for g in list_genes:
        result = seq(g)
    return list_genes, result, g

