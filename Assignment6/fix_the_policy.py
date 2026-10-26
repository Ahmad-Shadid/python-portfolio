# fix_the_policy.py
# Check a new password against an example policy and classify its length.
MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")
#syntax error , we didnt put the colon in the end
if len(password) < MIN_LENGTH:
    print("- Too short.")
#semantic error , it should be a seperate check
if password == username:
    print("- Same as the username.")

#semantic error , it should also happen if its less than 16 , if its more then the first thing will always happen and the elif wont ever happen
if len(password) >= MIN_LENGTH and len(password) < 16:
    strength = "acceptable"
elif len(password) >= 16:
    strength = "long"
else:
    strength = "short"
#semantic error , this line should work regardless of how long the password is , so it should be outside the if function
print(f"Length: {len(password)} ({strength})")