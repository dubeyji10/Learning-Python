#now readlines -----not readline


with open("/home/abhishek/Documents/pythonDUBEY/sampletext.txt","r") as asd:
    lines = asd.readlines()
    print(lines)
#no while loop needed
print("\n"+"-"*50)
for line in lines:
    print(line,end=' ')