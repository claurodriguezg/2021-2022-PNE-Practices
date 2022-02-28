import Seq1
print("----| Exercise 1, Exercise 4 |-----")
s1 = Seq1.Seq("")
s2 = Seq1.Seq("ACTGA")
s3 = Seq1.Seq("FDAAC")

if s1.null() == True:
    print(f"Sequence 1: (Length: {s1.len()}) NULL ")
print(f"Sequence 2: (Length: {s2.len()}) {s2}")
print(f"Sequence 3: (Length: {s3.new_len()}) {s3}")