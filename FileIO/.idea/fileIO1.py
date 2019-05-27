#/home/abhishek/Documents/pythonDUBEY
  #path of files ------------------------------- sampletext
jabber = open("/home/abhishek/Documents/pythonDUBEY/sampletext.txt",'r')
                                                            #in read only
for line in jabber:
    print(line)

#undo comment and se output ----and comment the other code
#and see output of fileIO3 ----- it removes double spaces in output
#see difference in how lines are printed

print("-"*50)

#
# for line in jabber:
#     if "jabberwock" in line.lower():#string is lowercase or uppercase ----
#         print(line,end='') #only returning the lines
#         # that have got the word jabberwock in them

jabber.close() #not this
