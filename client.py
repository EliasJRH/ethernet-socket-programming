import socket

# 1. Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connect to the server's IP address and port (replace with the server's IP)
# server_ip = '192.168.1.10'  # Replace with the IP address of the server machine
server_ip = input("Enter the server IP (Check ipconfig output): ")
server_port = 12345  # Same port as the server

client_socket.connect((server_ip, server_port))

# 3. Receive data from the server
data = client_socket.recv(1024)
print(f"Received from server: {data.decode()}")

# 4. Send data to the server
client_socket.send(b"Hello, Server!")

# 5. Close the socket
client_socket.close()