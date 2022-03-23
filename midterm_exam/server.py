import socket
import colorama
import sequence

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

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
            list_seq = ["U5", "FRAT1", "ADA", "FXN", "RNU6_269P"]
            i = int(arg)
            if i <= 4:
                choosen = list_seq[i]
                seq = sequence.Seq()
                filename = f"./sequences/" + choosen + ".txt"
                full_f = str(seq.read_fasta(filename))
                response = full_f

        elif cmd == "INFO":
            color_txt = "INFO"
            colorama.init()
            print(colorama.Fore.GREEN + color_txt + colorama.Fore.WHITE)
            seq = sequence.Seq(arg)
            response, count = seq.bases(arg)
            #response = seq.convert_message(bases)
            response = "Sequence: " + arg + "\n" + "Total Length: " + str(len(arg)) + "\n" + response

            #response += " " + "(" + str(round((count*100)/len(arg), 3)) + "%)"

        elif cmd == "COMP":
            color_txt = "COMP"
            colorama.init()
            print(colorama.Fore.GREEN + color_txt + colorama.Fore.WHITE)
            seq = sequence.Seq(arg)
            compl = seq.complement(arg)
            response = compl + " "

        elif cmd == "REV":
            color_txt = "REV "
            colorama.init()
            print(colorama.Fore.GREEN + color_txt + colorama.Fore.WHITE)
            response = arg[::-1] + " "
            print("New sequence created!")

        elif cmd == "GENE":
            color_txt = "GENE "
            colorama.init()
            print(colorama.Fore.GREEN + color_txt + colorama.Fore.WHITE)

            seq = sequence.Seq(arg)
            #s = "../P0/sequences/" + arg + ".txt"
            #filename = seq.read_fasta(arg)
            filename = f"./sequences/" + arg + ".txt"
            full_f = seq.read_fasta(filename)
            response =  str(full_f)

        elif cmd == "OPE":
            color_txt = "GENE "
            colorama.init()
            print(colorama.Fore.GREEN + color_txt + colorama.Fore.WHITE)
            a = 0
            c = 0
            g = 0
            t = 0
            seq = sequence.Seq(arg)
            if seq.valid_sequence():
                for i in arg:
                    if i == "A":
                        a += 4
                    elif i == "C":
                        c += -3
                    elif i == "G":
                        g += 7
                    elif i == "T":
                        t += -6
                response = str(a + c + g + t) + " "

            elif seq == "ERROR" or "NULL":
                response = "We could not sum the bases since the sequence is not correct."

        else:

            response = "HELLO. I am the Server :-)\n"

        print(response)



        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the data socket
        cs.close()

