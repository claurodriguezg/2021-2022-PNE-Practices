import seq0

FOLDER = "./sequences/"
f = open(FOLDER + "U5.txt", "r").read()
full_f = f[f.find("\n") + 1:].replace("\n", "")
string, reverse_string = seq0.seq_reverse(full_f)
print("Frag: ", string)
print("Rev:  ", reverse_string)