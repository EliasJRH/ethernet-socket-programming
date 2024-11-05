#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <unistd.h>

int main() {
    const char *multicast_group = "239.100.110.211"; // multicast group address
    int multicast_port = 12345; // multicast port
    const char *interface_ip = "192.168.1.22"; // IP of the network interface

    int sock;
    struct sockaddr_in addr;
    struct ip_mreqn mreq;

    // Create UDP socket
    if ((sock = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("Socket creation failed");
        exit(1);
    }

    // Set up the address structure
    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_port = htons(multicast_port);
    addr.sin_addr.s_addr = htonl(INADDR_ANY);

    // Bind the socket to the specified port
    if (bind(sock, (struct sockaddr*)&addr, sizeof(addr)) < 0) {
        perror("Binding failed");
        close(sock);
        exit(1);
    }

    // Configure the multicast request structure
    memset(&mreq, 0, sizeof(mreq));
    mreq.imr_multiaddr.s_addr = inet_addr(multicast_group); // multicast group address
    mreq.imr_address.s_addr = inet_addr(interface_ip); // IP of the network interface
    mreq.imr_ifindex = 0; // set to 0 if not using interface index directly

    // Join the multicast group on the specified interface
    if (setsockopt(sock, IPPROTO_IP, IP_ADD_MEMBERSHIP, &mreq, sizeof(mreq)) < 0) {
        perror("Setting IP_ADD_MEMBERSHIP failed");
        close(sock);
        exit(1);
    }

    printf("Joined multicast group %s on interface %s, port %d\n", multicast_group, interface_ip, multicast_port);

    // Your code here to receive data...
    while (1) {

    }

    // Cleanup
    close(sock);
    return 0;
}
