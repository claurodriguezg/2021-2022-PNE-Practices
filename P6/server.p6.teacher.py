import http.server
import socketserver
import termcolor  # if we have it in gery it means we are not using the module yet
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse

HTML_FOLDER = "./html/"
LIST_SEQUENCES = ["ACGTCCAGTAAA", "ACGTAGTTTTTAAACCC", "GGGTAAACTACG",
                  "CGTAGTACGTA", "TGCATGCCGAT", "ATATATATATATATATATA"]
LIST_GENES = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]

def read_html_file(filename):
    contents = Path(HTML_FOLDER + filename).read_text()
    contents = j.Template(contents)
    return contents

def count_bases(seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in seq:
        d[b] += 1

    total = sum(d.values())
    for k,v in d.items():
        d[k] = [v, round((v * 100) / total,1)]
    return d

def complement(seq):
    compl = ""
    for g in seq:
        if g == "A":
            compl += "T"
        elif g == "T":
            compl += "A"
        elif g == "C":
            compl += "G"
        elif g == "G":
            compl += "C"

    return compl

def convert_message(base_count):
    message = ""
    for k,v in base_count.items():
        message += k + ": " + str(v[0]) + " (" + str(v[1]) + "%)" + "\n"
    return message

def info_operation(arg):
    base_count = count_bases(arg)
    response = "<p> Sequence: " + arg + "</p>"
    response += "<p> Total length: " + str(len(arg)) + "</p>"
    response += convert_message(base_count)
    return response

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        url_path = urlparse(self.path)
        path = url_path.path #this is the url
        arguments = parse_qs(url_path.query)  #esto es lo que conviertes en diccionario
        print("The old path was", self.path)
        print("The new path is", url_path.path)
        print("arguments", arguments)
        # Message to send back to the client
        if self.path == "/":
            contents = read_html_file("index.html")\
                .render(context=
                        {"n_sequences": len(LIST_SEQUENCES),
                         "genes": LIST_GENES})
            #el render se utiliza cuando usamos jinja. es lo mismo que el format de antes.

        elif path == "/ping":
            contents = read_html_file(path[1:] + ".html").render()
        elif path == "/get":
            n_sequence = int(arguments["n_sequence"][0])  #always an int #the 0 is important to access to this value
            sequence = LIST_SEQUENCES[n_sequence]
            contents = read_html_file(path[1:] + ".html")\
                .render(context = {
                "n_sequence": n_sequence,
                "sequence": sequence
            })
        elif path == "/gene":
            gene_name = arguments["genes"][0]
            sequence = Path("./sequences/" + gene_name + ".txt").read_text()
            sequence = sequence[sequence.find("\n"):].replace("\n", "")
            contents = read_html_file( path + ".html") \
                .render(context={
                "gene_name": gene_name,
                "sequence": sequence
            })
        elif path == "/operation":
            sequence = arguments["msg"][0]
            operation = arguments["option"][0]
            print(operation)

            if operation == "Rev":
                contents = read_html_file(path[1:] + ".html") \
                    .render(context={
                    "sequence": sequence,
                    "operation": operation,
                    "result": sequence[::-1]
                })
            elif operation == "Info":
                contents = read_html_file(path[1:] + ".html") \
                    .render(context={
                    "sequence": sequence,
                    "operation": operation,
                    "result": info_operation(sequence)
                })

            elif operation == "Comp":
                print(operation, "test")
                contents = read_html_file(path[1:] + ".html") \
                    .render(context={
                    "sequence": sequence,
                    "operation": operation,
                    "result": complement(sequence)
                    })
        else:
            contents = "I am the happy server! :-)"


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()