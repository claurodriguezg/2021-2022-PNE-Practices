# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json

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

print("\n")
print("Dictionary of Genes!")
print("There are 10 genes in the dictionary:")
print("\n")


for v,k in genes_dict.items():
    print(v + ": --> " + k)

SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/ping'
PARAMS = '?content-type=application/json'


# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT + PARAMS)  #we dont add server here
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()



# -- Read the response's body
data1 = r1.read().decode("utf-8")
data1 = json.loads(data1)  #this is a diccionary now




