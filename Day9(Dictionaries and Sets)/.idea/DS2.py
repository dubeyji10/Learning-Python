fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour,yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunhces",
         "lime": "a sour,green citrus fruit"
         }

print(fruit)
while True:
    dict_key = input(" Please enter a fruit : ")
    if dict_key == "quit":
        break
    #
    #fruit.has_key(dict_key) #has_key is a python2 method
    # and is deprecated
    # it is equivalent to
    # if dict_key in fruit :
    #
    if dict_key in fruit:
        description = fruit.get(dict_key) # a new fucntion we just learnt
        print(description) # it returns none if key doesn't exists
    else:
        print("we don't have a "+dict_key)

# aliter :


# while True:
#     dict_key = input(" Please enter a fruit : ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key,"We don't have a "+dict_key)
#
#     print(description)
#