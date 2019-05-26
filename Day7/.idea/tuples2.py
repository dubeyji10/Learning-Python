welcome = "Welcome to my Nightmare","Alice Cooper",1975
bad = "Bad Company" "Bad Company",1974
budgie = "Nightflight","Budgie",1981
imelda = "More Mayhem","Emilda May",2011
metallica = "Ride the lightning","Metallica",1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

#and since tuples are immutable

#this will generate an error

#metallica[0] = "Master of puppets"

#updation will done using indexing and slicing
print(imelda)

# in line 4 imelda[1] should be Imelda May
print("------ after correction ------")
#now we do update -------------


imelda = imelda[0],"Imelda May",imelda[2]
print(imelda)

#that still means tuples are immutable because here the variable
# imelda is assigned to a new object of that type

#while lists are mutable

print("-"*40)
print("\n now lists : ")
metallica2 = ["Ride the lightning","Metallica",1984]
print(metallica2)
metallica2[0] = "Master of Puppets"
print(" after changing ")
print(metallica2)
