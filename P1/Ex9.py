import Seq1
print("----| Exercise 1, Exercise 9 |-----")

s = Seq1.Seq()
s.read_fasta("../P0/sequences/U5.txt")


print(f"Sequence: (Length: {s.len()}) {s}")
print(f"    Bases: {s.count()[5]}")
print(f"    Rev: {s.reverse()}")
print(f"    Comp: {s.complement()}")
