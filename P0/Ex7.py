import seq0

f = open("U5.txt", "r").read()
full_f = f[f.find("\n") + 1:].replace("\n", "")
string, compl = seq0.seq_complement(full_f)
print ( "-----| Exercise 7 |-----")
print("Gene U5:")
print("Frag: ", string)
print("Comp: ", compl)
