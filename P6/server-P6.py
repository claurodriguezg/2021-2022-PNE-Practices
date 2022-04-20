import http.server
import socketserver
import termcolor  #if we have it in gery it means we are not using the module yet
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse

HTML_FOLDER = ".html/"
LIST_SEQUENCES = ["AGTTAACCAAGAT", "AGGAATTACA", "ATTTACCAGAATA",
                  "GGGTAAACATAG", "ATACAGATAAGATC", "AGAGATACTA"]
LIST_GENES = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]

def read_html_file(filename):
    contents = Path(HTML_FOLDER + filename).read_text()
    contents =j.Template(contents)
    return contents


# Define the Server's port
PORT = 6123

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

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        print("The old path was", self.path)
        print("The new path is", url_path.path)
        print("arguments")
        # Message ti send back to the client
        if self.path == "/":
            contents = read_html_file("index.html")\
                .render(context={"n_sequences": len(LIST_SEQUENCES)})
        elif path == "/ping":
            contents = read_html_file(path[1:] + ".html").render()
        elif path == "/get":
            n_sequence = int(arguments["n_sequence"][0]) #always an int #the 0 is important to acces to this value
            sequence = LIST_SEQUENCES[n_sequence]
            contents = read_html_file(path[1:] + ".html")\
                .render(context={
                "n_sequence":n_sequence,
                "sequence": sequence
            })

        else:
            contents = "I am the happy server! :-)"


        # Message to send back to the clinet
        contents = "I am the happy server! :-)"

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/plain')
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