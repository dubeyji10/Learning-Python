# challenge 1 :
# Modify the program so that the exit is a dictionary rather than a list ,
# with keys being the numbers of the locations and the value being
# dictionaries holding the exits (as they do at present ).
#No change should be needed to the actual code.
#
# Once that is working , create another dictionary that contains words that
#player may use . These words will be the keys,and their values will be
#a single letter that the program can use to determine which way to go .
# ( this is in DS8 )

locations = { 0 : "You are sitting in front of a computer learning Python",
              1 : "You are standing at the end of a road before a small building",
              2 : "You are at the top of a hill",
              3 : "You are inside a building, a well house for a small stream",
              4 : "You are in a valley beside a stream",
              5 : "You are in the forest"
              }
exits = {
  0 :  {"Q" : 0 },
  1 :  {"W": 2,"E": 3,"N" : 5,"S" : 4,"Q" : 0},
  2 :  {"N": 5,"Q": 0},
  3 :  {"W": 1,"Q": 0},
  4 :  {"N": 1,"W": 2,"Q": 0},
  5 :  {"W": 2,"S" :1,"Q": 0} }
vocabulary = { "QUIT" : "Q",
               "NORTH": "N",
               "SOUTH": "S",
               "EAST" : "E",
               "WEST" : "W"}
loc =1
while True:
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are "+availableExits+" : ").upper()
    print()
    #parse the user input,using our vocabulary dictionary if necessary
    if len(direction)>1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break
                #or use this ......................
    #more than one letter enter so check vocabulary
        # for word in vocabulary: #does it contains the word we know
        #     if word in direction:
        #         direction = vocabulary[word]

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print(" You cannot go in "+direction+" direction ")