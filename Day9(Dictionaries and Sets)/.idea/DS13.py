#sets

farm_animals = {"sheep","cow","hen"}  #creatin set way1
# ------- no key that's how python knows it's not a dictionary
print(farm_animals)


for animals in farm_animals:
    print(animals)

print("*"*40)

wild_animals = set({"lion","tiger","panther","elephant"})
#set function used .......
#comment lines from 17 to 25 and run ------ and see outputs
#using a literal -----
empty_set = set()
empty_set2 = {} #------------------------
empty_set.add("a")
empty_set2.add("a") #add is not a method for empty_set2
# -- line 18 creates a dictionary -------not a set
print(wild_animals)

for animal in wild_animals:
    print(animal)

farm_animals.add("hores")
wild_animals.add("horse")
# sets are unordered ------------------------
print(farm_animals)
print("-----------------------------------")
print(wild_animals)