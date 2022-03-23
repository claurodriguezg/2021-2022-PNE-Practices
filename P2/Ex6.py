from Client0 import Client
import termcolor
import P1.Seq1


PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 9000

c = Client(IP, PORT) #pair
print(c)  #printing the sentence of connection




FOLDER = "../P0/Sequences/"  # looking for it
gene = FOLDER + "FRAT1.txt"
#f = open(gene, "r").read() #reading the gene
#full_f = f[f.find("\n") + 1:].replace("\n", "") #getting just the body of the gene (i just want to send this)
seq = P1.Seq1.Seq()
seq.read_fasta(gene)
print(f"Gene FRAT1: {seq}")

msg = "Sending FRAT1 Gene to the server, in fragments if 10 bases..."
termcolor.cprint(f"{msg}", "yellow")

f1 = seq[0:10]
f2 = seq[11:21]
f3 = seq[23:33]
f4 = seq[34:44]
f5 = seq[45:55]
list_frag = [f1, f2, f3, f4, f5]
exit = False
while not exit:
    for f in list_frag:
        msg2 = f
        n = 1
        termcolor.cprint(f"Fragment", n, ": {msg2}", "yellow")
        exit = True

