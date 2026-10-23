#type_check.py
#value_1, value_2, value_3, value_4, value_5 = 8080, "8080", 99.5, "198.51.100.7", 1_000
#at first i wrote this but then realised that i dont need variables , but i will keep it as a comment anyway :)
#ok so this will for sure be an intiger
print(type(8080))
#this will be a string because we have a double quotation
print(type("8080"))
#this will be a float because of the half
print(type(99.5))
#this is a string , because we have to put a double quotation , without it it would give us an error because no number in math has more than one comma
print(type("198.51.100.7"))
#this will be an intiger , because the code doesnt read the underscore , its just there so its easier for us (humans) to read it
print(type(1_000))
print(int("443"), type(int("443")))
print(str(8080), type(str(8080)))
#2.5 is already a float , so i dont really get the point of this but sure , why not
print(float(2.5), type(float(2.5)))