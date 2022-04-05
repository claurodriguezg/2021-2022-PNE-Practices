import socket
import termcolor
import pathlib


# -- Server network parameters
IP = "127.0.0.1"
PORT = 21000

def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\n')

    # -- The request line is the first
    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    # -- Generate the response message
    # It has the following lines
    # Status line
    # header
    # blank line
    # Body (content to send)
    print(req_line)
    route =req_line.split(" ")[1] #everytime i change the server i need to run it
    #if we change the htmlfile WE DO NOT NEED TO RESTART IT in order for it to function
    print("ROUTE", route)

    if route == "/": #this route right now is not defined
        #this new contesnts are written in HTML file
        body = pathlib.Path("html/index.html").read_text()
    #elif route == "/goodbye/":
        #body = pathlib.Path("html/goodbye.html").route_text()
    #elif route == "/question":
        #body = pathlib.Path("html/question.html").read_text()
    elif route == "/favicon.ico":
        body = pathlib.Path("html/info/A.html").read_text()
    else:
        try:
            filename = route[1:]
            filename.split("/")[-1]
            body = pathlib.Path("html/" + filename + ".html").read_text()
        except FileNotFoundError:
            body = pathlib.Path("html/Error.html").read_text()



    # This new contents are written in HTML language
    # -- Status line: We respond that everything is ok (200 code)
    status_line = "HTTP/1.1 200 OK\n"

    # -- Add the Content-Type header
    header = "Content-Type: text/html\n"

    # -- Add the Content-Length
    header += f"Content-Length: {len(body)}\n" #exactly the number of bytes of the body

    # -- Build the message by joining together all the parts
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


# -------------- MAIN PROGRAM
# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()

print("SEQ Server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:

        # Service the client
        process_client(cs)

        # -- Close the socket
        cs.close()
