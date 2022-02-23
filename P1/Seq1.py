class Seq:

    def __init__(self, strbases): #strbasis son los parametros de la sequencia
        self.strbases = strbases #bases de la sequencia (self --> constructor)
        if not self.valid_sequence():
            self.strbases = "ERROR"
            print("ERROR !!")
        else:
            print("New sequence created !")

    def __init__(self, strbases = "NULL"):
        self.strbases = strbases  # bases de la sequencia (self --> constructor)
        if not self.valid_sequence():
            self.strbases = "ERROR"
            print("INVALID Seq!")

        elif len(self.strbases) == 0:
            print("NULL Seq created")

        else:
            print("New sequence created !")



    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases


    def valid_sequence(self):
        # add a method to a function
        # in classes the functions can be written in any order --> they don´t have to be in order to be called one by one
        valid = True
        i = 0
        while i < len(self.strbases) and valid:
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def len(self):
        """Calculate the length of the sequence"""
        if not self.strbases == "ERROR":
            len(self.strbases) == 0
        return len(self.strbases)

    def null(self):
        """Check if the length of the sequence is 0"""
        return len(self.strbases) == 0

    def seq_read_fasta(self):
        f = open("./sequences/" + self + ".txt",  "r").read()
        self.strbases = f[f.finf("\n"):].replace("\n", "")






