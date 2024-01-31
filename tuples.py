student = ("Nico",21,"male")

print(student.count("Nico")) #hvor mange av en verdi
print(student.index("male")) #hvilken indeks verdien er på

for x in student:
    print(x) #printer alle verdier
    
if "Nico" in student:
    print("Ja!") #Sjekker om verdien er i tuple