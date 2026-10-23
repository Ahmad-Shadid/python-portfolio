#login_report.py
MAX_LOGIN_ATTEMPTS = 5
name = input("What is the username ? :")
failed = int(input("How many failed attempts ? :"))
print("=" * 30)
print ("         LOGIN REPORT")
print("=" * 30)
attempts = MAX_LOGIN_ATTEMPTS - failed
print(f"Username :\t\t{name} ")
print(f"failed attempts :\t{failed}")
print(f"Attempts left :\t {attempts}")