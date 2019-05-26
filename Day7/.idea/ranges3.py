decimals = range(0,100)
print(decimals)
#----------     start:end:slices_of
my_range = decimals[3:40:3]

print(my_range)

for i in my_range:
    print(i)

print("-"*30)

for i in range(3,40,4):
    print(i)

print("\n",my_range == range(3,40,3))