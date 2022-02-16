from seq1 import Seq
str_list = ["ACCTGC", "hello? Am I a valid sequence?"]

# print(Seq.validsequence2(st1)):
sequence_list = []

for st in str_list:
    if Seq.valid_sequence2(st):
        sequence_list.append(Seq(st))
    else:
        sequence_list.append(Seq("ERROR"))

for i in range(0, len(sequence_list)):
    print("Sequence", str(i) + ":", sequence_list[i])

#everytime there is a number we use loops

