
# remove comment tags and see output

#simple example of loop :

for i in range(1,20):
    print(" i = {}".format(i))

#or
#
for i in range(1,10):
    print(" i = %4d "%(i))
#

#len couts number of characters in string
# number [0] =9
number = " 9,223,372,036,854,775,807"

for i in range(0,len(number)):
    print(number[i])

# more examples :
#here we extract numbers from the string
# which was comma seperated

for i in range(0,len(number)):
      if number[i] in '0123456789':
         print(number[i])

         ### -------------  ###
# to print it in one line seperated by a space

print("\n\n original string is {}".format(number))
for i in range(0,len(number)):
    if number[i] in '0123456789':
         print(number[i],end=' ')


cleanedNumber = ''
# to print it without space and also store it as a new number
for i in range(0,len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]


newNumber = int(cleanedNumber)
print(" \n\nthe number is = {}".format(newNumber))
