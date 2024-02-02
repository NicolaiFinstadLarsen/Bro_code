#str.format()       gir mer kontroll for output

# animal = "cow" #trenger ikke disse på siste print
# item = "moon" #trenger ikke disse på siste print

# print("The "+animal+" jumped over the "+item) ikke pent og vanskelig å lese

# print("The {} jumped over the {}".format("cow", "moon"))
# print("The {} jumped over the {}".format(animal, item))
# print("The {0} jumped over the {1}".format(animal, item))
# print("The {animal} jumped the {animal} over the {item}".format(animal="cow", item="moon"))

# text = "The {} jumped over the {}"
# print(text.format(animal, item))

# ===================================================

# name = "Nico"

# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}. Nice to meet you".format(name))
# print("Hello, my name is {:>10}. Nice to meet you".format(name)) #right align
# print("Hello, my name is {:^10}. Nice to meet you".format(name)) #center
# print("Hello, my name is {last_name:^10}. Nice to meet you".format(last_name = "Finstad", name="Nico"))

# ===================================================

number = 3.14159
number2 = 1000

print("The number pi is {:.2f}".format(number)) #viser bare de 2 første float og rounder av
print("The number 1000 is {:,}".format(number2)) #legger til tusentallskille
print("The number 1000 is {:b} in binary".format(number2)) #binary
print("The number 1000 is {:o} in octal".format(number2)) #octal
print("The number 1000 is {:x} in hex lowercase".format(number2)) #hex, endre x til stor for capital
print("The number 1000 is {:E} standardform capital".format(number2)) #standardform, også stor eller liten









