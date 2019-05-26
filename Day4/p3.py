# here we removed spam from
# list it will give an error ------------- when line 9 is in comment

# at line 15 because nasty_food_item was never set to a value


meal = ["egg","bacon","sausages","soup"]

#nasty_food_item = ''
for item1 in meal:
    if item1 == 'spam':
        nasty_food_item = item1
    break

if nasty_food_item:
    print(" Can't have i anything without spam in it ")