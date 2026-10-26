#risk_score.py
score = 0
failed = int(input("Failed attempts in the last hour : "))
hour = int(input("Login hour (0-23) : "))
device = input("New device ? (yes / no) : ")
if failed >= 3:
    score = score + 40
if hour < 6:
    score = score + 30
if device == "yes":
    score = score + 30
if score >= 70:
    risk = "HIGH"
elif score >= 30:
    risk = "MEDIUM"
else:
    risk = "LOW"
print(f"Risk score : {score} ({risk})")
#on a side note , this way probably the most fun assignment so far , i hope it only gets better !