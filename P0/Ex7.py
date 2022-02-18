import seq0

FOLDER = "./sequences/"
f = open(FOLDER + "U5.txt", "r").read()
full_f = f[f.find("\n") + 1:].replace("\n", "")
compl, string = seq0.seq_complement()
print("Frag: ", string)
print("Comp: ", compl)
