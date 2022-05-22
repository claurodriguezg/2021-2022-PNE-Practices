import http.server
import socketserver
import termcolor  # if we have it in gery it means we are not using the module yet
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
import http.client
import json

HTML_FOLDER = "./html/"
SERVER = 'rest.ensembl.org'
PARAMS = '?content-type=application/json'

def species_function (species_all,limit):
    for i in range(0, limit):
        selected_species = species_all[i]["common_name"]
        print(selected_species)
        return selected_species

def read_html_file(filename):
    contents = Path(HTML_FOLDER + filename).read_text()
    contents = j.Template(contents)
    return contents


def make_ensembl_request(url,params):
    #connect with the server
    conn = http.client.HTTPConnection(SERVER)
    parameters = '?content-type=application/json'
    # -- Send the request message, using the GET method. We are requesting the main page (/)
    try:
       conn.request("GET", url + parameters + params)

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()  # -- Read the response message from the server

    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason} \n")
    # -- Read the response´s body
    data1 = r1.read().decode('utf-8')  #this is the dictionary

    # -- Print the received data
    our_dict = json.loads(data1)
    return our_dict


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
                        {"genes": SERVER + "info/species" + PARAMS})
        elif path == "/list_species":

            dict_answer = make_ensembl_request("/info/species", "")
            species_all = dict_answer["species"]
            limit = int(arguments['limit'][0])
            species = species_all[0: limit ][0]
            print(species)

            result = species_function(species_all, limit)

            print(result)


            contents = read_html_file(path[1:] + ".html")\
                .render(context = {"species": result ,
                                   "n_species": len(species_all),
                                   "limit": limit})



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