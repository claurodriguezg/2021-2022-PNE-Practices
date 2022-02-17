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

def seq_len(gene_list, full_f):
    for g in gene_list:
        length = len(full_f)

    return length

def seq_count_base(gene_list, full_f):
    bases = ["A", "C", "T", "G"]
    for g in gene_list:
        a = count(bases[0])
        c = count(bases[1])
        t = count(bases[2])
        g = count(bases[3])
    return a, c, t, g






