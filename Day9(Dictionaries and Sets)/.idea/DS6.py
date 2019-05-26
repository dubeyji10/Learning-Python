list1 = ["a","b","c","d"]
string1 = ''
for i in list1:
    string1 += i + ","
print(string1)

#strings are immutable
#augmented assignment like on line 4 is not going to help
#we will need join

print("-"*40)
#correct way to do it is :
 # "string".join() ------ string.join()

string2 = ",".join(list1)
print(string2) #trailing comma is not here

#we can do that with strings too
print("-"*40)
letter = "abcdefghijklmnopqrstuvwxyz"

string3 = ",".join(letter)
print(string3)
print("-"*40)
#more examples :
numbers = "123457789"
string4 = " mississippi ".join(numbers)
print(string4)