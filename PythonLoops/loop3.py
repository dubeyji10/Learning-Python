for i in range(1,11):
    for j in range(1,11):
         print(" {:4} times {:2} is {:2} ".format(j,i,i*j),end=' ')
    print("---------------------")
# see the difference in format
print("\n\n")
for i in range(1,11):
    for j in range(1,11):
        print(" {:4} times {:2} is {:2} ".format(i,j,i*j),end=' ')
    print("---------------------") # lookout for indent level
