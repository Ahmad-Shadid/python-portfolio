#device_card.py
#this program shows connection information of a website
MAX_CONNECTIONS = 50
#i named it "web_server_01" because i didnt find a better name
device_name = "web_server_01"
device_ip = "192.0.2.17"
service = "HTTPS"
open_port = 74
print("Device name :", device_name)
print("IP address:", device_ip)
print("Service", service)
print("Port :", open_port)
print("Max connections :", MAX_CONNECTIONS)
service, open_port = "SSH", 92
print("Updated service :", service, "on port", open_port)