# fix_the_session.py
# This program reports a user's session time.

username = input("Username: ")
total_seconds = int(input("Session length in seconds: "))
#first its a runtime error , we need the input to be an intiger , not a string
#then its a semantic error , we need it to be 2 slashes instead of one to get an intiger with decemels and not a float
minutes = total_seconds // 60
seconds = total_seconds % 60

print("=" * 30)
#semantic error , we want the value of the username , not just {username} , so we use an f string
print(f"User: {username}")
#runtime error , we cant add an intiger to a string , so we make it all a string
print("Session: " + str(minutes) + " min " + str(seconds) + " s")
print("=" * 30)