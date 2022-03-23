import socket
from class_client import Client

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

PORT = 8080
IP = "127.0.0.1"

print("Connection to SERVER at", IP, ", PORT:", PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
c = Client(IP, PORT)


#ping:

print("* Testing PING...")
s.send(str.encode("PING"))
msg = s.recv(2048)
print(msg.decode("utf-8"))

print("\n")

#get

print("* Testing GET...")
args = ["0", "1", "2", "3", "4"]
for a in args:
    msg = c.talk("GET " + a)
    print("GET", a + ": " + msg)

message = c.talk("GET 0")


print("\n")

#info
print("* Testing INFO...")
msg = c.talk("INFO " + message)
print(msg)

print("\n")

#comp
print("* Testing COMP...")
msg = c.talk("COMP " + message)
print(msg)

print("\n")

#rev
print("* Testing REV...")
msg = c.talk("REV " + message)
print(msg)

print("\n")

#gene

print("* Testing GENE...")
args = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
for g in args:
    msg = c.talk("GENE " + g)
    print("GENE", g + "\n " + msg)















