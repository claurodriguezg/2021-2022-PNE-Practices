class Seq:

    def __init__(self, strbases):
        self.strbases = strbases
        if not self.valid_sequence():
            self.strbases = "ERROR"
            print("ERROR !!")
        else:
            print("New sequence created")


    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

