import seq0
filename = seq0.get_file()
sequence = seq0.seq_read_fasta(filename)
result = sequence[0:20]
print(result) #in order to get the amount of character we want we subtract the first number to the second number adn it has to give us the number of characters we need to print.


#import seq0
#FOLDER = "./sequences/"
#gene = input("Choose a gene: ")
#f = open(FOLDER + gene + ".txt")
#print(f.read())