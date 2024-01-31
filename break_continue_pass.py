while True:
    name = input("Your name? ")
    if name != "":
        break

phone_nu = "123-456-789-0"

for i in phone_nu:
    if i == "-":
        continue
    print(i, end="")
print()

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i, end=",")
        
    