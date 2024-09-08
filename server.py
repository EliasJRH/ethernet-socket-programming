import socket

# 1. Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind to the server's IP address and port (replace with your server's private IP)
# server_ip = '192.168.1.10'  # Replace with the IP address of the server machine
server_ip = input("Enter the server IP (Check ipconfig output): ")
server_port = 12345  # Same port for both client and server

server_socket.bind((server_ip, server_port))
server_socket.listen(5)
print(f"Server listening on {server_ip}:{server_port}...")

while True:
    # 3. Accept an incoming connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # 4. Send a welcome message to the client
    client_socket.send(b"Hello, Client!")

    # 5. Receive data from the client
    data = client_socket.recv(1024)
    print(f"Received from client: {data.decode()}")

    # 6. Close the connection
    client_socket.close()