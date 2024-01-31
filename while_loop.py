#video timestamp  1:04:04
#while loop

x = 0
while x <= 5:
    print(x)
    x += 1
    
name = ""
while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " +name)

new_name = None
while not new_name:
    new_name = input("Enter your name 2: ")
    
print("Hello " +new_name)
