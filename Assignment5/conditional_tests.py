#conditional_test.py
user = "analyst"
role = "viewer"
failed = 3
port = 22
print("is user != \"analyst\" ? i predict false")
print(user != "analyst")
print("\nis port >= 0 ? i predict true")
print(port >= 0)
print("\nis failed < port ? i predict true")
print(failed < port)
print("\nis role == \"Viewer\" ? i predict false")
print(role == "Viewer")
print("\nis port > 3 and failed < 22 ? i predict true")
print(port > 3 and failed < 22)
print("\nis role == \"analyst\" or not failed != -2 ? i predict false")
print(role == "analyst" or not failed != -2)
print("\nis not user == \"analyst\" and True ? i predict false")
print(not user == "analyst" and True)
print("\nis not port != 22 or failed == 3 and user == \"analyst\" ? i predict true")
print(not port != 22 or failed == 3 and user == "analyst")
print("\nis 0 < port < 255 and port != 22 ? i predict false")
print(0 < port < 255 and port !=22)
# :D
print("\nis not user != \"analyst\" and role == \"viewer\" and failed < 5 and failed > 0 and port >= 1 and port <= 25556 and user != role and failed != port and not 2 == 3 or False ? i predict true :D")
print(not user != "analyst" and role == "viewer" and failed < 5 and failed > 0 and port >= 1 and port <= 25556 and user != role and failed != port and not 2 == 3 or False)