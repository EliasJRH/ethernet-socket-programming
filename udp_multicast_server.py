import socket
import struct

MCAST_GRP = '239.100.110.210'
MCAST_PORT = 5007

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Set the time-to-live for messages to 1 so they do not go past the local network segment
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

while True:
  message = b'Hello, Multicast!'
  sock.sendto(message, (MCAST_GRP, MCAST_PORT))
  print(f"Sent: {message}")
