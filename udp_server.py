import socket

def udp_server(host='127.0.0.1', port=12345):
  # Create a UDP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  server_address = (host, port)
  sock.bind(server_address)

  print(f"UDP server up and listening on {host}:{port}")

  while True:
    data, address = sock.recvfrom(4096)
    print(f"Received {len(data)} bytes from {address}")
    print(data.decode())

    if data:
      sent = sock.sendto(data, address)
      print(f"Sent {sent} bytes back to {address}")

if __name__ == "__main__":
  udp_server()