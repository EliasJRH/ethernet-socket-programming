import socket

def main():
  host = '127.0.0.1'  # Server's IP address
  port = 12345        # Server's port

  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.connect((host, port))

  print("Connected to server. Type 'close' to end the connection.")
  
  while True:
    message = input("Enter message: ")
    client_socket.sendall(message.encode())

    if message.lower() == 'close':
      break

    response = client_socket.recv(1024).decode()
    print(f"Server response: {response}")

  client_socket.close()
  print("Connection closed.")

if __name__ == "__main__":
  main()