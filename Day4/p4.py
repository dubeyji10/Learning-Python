# this will not give an error because we have
#intialized the value of
# #nasty_food_item  ...... and no output visible
# because spam is not set to nast_food_item
meal = ["egg","bacon","sausages","soup"]
nasty_food_item = ''

for item1 in meal:
    if item1 == 'spam':
        nasty_food_item = item1
        break

if nasty_food_item:
    print(" Can't have i anything without spam in it ")