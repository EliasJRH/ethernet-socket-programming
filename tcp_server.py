import socket

def start_server(host='0.0.0.0', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                message = data.decode()
                print(f"Received message: {message}")
                conn.sendall("Message received".encode("utf-8"))
                if message.lower() == "close":
                    print("Closing connection.")
                    break

if __name__ == "__main__":
    start_server()