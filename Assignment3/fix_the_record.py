# fix_the_record.py
# This program prints a short record about a network device.
#i couldn't find the original code so i just copied the code from the slides

device_name = "edge-router"
#first error : this line was a syntax error , because we cant start a variable name with a number
second_ip = "192.0.2.1"
#second error : another syntax error , this time its because the word "class" is taken by python and we cant use it as the name of a variable
kind = "router"
#third error : value error (runtime error) , its because we cant turn letters/text into an intiger
port = int("22")
#fourth error : runtime error , because "device_nam" is not a variable (because its a mis-spell)
print("Device:", device_name)
#(with error 1) : chaged this to work with (second_ip)
print("Backup IP:", second_ip)
#(with error 2) : changed this to work with (kind)
print("Type:", kind)
print("Port:", port)