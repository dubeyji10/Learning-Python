#refer to screenshot taken at 11:38 on 25th may

locations = { 0 : "You are sitting in front of a computer learning Python",
              1 : "You are standing at the end of a road before a small building",
              2 : "You are at the top of a hill",
              3 : "You are inside a building, a well house for a small stream",
              4 : "You are in a valley beside a stream",
              5 : "You are in the forest"
           #key : description
}
#now a list
exits = [
    {"Q" : 0 },
    {"W": 2,"E": 3,"N" : 5,"S" : 4,"Q" : 0},
    {"N": 5,"Q": 0},
    {"W": 1,"Q": 0},
    {"N": 1,"W": 2,"Q": 0},
    {"W": 2,"S" :1,"Q": 0}
]
# we start with element 1 - road
#then to 2-hill
#then to 5-forest
#then to 1 ----
#---here ---
# Q = 0 refer to tupple -------you are siting in .... python
# S = 4 (tupple )  ---- you are in a valley beside a stream
# a loop to allow player to keep playing until he enters quit

#initially
#Q to ext
loc =1
while True:
    availableExits = ""
    #nothing now

    # for direction in exits[loc].keys():
    #     availableExits +=direction+", "
    #aliter
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break
    #until location 0.............


    direction = input(" Available exits are "+availableExits+" ").upper()
    # .upper() so even if player enter a lowercase it could still be playable
    # since keys are in uppercase
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")
        # if keyword is entered again ....
        # #once entered it is removed from choices

