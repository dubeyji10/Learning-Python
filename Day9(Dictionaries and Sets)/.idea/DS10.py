# solution to challenge 1

locations = { 0 : "You are sitting in front of a computer learning Python",
              1 : "You are standing at the end of a road before a small building",
              2 : "You are at the top of a hill",
              3 : "You are inside a building, a well house for a small stream",
              4 : "You are in a valley beside a stream",
              5 : "You are in the forest"
              #key : description
              }
locations1 = { "quit" : "Q",
               "north" : "N",
               "west" : "W",
               "south" : "S",
               "east" : "E"}

#exit list is changed to a dictionary
value0 = {"Q" : 0 }
value1 = {"W": 2,"E": 3,"N" : 5,"S" : 4,"Q" : 0}
value2 = {"N": 5,"Q": 0}
value3 = {"W": 1,"Q": 0}
value4 = {"N": 1,"W": 2,"Q": 0}
value5 = {"W": 2,"S" :1,"Q": 0}

exits = { 0 : value0,
          1 : value1,
          2 : value2,
          3 : value3,
          4 : value4,
          5 : value5
          }

# or simply ------

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
    print()
    # .upper() so even if player enter a lowercase it could still be playable
    # since keys are in uppercase
    #passing user input using new dictionary --- locations1
    if len(direction)>1:
        words = direction.split()
        for word in words:
            if word in locations1:
                direction = locations1[word]
                break
        #other way


    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")
        # if keyword is entered again ....
        # #once entered it is removed from choices



