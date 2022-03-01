import Seq1
print("----| Exercise 1, Exercise 5 |-----")
s1 = Seq1.Seq("")
s2 = Seq1.Seq("ACTGA")
s3 = Seq1.Seq("FDAAC")

if s1.null() == True:
    print(f"Sequence 0: (Length: {s1.len()}) NULL ")
    print(f"A:", s1.count_base()[0], ", ", "C:", s1.count_base()[1], ", ", "G:", s1.count_base()[2], ", ", "T:", s1.count_base()[3], ",",)
print(f"Sequence 1: (Length: {s2.len()}) {s2}")
print(f"A:", s2.count_base()[0], ", ", "C:", s2.count_base()[1], ", ", "G:", s2.count_base()[2], ", ", "T:", s2.count_base()[3], ",",)
print(f"Sequence 2: Length: ({s3.new_len()}) {s3}")
print(f"A:", s3.count_base()[0], ", ", "C:", s3.count_base()[1], ", ", "G:", s3.count_base()[2], ", ", "T:", s3.count_base()[3], ",",)