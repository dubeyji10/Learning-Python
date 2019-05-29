with open("imelda3.txt","r") as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents) #eval is not a good way to deal with data external
# to program
print(imelda)
title,artist,year,tracks = imelda
print(title)
print(artist)
print(year)