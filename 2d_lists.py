drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream", "gellato"]

food = [drinks, dinner, dessert]

#Her veleg vi 1 hvilken liste og 2 hvilken indeks i listen.
print(food[0][1])


#Her kan vi lage et forslag til servering ved input fra bruker.
print("Choose 0-2 x 3 for drinks, dinner, dessert")
service = [drinks[int(input("Drinks (0-2): "))], 
        dinner[int(input("Dinner (0-2): "))], 
        dessert[int(input("Dessert (0-2): "))]]

print(service)