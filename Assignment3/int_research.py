#int_research.py
#this is a small research i did about the intiger function in python
#all the information was gathered from the website https://docs.python.org/3/builtins/functions.html#int
#this line of code will work , from what i saw the intiger function doesnt care about spaces before or after the number
print(int(" 22 "))
#this also works because we are just telling it that there is a number , and its positive
print(int("+22"))
#when python reads that in the intiger there are zeros before the number ... it just deletes them , so yeah it works
print(int("0022"))
#the underscore here is the same as in things like 1_000_000 , so once again the code ignores it and its just for us to see
print(int("2_2"))
#so in the end all of these were the same output , wow