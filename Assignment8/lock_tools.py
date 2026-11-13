# lock_tools.py

def is_locked(failed, max_tries=3):
    """Returns True if failed attempts reach or exceed the maximum."""
    if failed >= max_tries:
        return True
    else:
        return False


def tries_left(failed, max_tries=3):
    """Returns 0 if locked, otherwise the number of remaining tries."""
    if is_locked(failed, max_tries):
        return 0
    else:
        return max_tries - failed


def status(failed):
    """Returns the account status and remaining tries, if applicable."""
    if tries_left(failed) == 0:
        return "locked"
    else:
        return f"active ({tries_left(failed)} tries left)"


print(is_locked(2))
print(is_locked(3))
print(is_locked(3, 5))
print(tries_left(1))
print(tries_left(7))
print(status(1))
print(status(4))