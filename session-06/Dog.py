class Dog:
    def __init__(self, the_name, the_age):  #this prints the data/parameters.
        self.name = the_name  #this values are to create the parameters inside the class to define my object
        self.age =  the_age

    def say_your_name(self):
        print("I'm {}, and I'm sitting down here".format(self.name))

    def say_your_age(self):
        print("I'm {} years old!".format(self.age))

    def say_what_you_like(self):
        print("I like aritmetic!")

    def multiply(self, first_operand, second_operand): #inside this to braquets i could call another function such as calculate whatever
        print(f'Easy!, the result is {first_operand * second_operand}')
        #print("The result is", first_operand * second_operand)

ares = Dog('ares', 10)
ares.say_your_name()
ares.say_your_age()
ares.say_what_you_like()
ares.multiply(3,5)

#self does not have to be defined
#self is just used to defined an atribute of a class

