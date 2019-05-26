_author_ = "dubeyji"

name = input(" please enter your name ")
# aliter : age = input(" how old are you %s "%name)
#age = input(" how old are you {} ?".format(name))

#print("{0} , {1} ".format(age,name))  #remember put a . not a comma after "
#this will give error ---- age is str
#if age>= 18 :
 #   print(" {} are old enough to vote ".format(name))

 #so we will change the inpput to int
 # again input for age but this time as integer
print("\n\n")
age2 = int(input(" how old are you {} ? ".format(name)))
if age2>= 18 :
  print(" {} is old enough to vote ".format(name))
else :
     print("you can't vote now \n please come back in {0} years".format(18-age2))

