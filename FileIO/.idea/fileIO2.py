#another way to read files
with open("/home/abhishek/Documents/pythonDUBEY/sampletext.txt","r") as asd:
    for line in asd:
        if "JAB" in line.upper():
            print(line,end='') #here variable is asd


# the benefit here is that with statement handles errors
