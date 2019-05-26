#more on sets


even_set = set(range(0,40,2))
print(even_set) #* unordered
print(len(even_set))
print("--"*30)
squares_tupple = (4,6,9,16,25)
squares = set(squares_tupple)
print(squares)
print(len(squares))
print("--"*30)
#union of sets
#mathematical union  ------- one item on time
print(even_set.union(squares))

#intersection of sets
print("--"*30)
print(even_set.intersection(squares))
print("--"*30)
#since sets are unordered ------ sorting -------
print(sorted(even_set))
print("--"*30)
print(" even minus square : ",even_set.difference(squares))
print(sorted(even_set - squares)) # also works// '-' sign
print("--"*30)
print("sqaures minus even :",squares.difference(even_set))
print(squares-even_set)