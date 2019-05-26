fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour,yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunhces",
         "lime": "a sour,green citrus fruit"
         }

print(fruit)
print("-"*40)
#remove comment and run
# while True:
#     dict_key = input(" Please enter a fruit : ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key,"We don't have a "+dict_key)
#
#     print(description)
#

for snack in fruit:  #key is hashed ?
    print(fruit[snack]) #order isn't same ....  hashing ?


print("-"*40)

for i in range(10):
    for snack in fruit:
        print(snack+" is "+fruit[snack])
    print("-"*40)
