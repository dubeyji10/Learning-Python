
even_set = set(range(0,40,2))
print(even_set) #* unordered
print(len(even_set))
print("--"*30)
squares_tupple = (4,6,9,16,25)
squares = set(squares_tupple)
print(squares)
print(len(squares))
print("--"*30)

print(" symmeteric even - squares")
print(sorted(even_set.symmetric_difference(squares)))

print("\nsymmeteric square - even")
print(sorted(squares.symmetric_difference(even_set)))
print("--"*30)

print("they are identical")
print("--"*30)

#discard
print(squares)
print("\n removing 4 ---- ")
squares.discard(4)
print(squares)
squares.remove(16)
print(squares)
squares.discard(8) #does nothing because 8 is not in the set
#but remove   will give an error
#square.remove(8) #error
#so we will fix that
try :
    squares.remove(8)
except KeyError:
    print(" 8 is not a member of set")