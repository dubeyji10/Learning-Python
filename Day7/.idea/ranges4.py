decimals = range(0,100)
my_range = decimals[3:40:3]
print(my_range == range(3,40,3))

print(range(0,5,2)==range(0,6,2)) #why true ?
 # see below

print("list(range(0,6,2)) is :  ",list(range(0,6,2)))
print("list(range(0,5,2)) is :  ",list(range(0,5,2)))

#slices can also be negative

r = range(0,100)

print(r)

for i in r[::-2]:
    #going back to 1 from 100 with scies of 2
    print(i,end=" ")

#similar to --------
print("\n")
print("--"*20)
print("\n")
for i in range(99,0,-2):
    print(i,end=" ")

print("-"*50)

print("-------------------------------------------------------")
print(range(0,100)[::-2] == range(99,0,-2))

print("-------------------------------------------------------")

for i in range(0,100,-2):
    print(i) #gives nothing ? because -2 is not valid for range 0 to 100