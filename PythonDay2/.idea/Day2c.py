a=12
b=3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b )
#dealing with integers
print()
print()
for i in range(1,a//b): # a/b gives error --  a float value
    print(i)

print()
print()
print(a + b / 3 -4 *12) #   -35.0 ?? -- operator precedence --
print(8 /2 *3) #12
print(8 *3 / 2) #12

print((((a+b)/ 3 ) - 4 ) * 12) # now it gives 3
c = a + b # 15
d = c / 3 # 5
e = d - 4 # 1
print(e*12) # 12

