#fix_the_rules.py
# This program checks a connection against three rules.
role = input("Role: ")
#runtime error , we need it to be an int
port = int(input("Port: "))
#semantic error
is_admin = role == "admin"
#syntax error , it should be <= not =<
is_system_port = port <= 1023
#semantic error
is_web_port = port == 80 or port == 443
print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")