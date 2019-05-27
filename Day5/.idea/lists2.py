list1 = []
list2 = list() #constructor ?
print(" List 1 : {}".format(list1))
print(" List 2 : {}".format(list2))

if list1 == list2 :
    print(" lists are equal")


#passsing a string to the list
#creates a list with each character
print(list(" the lists are equal ")) # see the output

print(" \n------ reversing a list ------\n")
even = [2,4,6,8]
even2 = even
even2.sort(reverse=True)
print("\noriginal list of even is also sorted : ",even,"\n--")
print(even2)


print("even variable was also updated \n"
      "--------------------\n--------------------\n"
      "--------------------")

another_even = even
print(another_even is even) #this returns true
another_even.sort(reverse=True)
print(even)
# another_even2 = list(even) # a constructor and
# # passing list even to it which returns a new list
# print( "\n !!!! see source !!!!")
# print(another_even2 is even) # this returns false
# another_even2.sort(reverse=True)
# #make the required --- excep for declaration of even
# # above code comment and see
# print(even) # false -- line 33 so
#  # ' even ' list (original) is not reversed