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
    bases = ["A", "C", "G", "T"]
    count_bases = []
    for g in gene_list:
        i = 0
        exit = False
        while i < len(full_f) and not exit:
            count_a = count_bases.append(full_f.count("A"))
            count_c = count_bases.append(full_f.count("C"))
            count_g = count_bases.append(full_f.count("G"))
            count_t = count_bases.append(full_f.count("T"))
            i += 1
            exit = True
        dict_bases = dict(zip(bases, count_bases))

    return dict_bases






