#iterator
# ---- it is an object that represents a stream of a data
# it returns the stream or the actual data in the stream (one element at a time)
#an object that supports iteration is called itertion

# two iterable objects we've seen already so far --- strings and lists

string = "1234567890"

# for char in string:
#     print(char,end=" ")

#for terminates when error? generates
# ( error here is something when end of iterable object occurs
# it is not visible but that's what terminates the loop)

# for vs iter()


my_iterator = iter(string)
print(my_iterator)

#the iterable object
#iterating one element at a time
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# now if we add it will give error because there weren't any element

print(next(my_iterator))


for char in string:
    print(char)
print("\n\n\n")
for char in iter(string):
    print(char)