bike = {"make" : "Honda",
        "model" : "250 dream",
        "color" : "red",
        "engine_size" : 250}
print(bike)

print("-"*40)
print(bike["engine_size"])
print(bike["color"])

#keys must be immutable
#therefore we can't use lists as keys
#but we can use tuples
 #see DS1