food = ["pizza", "hamburger", "hotdog", "spaghetti"]

print(food)
print(food[0])
print(food[:2])
print(food[2:])

food[0] = "sushi"
print(food[0])

for x in food:
    print(x)
print()

food.append("ice cream")
food.remove("hotdog")

for x in food:
    print(x)
print()

food.pop()
food.insert(0,"cake")

for x in food:
    print(x)
print()

food.clear()

for x in food:
    print(x)