import seq0

g, length = seq0.seq_len()

print("------| Exercise 3 |------")
if g == "U5":
    print("Gene U5 ---> Length: ", length )
elif g == "ADA":
    print("Gene ADA ---> Length: ", length)
elif g == "FRAT1":
    print("Gene FRAT1 ---> Length: ", length)
else:
    print("Gene FXN ---> Length: ", length)

