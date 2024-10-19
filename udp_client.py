import socket

def udp_client():
  server_address = ('localhost', 12345)
  buffer_size = 1024

  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    while True:
      message = input("Enter message to send to server (type 'close' to exit): ")
      sock.sendto(message.encode(), server_address)
      
      if message.lower() == 'close':
        print("Closing connection.")
        break

      data, _ = sock.recvfrom(buffer_size)
      print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
  udp_client()