# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json


SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/ping'
PARAMS = '?content-type=application/json'


print(f"\nServer: {SERVER}\n")

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

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")
data1 = json.loads(data1)  #this is a diccionary now


if data1["ping"] == 1:
    print("PING OK !!! The database is running")
else:
    print("ERROR !!! The database is not running")

    # -- Print the received data
    print(f"CONTENT: {type(data1['ping'])}")

