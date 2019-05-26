fruit = { "orange" : "a sweet,orange ,citrus frut",
          "apple" : "good for making cider",
          "lemon" : "a sour, yellow citrus fruit",
          "grape" : "a small, sweet fruit growing in bunches",
          "lime" : "a sour,green citrus fruit"
}

print(fruit)

print("*"*40)
veg = {"cabbage" : "every child's favourite",
       "sprouts" : "mmmm,lovely",
       "spinach" : "can I have some more fruit,please"}
print(veg)

print("*"*40)

#veg.update(fruit) #adding fruit dictionary to veg dictionary

print(veg)
print("*"*40)
print("*"*40)
#print(fruit.update(veg)) #gives None therefore update returns nothing
print(fruit) #fruit is updated
# adding veg to fruit .........
# print("*"*40)
# fruit.update(veg)
# print(fruit)
print("*"*40)
nice_and_nasty = fruit.copy() # a new dictionary created from fruit
nice_and_nasty.update(veg) #whhile making line 23 and 18 comment
#so veg and fruit are same they were.......
print(nice_and_nasty)
print("\n\n")
print(fruit)
print("\n\n")
print(veg)