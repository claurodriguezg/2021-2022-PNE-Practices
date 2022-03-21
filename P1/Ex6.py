import Seq1
print("----| Exercise 1, Exercise 6 |-----")
s1 = Seq1.Seq( )
s2 = Seq1.Seq("ACTGA")
s3 = Seq1.Seq("FDAAC")

print(f"Sequence 0: (Length: {s1.len()}) {s1}")
print(f" Bases: {s1.count()[5]}")
print(f"Sequence 1: (Length: {s2.len()}) {s2}")
print(f" Bases: {s2.count()[5]}")
print(f"Sequence 2: (Length: {s3.len()}) {s3}")
print(f" Bases: {s3.count()[5]}")