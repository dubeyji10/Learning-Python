even =set(range(0,40,2))
print(even)
square_tuple = (4,6,16)
squares = set(square_tuple)
print(squares)
print("--"*30)
if squares.issubset(even):
    print(" squares is a subset of even ")
if even.issuperset(squares):
    print(" even is a superset of squares ")
print("--"*30)    