# this will not give an error because we have
#intialized the value of
# #nasty_food_item  ...... and no output visible
# because spam is not set to nast_food_item


# else satements will be printed
meal = ["egg","bacon","sausages","soup"] #spam is not in the list
nasty_food_item = ''

for item1 in meal:
    if item1 == 'spam':
        nasty_food_item = item1
        break
else : # out of loop
        print(" I'll have a plate of that ")

if nasty_food_item:
    print(" Can't have i anything without spam in it ")