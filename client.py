import telnetlib

HOST = 'localhost'  # Server host
PORT = 9999  # Server port

# Connect to the server
tn = telnetlib.Telnet(HOST, PORT)

# Send data
tn.write(b"Hello, server!\n")

# Read response (optional)
response = tn.read_all()
print(response.decode())

# Close the connection
tn.close()
