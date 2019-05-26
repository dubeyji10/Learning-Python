fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour,yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunhces",
         "lime": "a sour,green citrus fruit"
         }

print(fruit)
print("-"*40)

#ordered_keys = list(fruit.keys())
#ordered_keys.sort()

#or
ordered_keys=sorted(list(fruit.keys()))
for f in ordered_keys:
    print(f," - ",fruit[f])
print("-"*40)

for f in sorted(fruit.keys()):
    print(f," - ",fruit[f])


print("-"*40)

print(fruit.keys())
print(fruit.values())


print("-"*40,"\n")


fruit_keys = fruit.keys()
print(fruit_keys)
fruit["tomato"] = "not nice with ice cream"
print(fruit_keys) # keys updated ------
print("\n \n","-"*50)

print(fruit)
print("-"*50)
print(fruit.items())

