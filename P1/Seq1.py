class Seq:

    def __init__(self, strbases = "NULL"):  #strbasis son los parametros de la sequencia
        self.strbases = strbases  # bases de la sequencia (self --> constructor)

        if strbases == "NULL":
            print("NULL Seq created !")

        elif not self.valid_sequence():
            self.strbases = "ERROR"
            print("INVALID Seq!")

        else:
            self.strbases = strbases
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
        new_len = ""
        if self.strbases == "ERROR" or self.strbases == "NULL":
            new_len = 0
            return(new_len)
        else:
            return len(self.strbases)


    def seq_read_fasta(self):
        f = open("./sequences/" + self + ".txt",  "r").read()
        self.strbases = f[f.finf("\n"):].replace("\n", "")


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

        if len(reversed_str) == 0:
            reversed_str = "NULL"

        return reversed_str

    def complement(self):
        compl = ""
        for g in self.strbases:
            if g == "A":
                compl += "T"
            elif g == "T":
                compl += "A"
            elif g == "C":
                compl += "G"
            elif g == "G":
                compl += "C"
        if len(compl) == 0:
            compl = "NULL"
        if self.strbases == "ERROR":
            compl = "ERROR"
        return compl

    def read_fasta(self, filename):
        from pathlib import Path
        file_contents = Path(filename).read_text()
        lines = file_contents.splitlines()
        body = lines[1:]
        self.strbases = ""
        for lines in body:
            self.strbases += lines
        #we are introducing the seq in a strbases (just the body)

    def genes_bases(self):
        bases = ["A", "C", "G", "T"]
        count_a, count_c, count_g, count_t = self.count_base()
        total = [count_a, count_c, count_g, count_t]
        d = dict(zip(total, bases))
        ordered = max(d)

        return(ordered, d)








