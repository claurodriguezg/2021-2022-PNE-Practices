import http
import json
import http.client

genes_dict ={"FRAT1": "ENSG00000165879",
             "ADA": "ENSG00000196839",
             "FXN": "ENSG00000165060",
             "RNU6_269P": "ENSG00000212379",
             "MIR633": "ENSG00000207552",
             "TTTY4C": "ENSG00000228296",
             "RBMY2YP": "ENSG00000227633",
             "FGFR3": "ENSG00000068078",
             "KDR": "ENSG00000128052",
             "ANK2": "ENSG00000145362"}
SERVER = 'rest.ensembl.org'
PARAMS = '?content-type=application/json'

def make_ensembl_request(url,params=""):
    #connect with the server
    conn = http.client.HTTPConnection(SERVER)
    parameters = '?content-type=application/json'
    # -- Send the request message, using the GET method. We are requesting the main page (/)
    try:
        conn.request("GET", url + parameters + params)

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = conn.getresponse()
    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason} \n")
    # -- Read the response´s body
    data1 = r1.read().decode('utf-8')
    # -- Print the received data
    our_dict = json.loads(data1)
    return our_dict


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
        contents = read_html_file("index.html").render()

    if path == '/listSpecies':
        n_species = arguments['number_species']
        dict_answer = \
            make_ensembl_request("/info/species")
        list_species = dict_answer["species"]
        list_species = list_species[0:n_species]
        content = read_html_file("html/list_species.html")\
            .render(context={"species": list_species})

