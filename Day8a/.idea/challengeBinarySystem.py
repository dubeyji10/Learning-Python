print(" Printing first decimal numbers(positive) and their equivalent hexadecimal , binary and octal representations : \n")
for i in range(0,17):
    print("{:>2} in hexadecimal is {:02x}    ,      in binary is {:04b}    and in octal is {:02o} ".format(i,i,i,i))
    #or print("{0:>2} in hex is {0:02x} binary is {0:b}".format(i)
   # try {0:o} , {0:02o} , {0:0,04o} - same with b ,x -- see difference in output
print("-"*50)
x = 0x20 #prefix for hex ,,,,,,,,,  20 to decimal ------ 32 --- 2*(16^1) + 0*(16^0) ---
y = 0x0a # --- oa =  10 in decimal
# ------------------------------this { : x (here)} converts the output to hex
print("0x20 = {0} and in hex it is : {0:x}".format(x))
print("0x0a = ",y)

print("-"*50)
print(" convert the input number to binary ")
print("-"*50)

value = int(input(" Enter decimal value : "))
x = value
powersof2 = []

for power in range(15,-1,-1):
    powersof2.append(2 ** power)
for power in powersof2:
    print(value // power,end='')
    value %= power
#
# print(binary)
#or
printing = False
print("\n","-"*20,"removing extra zeroes","-"*20,"\n")
for power in powersof2:
    bit = x // power
    if bit != 0 or power == 1:
        printing = True
    if printing:
        print(bit,end='')
    x %= power
