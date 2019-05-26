#using split function


locations = { 0 : "You are sitting in front of a computer learning Python",
              1 : "You are standing at the end of a road before a small building",
              2 : "You are at the top of a hill",
              3 : "You are inside a building, a well house for a small stream",
              4 : "You are in a valley beside a stream",
              5 : "You are in the forest"
              #key : description
              }
print("locations[0] : ",locations[0])
print("\n","<>"*40)
print("locations[0].split() : ",locations[0].split())
print("<>"*40,"\n")
print(locations[3])
print("<>"*40,"\n")
print(locations[3].split(" , "))
#split is the opposite of join

print("<>"*40,"\n")

print(' '.join(locations[0].split()))
#gives location[0] split cancel's join
 #gives the original string