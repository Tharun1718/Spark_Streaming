import socket

HOST='localhost'
PORT=9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST,PORT))


server_socket.listen(5)

print(f"Server listening on {HOST}:{PORT}")

while True:
    client_socket,client_address = server_socket.accept()
    print(f"Connected to a client at {client_address}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received from the client: {data.decode()}")

    client_socket.close()