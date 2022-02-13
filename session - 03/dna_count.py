chain = input("Enter a sequence of DNA (the bases should be C, A, T and G: ")
count_a = 0
count_c = 0
count_g = 0
count_t = 0
for base in chain:

    if base == "A":
        count_a += 1
    elif base == "C":
        count_c += 1
    elif base == "G":
        count_g += 1
    elif base == "T":
        count_t += 1
    else:
        print("The chain´s bases must be A,C,T or G")


print("Total lenght: ", len(chain))
print("A: ", count_a)
print("C: ", count_c)
print("T: ", count_t)
print("G: ", count_g)


