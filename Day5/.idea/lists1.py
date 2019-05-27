# ipAddress = input(" Enter an IP address ")
# print("no of segments = {}".format((ipAddress.count(".")+1)))

#using list.count("_____________")

print("\n\n")
parrot_list = ["non pinin'","a stiff","bereft of live"]
for state in parrot_list:
    print(" this parrot is "+state)

parrot_list.append(" A Norwegian blue ")
print("\n ")
for state in parrot_list:
    print(" this parrot is "+state)

even = [2,4,6,8,10]
odd = [1,3,5,7,9]
numbers = even + odd
print(numbers)
print(" ------ comparing with sorted list ---- see source and difference\n")
numbers2=sorted(numbers)
if numbers == numbers2:
    print(" lists are equal ")
else :
    print(" the lists are not equal ")

if numbers2 == sorted(numbers):
    print(" the lists are equal ")
else:
    print(" the lists are not equal ")

print("\n ------------------\nsorting numbers :\n ")
numbers.sort()
# doesn't returns sorted list
# so print(numbers.sort()) won't work -- gives none
# sort works on object .. on existing variable
print(numbers)



numbers3 = even + odd
print(" \n -----------\n numbers 3 ---- : ",numbers3)

print(" \nnow returning a sorted list \n")
print(sorted(numbers3))

