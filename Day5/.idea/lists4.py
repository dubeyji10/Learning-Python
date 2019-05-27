even = [2,4,6,8]
another_even = list(even)
print(another_even == even )
# checks if the contents are identical
print("\n---------------------\n")

another_even2 = sorted(even,reverse= True )
print(another_even2 == even)
#false cause we sorted it into a different order

print(another_even2 is even) #false
# because they are different lists

print("\n ----- even list is : ",even ," ---still the same\n\n")

odd = [1,3,5,7,9]

numbers = [even,odd]

print(numbers,"\n--------------\n")
# this gives a list containing two lists
# now ----------  #
for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)

