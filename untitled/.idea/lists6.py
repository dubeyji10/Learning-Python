even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = [even,odd]
print(numbers)

#Q - what is the output :

#A -  a list containing two lists
# [[2,4,6,8],[1,3,5,7,9]]
print("\n\n-----------\n\n")
for numbers_set in numbers:
    print(numbers_set)


print("\n--------------\n")

for i in numbers:
    print(i) #print the even list first then odd

    for value in i:
        print(value) #first the even numbers and then the odd

# [2,4,6,8]
# 2
# 4
# 6
# 8
# [1,3,5,7,9]
# 1
# 3
# 5
# 7
# 9