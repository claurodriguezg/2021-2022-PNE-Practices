# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json
import Seq1

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

for d in genes_dict:
    KEY = d

    SERVER = 'rest.ensembl.org'
    ENDPOINT = '/sequence/id'
    PARAMS = '?content-type=application/json'
    URL = ENDPOINT + "/" + genes_dict[KEY] + PARAMS


    print(f"\nServer: {SERVER}")
    print("URL:", URL)


    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)

    # -- Send the request message, using the GET method. We are
    # -- requesting the main page (/)
    try:
        conn.request("GET", URL)  #we dont add server here
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")


    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    data1 = json.loads(data1)  #this is a diccionary now

    print("Gene: ", KEY)
    print("Description:", data1["desc"])
    SEQ = data1["seq"]
    s = Seq1.Seq(SEQ)
    print(f"Total length: {s.len()}")

    bases_count_dict = s.count()[5]

    for b in bases_count_dict:
        percentage = str(round((bases_count_dict[b]/s.len()) * 100, 1))
        print(b, ":", bases_count_dict[b], "(" + percentage + "%)")

    ordered, d = s.genes_bases()
    print("Most frequent Base: ", d[ordered])
