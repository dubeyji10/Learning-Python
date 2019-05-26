#undo next 3 lines

# greeting="HELLO"
# name=input("Enter you name ")
# print(greeting+' '+name)

#backslash gives a special meaning
#splitString
#and tabString show

# to put something in a comment select that part and use ctrl+/ button to make it a
# comment and undo it

splitString = " This string has been \nsplit over \nseveral\ntimes\nas\nyou can \nsee"
print(splitString)

tabString = " t1 \t t2\tt3\t\kt12312\t3\t\t213123213"
print(tabString)

print(' the pet shop owner said "NO NO ,no \'e \'s uhh........ he\s resting"  ')
#see difference in use of quotes single and double

print(" the pet shop owner said \"No No , no , 'e 's uhh.... he's resting\"")

anotherSplitString = """The string has been 
split over
several line .. using triple quotes"""

print(anotherSplitString)
print(''' the pet shop owner said  " NO , no , 'e 's  uh .. , he's resting " ''')

#now take care with 4 double quotes remove space  ......here b/w quotes one and triple
print("""the pet shop owner said "no , no , 'e 's uh.... , he's resting" """)
# and it will give error