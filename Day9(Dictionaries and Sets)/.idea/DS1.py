#Dictionaries
#are unordered
#contain key valued pairs
#values are not accessed by an index but by means of a key

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour,yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunhces",
         "lime": "a sour,green citrus fruit"
         }
print(fruit)
print("-"*20)
print("lemon --------",fruit["lemon"]) # using key which is seperated by a colon

print("-"*40)
#     new key
fruit["pear"] = "an odd shaped apple"

print(fruit) #pear is added to the dictionary

print("-"*40)
fruit["lime"] = " great with tequila"
print(fruit) #lime is updated -----------------------

print("-"*40,"\n lemon is deleted from dictionary ")
del fruit["lemon"]
print(fruit)
# print("-"*40,"\n deleting the whole dictionary")
# del fruit
# print(fruit) # gives error

print("-"*40)


# fruit.clear() #contents of fruit deleted
# print(fruit)
#

print(fruit["tomato"]) #key error since tomato is not in the dictionary
print("-"*40)
