import Seq1
print("----| Exercise 1, Exercise 9 |-----")
s = Seq1.Seq()

f = open("U5.txt", "r").read()
FILENAME = f[f.find("\n") + 1:].replace("\n", "")
s.read_fasta(FILENAME)

#for g in FILENAME:
    #s += g

print(f"Sequence: (Length: {s.len()}) {s.read_fasta(FILENAME)}")
print(f"    Bases: {s.count()[5]}")
print(f"    Rev: {s.reverse()}")
print(f"    Comp: {s.complement()}")
