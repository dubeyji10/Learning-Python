list1=[]
list2=list()
print("\n list 1 : {}".format(list1))
print("\n list 2 : {}".format(list2))

if list1 == list2:
    print("\n lists are equal ")


# adding value to list
# list2.append(7)
# print(list2)
# ------
# print is a fucntion and what's passed inside is an argument

#passsing a string into list

print(list("The lists are equal"))

#every character is passed into the list
print("\n\n\n\n\n")


even = [2,4,6,8]
another_even = even
print(another_even is even)
# True because they both point to same list

another_even.sort(reverse=True)
print(even) # it also updated the list even
# -- it is also reversed
print("\n\n see source ")
another_even2 = list(even) #here
#list constructor
# is used and even list is passed which returns a new list
print(another_even2 is even) #gives false
# because they are different lists

print(another_even2 == even) #gives true
# because contents of lists are equal
print("\n\n-------------\n\n")
even2=[2,4,6,8]
another_even3 = sorted(even,reverse=True)
print(another_even3 == even2) #gives False
#because sorted into different order
print(another_even3 is even2) # gives False
#because they are pointing to different lists