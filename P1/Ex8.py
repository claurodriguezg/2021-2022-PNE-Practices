import Seq1
print("----| Exercise 1, Exercise 8 |-----")
s1 = Seq1.Seq("")
s2 = Seq1.Seq("ACTGA")
s3 = Seq1.Seq("FDAAC")
if s1.null() == True:
    print(f"Sequence 0: (Length: {s1.len()}) NULL ")
    print(f"{s1.count()[5]}")
    print(f"Rev: {s1.reverse()}") #error here
    print(f"Comp: {s1.complement()}")
print(f"Sequence 1: (Length: {s2.len()}) {s2}")
print(f"{s2.count()[5]}")
print(f"Rev: {s2.reverse()}")
print(f"Comp: {s2.complement()}")
print(f"Sequence 2: (Length: {s3.new_len()}) {s3}")
print(f"{s3.count()[5]}")
print(f"Rev: {s3.reverse()}")
print(f"Comp: {s3.complement()}")