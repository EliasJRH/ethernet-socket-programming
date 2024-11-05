import socket
import struct

# Configuration
multicast_group = '239.100.110.210'  # Multicast group address
multicast_port = 50002         # Multicast port
interface_ip = '192.168.1.22'   # Local IP address of the interface (replace with your interface's IP)

# Create the UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Allow multiple programs to use the same socket (optional, for testing)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to listen on the specified port on all interfaces
sock.bind(('', multicast_port))

# Construct the multicast request using the ip_mreq structure format for Windows compatibility
# This includes:
# - multicast group IP address (in_addr)
# - interface IP address
mreq = struct.pack('=4s4s', socket.inet_aton(multicast_group), socket.inet_aton(interface_ip))

# Join the multicast group on the specified interface IP
try:
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    print(f"Joined multicast group {multicast_group} on interface {interface_ip}, port {multicast_port}")
except OSError as e:
    print(f"Failed to join multicast group: {e}")
    sock.close()
    exit(1)

# Now ready to receive data from the multicast group
try:
    message = b"Hello, Multicast Group!"
    sock.sendto(message, (multicast_group, multicast_port))
    print(f"Sent message: {message.decode()}")
    while True:
        input()
        break
        # data, address = sock.recvfrom(1024)
        # print(f"Received data from {address}: {data}")
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    # Leave the multicast group and close the socket
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_DROP_MEMBERSHIP, mreq)
    sock.close()
    print("Left multicast group and closed socket.")
