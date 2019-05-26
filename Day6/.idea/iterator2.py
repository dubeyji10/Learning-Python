
# more on iterable and iteration


string = "1234567890"


for char in string:
    print(char,end=' ')
print("\n-------------------")
for char in iter(string):
    print(char,end=' ')
