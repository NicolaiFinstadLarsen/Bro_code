# *args, kan kalles noe annet, men standard er args

def add(*args): #args tar da alle argumenter du kjører i funksjonen i linje 11
    result = 0 #vi må ha en startverdi
    args = list(args) #vi typecaster til en liste hvis vi vil endre en av verdiene 
    args[0] = 0 #vi endrer indeks 0 til verdien 0
    for i in args:
        result += i
    return result

print(add(1,2,3,4,5,6,7))