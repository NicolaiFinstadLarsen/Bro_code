import random

x = random.randint(1, 6) #begge sider er inkludert
y = random.random() #random float mellom 0 og 1



my_list = ["rock", "paper", "scissors"]

z = random.choice(my_list)



suits = ["Heart", "Clubs", "Spades", "Diamonds"]
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

random.shuffle(cards)
random.shuffle(suits)


print(x)
print(y)
print(z)
print(suits[1],cards[1]) #velger kortet på index 1
