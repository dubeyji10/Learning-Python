name = input(" what's your name ")
letter = input(" enter a character ")
if letter in name :
    print(" {0} is present in {1} ".format(letter,name))
else :
    print(" {0} is not present in {1} ".format(letter,name))
