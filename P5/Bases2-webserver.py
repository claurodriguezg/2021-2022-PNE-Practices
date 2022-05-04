import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse

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

        # We just print a message
        print("GET received! Request line:")

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Print the command received (should be GET)
        print("  Command: " + self.command)

        # Print the resource requested (the path)
        print("  Path: " + self.path)

        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        # Message to send back to the client
        if self.path == "/":
            contents = pathlib.Path("html/index.html").read.text()

        elif path == "/favicon.ico":
            contents = pathlib.Path("html/info/A.html").read_text()

        else:
            try:
                filename = path[1:]
                #filename.split("/")[-1]
                contents = pathlib.Path("html/info/" + filename + ".html").read_text()
            except FileNotFoundError:
                contents = pathlib.Path("html/Error.html").read_text()

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