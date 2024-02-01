#indexoperator = [] virker på bl.a. str, list, tuples

name = "nicolai Finstad Larsen!"

if(name[0].islower()):
    name = name.capitalize()

first_name = name[:7]
last_name = name[8:]
last_char = name[-1]

print(name)
print(first_name.upper())
print(last_name.lower())
print(last_char)
    

