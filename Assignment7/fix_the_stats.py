# fix_the_stats.py
# Count failed logins and the average session length.
events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]

#semantic error, the filed variable should be outside the loop , else every time the loop loops , failed gets set to 0 agian
failed = 0
for event in events:
    if event == "FAILED":
        failed += 1
print(f"Failed logins: {failed}")

total = 0
count = 0
for value in minutes:
    if value > 0:
        total += value
        count += 1
#semantic error, we want this to happen only once in the end , not everytime the loop happens , so we just move it out of the loop
#semantic error, we still need the left overs ... i guess ? this is the one i am not too sure about
print(f"Average session: {total / count} minutes")

#semantic error, range(1, 4) are number for 1 to 4 EXCLUDING the latter , so its 1 , 2 , 3. we need it to include the 4 so we make it range(1, 5)
for level in range(1, 5):
    print(f"Level {level}")