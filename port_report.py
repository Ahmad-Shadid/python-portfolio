#port_report.py
start_port = int(input("Start port: "))
end_port = int(input("End port: "))
print(f"Start port: {start_port}")
print(f"End port: {end_port}")
checked = end_port - start_port + 1

for port in range(start_port, end_port + 1):
    if 0 <= port <= 1023:
        type = "system"
    elif 1024 <= port <= 49151:
        type = "user"
    elif 49151 < port <= 65535:
        type = "dynamic"
    print(f"{port}: {type}")
print(f"Ports checked: {checked}")