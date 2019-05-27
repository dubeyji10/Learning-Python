#now readlines -----not readline


with open("/home/abhishek/Documents/pythonDUBEY/sampletext.txt","r") as asd:
    lines = asd.readlines()
    print(lines)
#no while loop needed
print("\n"+"-"*50)
for line in lines[::-1]: #reverse slices ----- first line printed at the end
    print(line,end=' ')

#now readlines -----not readline


with open("/home/abhishek/Documents/pythonDUBEY/sampletext.txt","r") as asd:
    lines = asd.read()
    print(lines)

print("\n---------------------------------- reverse every word ---------------------------------- \n")


for line in lines[::-1]:
    print(line,end='')