
import http.client
import termcolor
import json

PORT = 6123
IP = 'localhost'
SERVER = 'rest.ensembl.org'

print(f"\nConnecting to server: {IP}:{PORT}\n")

def make_ensembl_request(url,params):

    conn = http.client.HTTPConnection(IP,PORT)


    try:
       conn.request("GET", url + params)

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason} \n")

    data1 = r1.read().decode('utf-8')

    our_dict = json.loads(data1)
    return our_dict


def print_menu():

    print("""THESE ARE THE OPTIONS YOU CAN CHOOSE FROM:
         Basic level:
         1. A list of species
         2. The karyotype of a specie
         3. The length of a chromosome of a specie
         Medium level:
         4. A sequence of a given gen
         5. The information of a given gen
         6. Some calculations with a given gen
         7. A list of gens from a specific region of a chromosome
         ---
         8. End the program
         """)
def get_option():
    exit = False
    while not exit:
        option = input("Which option do you want to choose: ")
        if option.isdigit():
            option = int(option)
            exit = True
        else:
            print("The selected option needs to be an integer number: ", end = "")
    return option

exit = False

GENES = ["FRAT1", "ADA", "FXN", "RNU6_269P", "MIR633", "TTTY4C",
                 "RBMY2YP", "FGFR3",  "KDR", "ANK2"]

while not exit:
    print_menu()

    option = get_option()


    if option == 1:

        termcolor.cprint("BASIC: ", 'blue')

        limit = input("How many species are you looking for?: ")
        try:
            if limit.isdigit():

                listSpecies = make_ensembl_request("/list_species?", "limit=" + str(limit) + "&json=1")

                termcolor.cprint("The total amount of species in the database is: ", 'red', end="")
                print(listSpecies["n_species"])
                termcolor.cprint("The limit chosen is: ", 'red', end="")
                print(listSpecies["limit"])
                termcolor.cprint("The list of species is: ", 'red')
                for i in listSpecies["species"]:
                    print(" - ", i)
            else:
                termcolor.cprint("The limit must be an integer.", 'yellow')
        except TypeError:
            termcolor.cprint("Please write a number up to 311.", 'yellow')

    elif option == 2:

        termcolor.cprint("BASIC: ", 'blue')

        specie = input("Whose karyotype would you like to know? Write the specie: ")

        try:

            karyotype = make_ensembl_request("/karyotype?", "specie=" + str(specie) + "&json=1")
            termcolor.cprint("The karyotype is: ", 'red')
            for k in karyotype["karyotype"]:
                print(k)
        except TypeError:
            termcolor.cprint("Something went wrong. That choice does not exist in the database. Please try again.", 'yellow')

    elif option == 3:

        termcolor.cprint("BASIC: ", 'blue')
        specie = input("Write the specie: ")
        n_chromo = input("Which chromosome´s length would you like to know ?: ")
        try:
            chromosome_L = make_ensembl_request("/chromosomeLength?", "specie=" + str(specie) + "+&chromosome=" + str(n_chromo) + "&json=1")
            termcolor.cprint("The length of the chromosome is: ", 'red', end="" )
            print(chromosome_L["l"])
        except TypeError:
            termcolor.cprint("Something went wrong. That choice does not exist in the database. Please try again.",
                             'yellow')

    elif option == 4:
        termcolor.cprint("MEDIUM: ", 'blue')

        termcolor.cprint("""The genes you can choose from are: 
        FRAT1,  ADA,  FXN,  RNU6_269P,  MIR633,
        TTTY4C,  RBMY2YP,  FGFR3,  KDR,  ANK2""", 'magenta')
        gene = input("Choose a gen: ")

        try:

            if gene in GENES:

                dict_answer = make_ensembl_request("/geneSeq?", "seq=" + str(gene) + "&json=1")
                termcolor.cprint("The sequence of the gene is:", 'red')
                print(dict_answer)

            else:
                termcolor.cprint("The gen selected is not in the list. Please choose a gen from the list", 'yellow')
        except TypeError:
            termcolor.cprint("Something went wrong. That choice does not exist in the database. Please try again.",
                             'yellow')


    elif option == 5:
        termcolor.cprint("MEDIUM: ", 'blue')
        termcolor.cprint("""The genes you can choose from are: 
                FRAT1,  ADA,  FXN,  RNU6_269P,  MIR633,
                TTTY4C,  RBMY2YP,  FGFR3,  KDR,  ANK2""", 'magenta')

        try:

            gene = input("Choose a gen: ")
            if gene in GENES:
                info = make_ensembl_request("/geneInfo?", "info=" + str(gene) + "&json=1")
                termcolor.cprint("The chosen gene is: ", 'red', end="")
                print(gene)
                termcolor.cprint("The id of the gene is: ", 'red', end="")
                print(info["id"])
                termcolor.cprint("The name of the gene´s chromosome is: ", 'red', end="")
                print(info["chromosome_n"])
                termcolor.cprint("The gene starts at: ", 'red', end="")
                print(info["start"])
                termcolor.cprint("The gene ends at: ", 'red', end="")
                print(info["end"])
                termcolor.cprint("The length of the gene is: ", 'red', end="")
                print(info["l"])
            else:
                termcolor.cprint("That gene is not in the list, choose another one that is on the list", 'yellow')
        except TypeError:
            termcolor.cprint("Something went wrong. That choice does not exist in the database. Please try again.",
                             'yellow')


    elif option == 6:
        termcolor.cprint("MEDIUM: ", 'blue')
        termcolor.cprint("""The genes you can choose from are: 
                        FRAT1,  ADA,  FXN,  RNU6_269P,  MIR633,
                        TTTY4C,  RBMY2YP,  FGFR3,  KDR,  ANK2""", 'magenta')

        gene = input("Choose a gen: ")
        try:
            if gene in GENES:
                calc = make_ensembl_request("/geneCalc?", "calc=" + str(gene) + "&json=1")
                percentages = calc["p"].split("%")
                percentages.remove(percentages[-1])
                termcolor.cprint("The percentages of the bases are: ", 'red')
                for i in percentages:
                    i.split(":")
                    print(i+"%")
                termcolor.cprint("The length of the gene is: ", 'red', end="")
                print(calc["length"])

            else:
                termcolor.cprint("That gene is not in the list, choose another one that is on the list", 'yellow')
        except TypeError:
            termcolor.cprint("Something went wrong. That choice does not exist in the database. Please try again.",
                             'yellow')



    elif option == 7:
        termcolor.cprint("MEDIUM: ", 'blue')
        specie = input("Write the specie: ")
        name_c = input("Write the name of a chromosome: ")
        start_point = input("Write a startpoint: ")
        end_point = input("Write an endpoint: ")
        try:

            list = make_ensembl_request("/geneList?", "specie=" + str(specie) + "+&name_chromo=" + str(name_c) + "&start=" +
                                        str(start_point) + "&end=" + str(end_point) + "&json=1")
            termcolor.cprint("The list of the genes is: ", 'red')
            for i in list["n_g"]:
                print(" - ", i)
        except TypeError:
            termcolor.cprint("Something went wrong. That choice does not exist in the database. Please try again.",
                             'yellow')


    elif option == 8:
        termcolor.cprint("You have ended the program correctly.", 'red')
        exit = True









