# Given the tuple below that represents the Imelda May album "More Mayhem" , write
# code to print the album details , followed by a listing of all the tracks in the album .

# Indent the tracks by a single tab stop when printing them(remember that you can pass
# more than one item to the print function,seperating them with a comma) .

imelda = "More Mayhem","Imelda May",2011,(
    (1,"Pulling the Rug"),(2,"Psycho"),(3,"Mayhem"),(4,"Kentish Town Waltz"))

title,artist,year,tracks = imelda
track1,track2,track3,track4=tracks
print("\n ----------------------Album details---------------------- \n")
# print(" Title : {}      Artist : {}     Year : {}   ".format(title,artist,year))
#
# print(" track1 : {}     track2 : {}     track3 : {}     track4 : {}".format(track1,track2,track3,track4))

print("Album : {}   Artist : {}    Year : {}\ntrack1 : {}\ntrack2 : {}\ntrack3 : {}\ntrack4 : {}"
      .format(title,artist,year,track1,track2,track3,track4))
print("-"*40,"or do this","-"*40)
for songs in tracks :
    track,title = songs
    print("\tTrack Number : {} , Title : {} ".format(track,title))