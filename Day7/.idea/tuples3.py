a=b=c=d=12
print(c)
a,b=12,13 # will be useful ahead ------------
print(a,b)
a,b=b,a
print("a is {}".format(a))
print("b is {}".format(b))

#print("a is {}".format(a))

print("-"*40)

welcome = "Welcome to my Nightmare","Alice Cooper",1975
bad = "Bad Company" "Bad Company",1974
budgie = "Nightflight","Budgie",1981
imelda = "More Mayhem","Imilda May",2011 #corrected already
metallica = "Ride the lightning","Metallica",1984

# now see ------------------
print(" this is called unpacking the tupple ")
title,artist,year = imelda
print(title)
print(artist)
print(year)

#while this doesn't works for list
# this generates error -----------------------------------
metallica2 = ["Ride the lightning","Metallica",1984]
metallica2.append("Rock")
title,artist,year = metallica2 #we added another item to list using
#append so it can't be unpacked --- here error
print(title)
print(artist)
print(year)