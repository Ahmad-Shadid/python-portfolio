#pin_space_table.py
GUESS_PER_SECOND = 10

for digit in range(4, 9):
    possible = 10 ** digit
    time_seconds = possible // GUESS_PER_SECOND
    time_minutes = time_seconds // 60
    time_days = time_minutes // (60 * 24)
    print(f"{digit} digits: {possible} PINS, {time_minutes} minutes, {time_days} days")
"""not sure if i am missing something but why is this one so much easier than the other 3 ? it took my 5 minutes and worked first try ...
well maybe i did something wrong or unintended , but not much i can do now"""