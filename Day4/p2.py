meal = ["egg","bacon","spam","sausages","soup"]

for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break

if nasty_food_item:
    print(" Can't have i anything without spam in it ")


print(" after removing break \n\n")

for item1 in meal:
    if item1 == 'spam':
        nasty_food_item = item1
      #  break

if nasty_food_item:
    print(" Can't have i anything without spam in it ")