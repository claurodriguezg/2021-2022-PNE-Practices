
import http.client

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

def make_ensembl_request(url,params):

    conn = http.client.HTTPConnection(SERVER)
    parameters = '?content-type=application/json'

    try:
       conn.request("GET", url + parameters + params)

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()

    print(f"Response received!: {r1.status} {r1.reason} \n")

    data1 = r1.read().decode('utf-8')


    our_dict = json.dumps(data1)
    return our_dict

#print(f"CONTENT: {our_dict}")



