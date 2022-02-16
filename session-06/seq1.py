class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases  #we need to assign error to this property whenever its necessary
        if not self.valid_sequence():  #this should be done outside
            self.strbases = "ERROR"
            print("ERROR !!")
        else:
            print("New sequence created 1")

    def __str__(self):  # transofrms a class to the str we want to print.
        """Method called when the object is being printed"""
        # if we don´t have this function we will print the location and type of class

        # -- We just return the string with the sequence
        return self.strbases

    @staticmethod

    def valid_sequence2(sequence): #since the arg is in white it is not expecticting any class
        valid = True
        i = 0
        while i < len(sequence) and valid:
            c = sequence[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid
    #it depends on how in want to solve it: if i want to check my seq before intiating the class or after

    def valid_sequence(self):
        #add a method to a function
        #in classes the functions can be written in any order --> they dont have to be in prder to be called one by one
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
