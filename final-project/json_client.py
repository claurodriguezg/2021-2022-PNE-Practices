
import http.client
import termcolor
import json

PORT = 8080
IP = 'localhost'

print(f"\nConnecting to server: {IP}:{PORT}\n")

def make_ensembl_request(url,params):

    conn = http.client.HTTPConnection(IP,PORT)


    try:
       conn.request("GET", url + params)

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason} \n")

    data1 = r1.read().decode('utf-8')


    our_dict = json.loads(data1)
    return our_dict

print("BASIC: ")

print()

limit = str(input("How many species are you looking for?: "))

termcolor.cprint("The list of species is: ")
listSpecies = make_ensembl_request("/listSpecies?", "limit=" + limit + "&json=1")
print(listSpecies)






