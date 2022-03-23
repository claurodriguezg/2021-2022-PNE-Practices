from Client0 import Client
import termcolor
import P1.Seq1


PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 9000

c = Client(IP, PORT) #pair
print(c)  #printing the sentence of connection

genes = ["U5", "FRAT1", "ADA"] #this are the genes i want to send

for g in genes: #reading the list

    FOLDER = "../P0/Sequences/"  # looking for it
    gene = FOLDER + g + ".txt"
    #f = open(gene, "r").read() #reading the gene
    #full_f = f[f.find("\n") + 1:].replace("\n", "") #getting just the body of the gene (i just want to send this)
    seq = P1.Seq1.Seq()
    seq.read_fasta(gene)




    msg = "Sending the " + g + " Gene to the server..."

    response1 = c.talk(msg)
    response2 = c.talk(seq)


    termcolor.cprint(f"To Server: {msg}", "blue")
    termcolor.cprint(f"From Server: {response1}", "yellow")
    termcolor.cprint(f"To Server: {seq}", "blue")
    termcolor.cprint(f"From Server: \n {response2}", "yellow")




    #termcolor.cprint(f"To the Server: {msg}", "blue")
    #termcolor.cprint(f"To the Server: {full_f}", "yellow")

    #print(f"From Server:  \n \n{response}")ççexit = False

