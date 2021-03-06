import socket

class Client:

    PORT = 9000
    IP = "localhost"


    def __init__(self, ip, port):
        self.port = port
        self.ip = ip

    def ping(self):
        print("OK")

    def __str__(self):

        return "Connection to SERVER at "  +  str(self.ip) + "," + " PORT: " + str(self.port)

    def talk(self, msg): #msg from server
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data.
        s.send(str.encode (msg))

        # Receive data
        response = s.recv(2048).decode("utf-8")

        # Close the socket
        s.close()

        # Return the response
        return response





