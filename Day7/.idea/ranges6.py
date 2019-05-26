#more on ranges

# writing ranges with different parameters/argument and predicting outputs


print(range(0,100))
#output -------  range(0, 100)
print("\n")
i = range(1,132)
print(i)
#output ------- range(1, 132)
print("\n")
k=i[::2]
print(k)
#output ------- range(1, 132, 2)
print("\n")
l=k[::4]
print(l)
#output ------- range(1,132,8) ----- the slices is multiplied
print("\n")

print("-"*20)
#here we pick range from 0 to 100
o=range(0,100)
#modify it --- slices of 4 and store it in another variable
# name[starting:end:slice_of]
n=o[::4]
print(n) # it should be range(0, 100, 2)
#now slicing again
print("-"*20)
p = n[::5]
print(p)
print("-"*20)

for i in p:
    print(i)


print("-"*20) #slices multiplied -- after every 20 i is printed ......


#equivalent code is


for g in range(0,100,20):
    print(g)

print("-"*20)
print(" \n printing ranges in reverse --- \n")

print(range(1231,1))
asd=range(1000,940,2)
print(asd)
for i in asd:
    print(asd,end=" ")