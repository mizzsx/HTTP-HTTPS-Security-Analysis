
import ssl
import http.client

# Trust our locally generated certificate
context = ssl.create_default_context(cafile="cert.pem")

# Establish an HTTPS connection
connection = http.client.HTTPSConnection(
    "127.0.0.1",
    8443,
    context=context
)

connection.connect()

print("Secure connection established!")
print("TLS version:", connection.sock.version())

# Request the webpage
connection.request("GET", "/")
response = connection.getresponse()

print("HTTP status:", response.status)
print(response.read().decode())

connection.close()
