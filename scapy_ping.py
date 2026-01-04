"""
Scapy is a powerful interactive packet manipulation library written in Python.

Scapy is used to manually create packets, with this lib we can create
invalid packets, malicious packets, or tracker packets that would bypass a firewall.

### Layer Cake
In Scapy, we can "stack" layers using the division operator (/), just like a sandwich.

For example:
To send a packet for Google, the packet structure would be:
1. IP Layer -> We set origin and destination
2. TCP Layer -> We set the port and flags (SYN, ACK)
3. Payload -> This one is optional, but here we'll set the data
"""

# Before we reach our target, lets 'ping' it to check its health
from scapy.all import sr1
from scapy.layers.inet import IP, ICMP

google_address = "8.8.8.8"

# We are creating the packet
# IP() create the IP header, and ICMP() created the control protocol header
packet = IP(dst=google_address) / ICMP()

print("Sending packet...")
# The method show() prints the packet "anatomy" before sends it.
# This one is amazing to understand Scapy functionality, it shows exactly
# the fields that were automatically filled up, such as, TTL, Checksum, Flags
packet.show()

response = sr1(packet, timeout=2, verbose=False)

if response:
    print(f"\n[+] Received response from: {response[IP].src}")
else:
    print("[-] No response")


"""
COMMON ISSUES:
- If while running this script, and you reach a PermissionError exception, try to run it with admin privileges:
Using Linux
sudo ./<virtual_env_name>/bin/python scapy_ping.py

"""
