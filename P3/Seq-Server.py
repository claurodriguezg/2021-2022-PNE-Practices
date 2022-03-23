import socket
import colorama
import P1.Seq1

def count_bases(arg):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in arg:
        d[b] += 1
    return d

def covert_message(base_count)





# Configure the Server's IP and PORT
PORT = 8080 #6123 always work
IP = "127.0.0.1" #you could just write localhost

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #addresses can be reused
#run two servers with the same port --> avoid adress already used error.

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()  #if we dont specified the operating system will handle by itself how any clients can be at the same time

print("SEQ Server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect...")
    try:
        (cs, client_ip_port) = ls.accept()
        # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listening socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors

    else:

        print("A client has connected to the server!")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode().replace("\n", "").strip() #strip para quitar los espacios de la izq y de la derecha
        splitted_command = msg.split(" ")
        cmd = splitted_command[0]
        #arg = msg.split(' ')[1] #if we are not using the msg again we can just do the slipt after the strip
        if cmd != "PING":
            arg = splitted_command[1]
            #print(arg)
        #print(cmd)

        # -- Print the received message
        #print(f"Message received: {msg}")

        # -- Send a response message to the client
        if msg == "PING":
            color_txt = "PING command! "
            #print(color_txt)
            colorama.init()
            print(colorama.Fore.GREEN + color_txt + colorama.Fore.WHITE)
            response = "OK!\n"

        elif cmd == "GET":
            color_txt = "GET"
            colorama.init()
            print(colorama.Fore.GREEN + color_txt + colorama.Fore.WHITE)
            list_seq = ["ACTAAG", "AGCCTAA", "ATAACCA", "ACGGGAAT", "ATACGA"]
            response = list_seq[int(arg)] + " "

        elif cmd == "INFO":
            color_txt = "INFO"
            colorama.init()
            print(colorama.Fore.GREEN + color_txt + colorama.Fore.WHITE)
            seq = P1.Seq1.Seq()
            base_count = count_bases(arg)
            response = convert_message(base_count)




        elif cmd == "REV":
            color_txt = "REV "
            colorama.init()
            print(colorama.Fore.GREEN + color_txt + colorama.Fore.WHITE)
            response = arg[::-1] + " "
            print("New sequence created!")

        else:
            response = "HELLO. I am the Server :-)\n"

        print(response)


        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the data socket
        cs.close()

