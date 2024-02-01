capitals = {"Norge" : "oslo",
            "India" : "New Dehli",
            "China" : "Bejing",
            "USA" : "Washington DC"}

capitals.update({"Germany" : "Berlin"})
capitals.update({"USA" : "Las Vegas"})
capitals.pop("China")

# print(capitals.get("Germany"))
# print(capitals.get("USA"))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key, value in capitals.items():
    print(key, value)


