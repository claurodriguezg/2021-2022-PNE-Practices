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
        return len(self.strbases)

    def null(self):
        """Check if the length of the sequence is 0"""
        return len(self.strbases) == 0

    def seq_read_fasta(self):
        f = open("./sequences/" + self + ".txt",  "r").read()
        self.strbases = f[f.finf("\n"):].replace("\n", "")

    def new_len(self):
        new_len = ""
        if self.strbases == "ERROR":
            return len(new_len)

    def count_base(self):
        count_a = 0
        count_c = 0
        count_g = 0
        count_t = 0
        if len(self.strbases) > 0:
            count_a += self.strbases.count("A")
            count_c += self.strbases.count("C")
            count_g += self.strbases.count("G")
            count_t += self.strbases.count("T")

        return count_a, count_c, count_g, count_t

    def count(self):
        bases = ["A", "C", "G", "T"]
        count = []
        a = count.append(self.strbases.count("A"))
        c = count.append(self.strbases.count("C"))
        g = count.append(self.strbases.count("G"))
        t = count.append(self.strbases.count("T"))
        dict_six = dict(zip(bases, count))

        return a, c, g, t, count, dict_six

    def reverse(self):
        if self.valid_sequence():
            reversed_str = self.strbases[len(self.strbases) - 1 :: -1 ]
        elif not self.valid_sequence():
            reversed_str = self.strbases


        return reversed_str







