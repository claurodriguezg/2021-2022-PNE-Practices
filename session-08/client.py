import socket

# SERVER IP, PORT
# Write here the correct parameter for connecting to the
# Teacher's server
PORT = 8000 #this is to conncet to the process running inthe server
IP = "localhost" #"10.3.56.165" #with the ifconfig (inet - en0) #this is to connect with the server
#both IP and PORT have to match in order to work
#later everytime a CLIENT connects its goign to recieve a different port even tho the server maintains the same one
#if we change the servers port in the client file is not going to work because it would be like "if nobody was there to listen"
#if i wanrt to run the server from a different computer i need a different IP
#if we are in the same computer we can use a local IP also if we are using it in the same wifi




# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!"))

# Closing the socket
s.close()