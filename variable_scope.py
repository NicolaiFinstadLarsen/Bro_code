#scope of variable er hvor den er tilgjengelig. 
#eks en variabel inne i en funksjon er bare tilgjengelig i den funksjonen

name = "Nico3" #global. denne printes etter den lokale variabelen med samme navn.
name2 = "Nico2"

def the_name():
    name="Nico" #lokal
    print(name)
    print(name2) #tilgjengelig
    
the_name()

print(name) #ikke tilgjengelig, kun den variabelen som er utenfor func
print(name2) #tilgjengelig