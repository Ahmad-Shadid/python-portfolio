#truth_research.py
#all the information was gathered from "https://docs.python.org/3/builtins/stdtypes.html"
#this will turn out False , because if we have nothing in quotation mark then its counted as false
print(bool(""))
#true , because its just a string that is not empty
print(bool("0"))
#false , 0 is counted as false in python by defult
print(bool(0))
#false , it doesnt matter if its 0 or 0.0 (int or float) , what matters is that its just 0
print(bool(0.0))
#true , because its a string , doesnt matter what is inside it
print(bool("False"))