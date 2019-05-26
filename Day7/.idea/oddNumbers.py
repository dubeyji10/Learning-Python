odd = []
for i in range(1,10000):
    # print(i,end="\n")
    if i%2!=0:
        odd.append(i)


print(" list of odd numbers :\n\n ")
#print(odd)
for i in range(0,len(odd)):
    print(" {} odd number = {:4}".format(i+1,odd[i]))


print("\n\n",odd[985])    #for reference odd index of 985 gives -- 1971
# 984+1 ------ is 1969
# and 986th( 985+1) odd number is 1971