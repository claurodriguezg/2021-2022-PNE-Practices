from Client0 import Client

class Client(Seq):


    PRACTICE = 2
    EXERCISE = 5

    print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

    IP = "127.0.0.1"
    PORT = 9000

    c = Client(IP, PORT)
    print(c)

    genes = [U5, FRAT1, ADA]

    s.Seq1.Seq()

    for g in genes:
        FOLDER = "../P0/Sequences/"
        gene = FOLDER + g + ".txt"

        print("To Server: Sending the", g, " Gene to the server...")
        print(f"To Server: {s}")

        response = c.talk("Testing!!!")
        print(f"From Server:  \n \n{response}")