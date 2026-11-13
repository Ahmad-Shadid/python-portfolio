# fix_the_functions.py

def print_header():
   """Display the report header."""
   print("=" * 30)
   print("LOGIN REPORT")
   print("=" * 30)

#runtime error, using the function should be after we define it, not before
print_header()

#semantic error, how do i even explain what was happening here... well there is not total, we just need to return the value, and ELSE return 0, not whatever that was
def lock_minutes(failed, minutes=15):
   """Return failed * minutes if failed >= 3, else 0."""
   if failed >= 3:
        return failed * minutes
   else:
        return 0


def login_line(username, failed):
   """Return one line of the report."""
   minutes = lock_minutes(failed)
   return f"{username}: {failed} failed, locked {minutes} min"

#runtime error, the funtion has username , not user
print(login_line(username="sara", failed=4))
#semantic error , we need to print the output
print(login_line("omar", 1))