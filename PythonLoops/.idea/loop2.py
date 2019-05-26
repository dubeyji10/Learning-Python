number = " 9,223,372,036,854,775,807"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print(" new number is {}".format(newNumber))

for state in [" not pinin'","no more","a stiff","bereft of lift"]:
     print(" this parrot is "+state)
     #or
print("\n\n")
for state in [" not pinin'","no more","a stiff","bereft of lift"]:
     print(" This parrot is {}".format(state))

# skip of 5
for i in range(0,100,5):
     print(" i is {}".format(i))


