#pin_tries.py
MAX_TRIES = 3
CORRECT_PIN = 2580
tries = 0
while tries < MAX_TRIES:
    pin = int(input("PIN: "))
    if pin == CORRECT_PIN:
        print("Access granted.")
        break
    else:
        tries += 1
        tries_left = MAX_TRIES - tries
        print(f"Wrong PIN. Tries left: {tries_left}")
        if tries_left == 0:
            print("Card blocked.")
            break