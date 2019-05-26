odd = []
for i in range(1,100):
   # print(i,end="\n")
    if i%2!=0:
        odd.append(i)


print(" list of odd numbers :\n\n ")
print(odd)
for i in range(0,len(odd)):
    print(" {} odd number = {}".format(i+1,odd[i]))