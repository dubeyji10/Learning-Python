with open("/home/abhishek/Documents/pythonDUBEY/sampletext.txt","r") as asd:
    line = asd.readline()
    while line:
        print(line,end='')
        line=asd.readline()