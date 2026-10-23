#port_facts.py
# RFC 9293: TCP specification.
# RFC 791: IPv4 specification.
PORT_BITS = 16
IPV4_BITS = 32
possible_ports = 2 ** PORT_BITS
highest_port = 2 ** PORT_BITS - 1
possible_ipv4_addresses = 2 ** IPV4_BITS
print(f"Possible port numbers: {possible_ports}")
print(f"Highest port number: {highest_port}")
print(f"Possible IPv4 addresses: {possible_ipv4_addresses}")