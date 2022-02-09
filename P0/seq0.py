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
