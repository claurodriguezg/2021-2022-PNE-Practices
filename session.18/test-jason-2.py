import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-2.json").read_text()  #transforming it into a string

# Create the object person from the json string
person = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# Print the information on the console, in colors
print()
termcolor.cprint("Name: ", 'green', end="")
print(person['Firstname'], person['Lastname'])
termcolor.cprint("Age: ", 'green', end="")  #accessing the info
print(person['age'])

# Get the phoneNumber list
phoneNumbers = person['phoneNumber']  #we create a variable that is the value of the key phoneNumber

# Print the number of elements int the list
termcolor.cprint("Phone numbers: ", 'green', end='')
print(len(phoneNumbers))

# Print all the phone numbers   # we can do this because it is a list
for i, num in enumerate(phoneNumbers):
    termcolor.cprint("  Phone {}:".format(i), 'blue', end='')
    print(num)
