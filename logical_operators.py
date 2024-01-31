#Python Full Course for free
#https://www.youtube.com/watch?v=XKHEtdqhLK8&list=PL5eZmf4ZIS9QAVRP3KeYS6mMFkragcU1S&index=3&t=3521s


#video timestamp: 58:19
#logical operators and/or/not

temp = int(input("Hvor varmt er det? "))

if temp >=0 and temp <= 30:
    print("Det er en fin dag, ikke for varmt. Temp: " +str(temp) +" grader :)")
    print("Gå ut")
    
elif temp > -9 or temp > 30:
    print("Det er ikke fint ute nå")
    print("Greit å bli inne")
    
elif not(temp < -10):
    print("Det er ikke -10 grader")
    
   
