utensils = {"fork", "spoon", "knife", "knife", "knife"} #bare unike verdier

utensils.add("Napkin")
utensils.remove("fork")
# utensils.clear()




# for x in utensils:
#     print(x)

dishes = {"bowl", "plate", "cup", "knife"}
# utensils.update(dishes) #legger til dishes i utensils

# print(utensils)

dinnertable = utensils.union(dishes)

# print(dinnertable)

# print(utensils.difference(dishes))
# print(utensils.intersection(dishes)) #hva som er likt.