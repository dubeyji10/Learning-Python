available_exits = ["east","north-east","south"]
choosen_exit = ""
while choosen_exit not in available_exits:
    choosen_exit = input(" please choose a direction again ")
    if choosen_exit == "quit":
        print(" Game over ")
        break

else :
    print(" aren't you glad you got out of there ")
