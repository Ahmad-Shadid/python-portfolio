#login_decision.py
#i dont fully understand step 3 to be honest , what do you mean "check in this order : locked ...." , what even is locked ? i dont get it
#so i will just assume that i need to make a new boolean variable named locked then move on
MAX_FAILED = 5
KNOWN_USER = "analyst"
STORED_PASSWORD = "Blue#Falcon72"
user_name = input("User name : ")
failed = int(input("failed attempts so far : "))
password = input("Password : ")
locked = failed >= MAX_FAILED
attempts = MAX_FAILED - failed - 1
if locked:
    print("account locked")
elif user_name == "analyst":
    if password == "Blue#Falcon72":
        print("access granted")
    else:
        print(f"access denied , attempt left : {attempts}")
else:
    print("unknown user")