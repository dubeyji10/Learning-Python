# factorial of a number

number = int(input("enter a number  :  "))
fac =1

for i in range (1,number+1) :
    fac = fac * i


print(" \n{} ! = {}".format(number,fac))
