import socket
import struct

MCAST_GRP = '239.100.110.210'
MCAST_PORT = 5007

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Allow multiple sockets to use the same PORT number
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to the port that we know will receive multicast data
sock.bind(('', MCAST_PORT))

# Tell the kernel that we are a multicast socket
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

# Tell the kernel to add us to the multicast group on all interfaces
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Receive data from the socket
while True:
  data, addr = sock.recvfrom(1024)
  print(f"Received message: {data} from {addr}")
