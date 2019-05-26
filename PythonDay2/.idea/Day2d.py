parrot = "I Am a bird"
print(parrot)
print(parrot[3]) # prints m -- 3rd character

#print(parrot[23])  #gives error -- index out of range
print(parrot[-1]) #last character -- 1st from last
print(parrot[-6]) #6th character from last
print(parrot[0:6]) # 0 to 6th character including 6th character from 0 to 6th index !
print(parrot[:6])# automatically starts from beginning of string

parrot1="Norwegian Blue"
print(parrot1[6:]) # from index 6 to last not including 6th

print(parrot1[-4:-2])

print(parrot1[0:6:2]) # start form 0 extract all characters up to
# but including index position 6 in steps of two --

# should give Nre Norweg
#                0123456
#                0-N inlcuded
#                and 2nd characters skip to 2nd character  every time
#                6-e excluded
#
print(parrot1[0:6:1])
# this should give Norweg because skip is 1 same as [0:6] so no skip
# Norweg
print(parrot1[0:6:3])
#this should give Nw ......... correct
number = "9,223,372,036,854,775,807 "
print(number[1::4]) # only commans because middle position is empty
# which implies till end of string and skip to every 4 th character which is a comma
numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3]) # space and comma ignored or skipped
# just a way to extract information
string1 = " abhishek "
string2 = "dubey"
print(string1+string2)
print()
print(" \n ")
print(" i  " " am " +string1 + string2)
print()
print(" \n ")
print("hello")
print()
print(" \n ")
print("hello "*5)
#print("hello "*5+4) # gives error
print(" hello "*(5+4)) # if i remove '#'
# before print in 48 this line will
# not print since python runs on an interpreter system there is an error in 48 -- int,str
today = "friday"
print("day" in today) # Gives True in operator to check if the string is a substring or not
print("kkk" in today) # Gives False
print()
print(" \n ")
#      str1 in str 2
print("hello " in " hello abhishek") # true
print(" hello " in " abhishek ") # false