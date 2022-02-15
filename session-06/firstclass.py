class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inherite
       the methods from the Seq class
    """
    pass

    def __init__(self, strbases, name=""):
        # -- Call first the Seq initilizer and then the
        # -- Gene init method
        super().__init__(strbases)
        self.name = name #this is not in the parent class. im defining an additional attribute
        print("New gene created")

    def __str__(self):
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.strbases



# Main program
# Create an object of the class Seq
s1 = Seq("AGTACACTGGT")  #i dont have to write self here.
g = Gene("CGTAAC", "FRAT1")  # gene is still a seq but i want to specialize more
#frat1 is the name of the gene

# Create another object of the Class Seq
s2 = Seq("CGTAAC")



# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")
print(f"Gene: {g}")

#everytime i create an object it will go through the init function (thats why we gets "new sew created!" twice

