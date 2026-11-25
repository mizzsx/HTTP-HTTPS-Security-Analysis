
import http.server
import ssl
from functools import partial

# Server address and port
HOST = "127.0.0.1"
PORT = 8443

# Serve the webpage from the web folder
handler = partial(
    http.server.SimpleHTTPRequestHandler,
    directory="web"
)

# Create the web server
server = http.server.HTTPServer((HOST, PORT), handler)

# Configure TLS
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

# Load the certificate and private key
context.load_cert_chain(
    certfile="cert.pem",
    keyfile="key.pem"
)

# Enable encrypted communication
server.socket = context.wrap_socket(
    server.socket,
    server_side=True
)

print("HTTPS server is running!")
print("https://127.0.0.1:8443")

server.serve_forever()
