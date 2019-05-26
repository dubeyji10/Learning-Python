fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour,yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunhces",
         "lime": "a sour,green citrus fruit"
         }

print(fruit)
print("-"*40)

#producing a tuple

fruit_tuple = tuple(fruit.items())
print(fruit_tuple)

print("-"*40)

for snack in fruit_tuple:
    item,description = snack
    print(item+" is "+description)
print("-"*40)
#passing tuple into the dict function it creates another dictionary
print(dict(fruit_tuple))