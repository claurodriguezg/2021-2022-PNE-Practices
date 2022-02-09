from pathlib import Path
FILENAME = "RNU6_269P.txt"   #we write filename in capital letters so it becomes a constant
#open and read the file
file_contents = Path(FILENAME).read_text()
print(file_contents)  #print the contents on the console

#the file I want to open neeed to be in the same directory as the pyhton file


