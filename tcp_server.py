import socket
import time
import random

HOST = 'localhost'
PORT = 9999

def generate_stock_data():
    symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']
    symbol = random.choice(symbols)
    timestamp = time.strftime("%H:%M:%S")
    price = round(random.uniform(100, 500), 2)
    return f"{symbol},{timestamp},{price}\n"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"TCP server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        try:
            while True:
                stock_data = generate_stock_data()
                conn.sendall(stock_data.encode())
                time.sleep(1)
        except KeyboardInterrupt:
            print("Server interrupted")
            break