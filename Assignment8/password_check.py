#password_check.py

def long_enough(password, minimum=8):
    if len(password) >= minimum:
        return True
    else:
        return False


def differs_from_username(password, username):
    if password == username:
        return False
    else:
        return True


def password_ok(password, username):
    if long_enough(password) and differs_from_username(password, username):
        return True
    else:
        return False


username = input("Username: ")
password = input("Password: ")

if password_ok(password, username):
    print("Password accepted.")
else:
    print("Password rejected.")
