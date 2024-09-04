from scapy.all import ARP, Ether, sendp

# Define the target IP address and the target MAC address
#target_ip = "10.53.32.1"
target_ip = "192.168.1.1"

# target_mac = "00:11:74:33:44:55"
target_mac = "FF:FF:FF:FF:FF:FF"

# Create an ARP request packet
arp_request = ARP(op=1, pdst=target_ip, hwdst=target_mac)

# Create an Ethernet frame to encapsulate the ARP request
ether = Ether(dst=target_mac)

# Combine the Ethernet frame and the ARP request
packet = ether / arp_request

# Send the packet on the network
for i in range(0,10):
    sendp(packet, iface="en0")

