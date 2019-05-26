_author_ = 'dubey'
age = 21
# print(" My age is " + age + " years ") #this gives error make it comment undo to see error
print(" My age is "+ str(age) + " years ")
print(" My age is {0} years ".format(age))

# this will make it clear
print(" There are {0} days in {1} , {2} , {3} , {4} , {5} , {6} and {7} ".
      format(31,"January","March","May","July","August","October","December"))
print("""\n days in\njan - {2}
 feb - {0}
 mar - {2}
 apr - {1}
 may - {2}
 jun - {1}\njuly - {2}\n aug - {2}
sep - {1}\n oct - {2}\n nov - {1}\n dec - {2}""".format(28,30,31))

print(" My age is %d years " % age)


#--------------- number string ,  string number
print(" My age is %d %s,name is %s roll number %d"%(age,"years","abhishek",2))
print("\n ")
#looping
 #           -------------------------------------   i**2 is i*i or i^2
 #        -----------------------------------------  i **3 is i*i*i or i^3
for i in range(1,12):
    print(" No. %2d squared is %4d and cubed is %4d "%(i,i ** 2,i ** 3))
# here %nd gives n number of spaces b/w characters

print(" Pi is approximately ---- %f"%(22/7))
print(" Pi is approximately ---- %12f"%(22/7)) #n>9 ...... doesn't works well
print(" Pi is approximately ---- %.50f"%(22/7)) #upto 50 decimal places
print()
for i in range(1,12):
    print(" No {0:2} sqaured is {1:4} and cubed is {2:4} ".format(i,i ** 2, i** 3))

    #------------------------ {position of format :width of spaces} ---------------

    # will print left formatted                                           ---------     0,1,2
for i in range(1,12):
     print(" No {0:2} sqaured is {1:<4} and cubed is {2:<4} ... left formatted ".format(i,i**2,i**3))

print()
#again ---------
print(" Pi is approimately {0:12.50}".format(22/7))
print(" table of 2 ----- ")
for a in range(1,11):
    print(" {0:2} * {1:2} = {2:3} ".format("2",a,2*a))