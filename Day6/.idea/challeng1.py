# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using iter() function.
#
# Use a for loop to loop "n" times , where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function rather than counting the number of items in the list .

list1 = ["hey","hello","hi","bye"]
my_iterator = iter(list1)

for item in range(0,len(list1)):
    print(next(my_iterator))

print("\n-------------\n")
# same -------------- #
# for item in list1:
#     print(item)
