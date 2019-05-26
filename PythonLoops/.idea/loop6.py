available_exits = ["east","north-east","south"]
choosen_exit = ""
while choosen_exit not in available_exits:
    choosen_exit = input(" please choose a direction again ")

print(" aren't you glad you got out of there ")

print("\n\n ( see source ) in case of choosen_2exit it is initialized to east and "
      "it lies in the list of available_exits so loop is skipped")
choosen_2exit = "east"
while choosen_2exit not in available_exits:
    choosen_2exit = input(" please choose a direction again  ")

print(" aren't you glad you got out of there ")
