#session_timer.py
#this code calculates the sessions time , minutes and seconds
overall_time = int(input("How long has the session been going on for (in seconds) ? :"))
minutes = overall_time // 60
seconds = overall_time % 60
print(f"The session took {minutes} minutes and {seconds} seconds in total")
#when we input 905 we get "The session took 15 minutes and 5 seconds in total"
#when we input 60 we get "The session took 1 minutes and 0 seconds in total"
#when we input 59 we get "The session took 0 minutes and 59 seconds in total"