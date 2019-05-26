print(range(100))
#what is the output ? ------- range(0,100)
print(range(1,100))
#what is the output ? ------- range(1,100)

# raange(x,y,z) for any value of x,y,z will use same amount of memory but when
# stored in a list obviously list will have different memory size
my_list = list(range(10))
print("\n",my_list,"\n")
# stores range element into my_list which are passed into the constructor list()

#[0,1,2,3,4,5,6,7,8,9] !!!!!!! from 0 to 9


even = list(range(0,100,2)) #skipping every 2nd item from 0
odd = list(range(1,100,2)) #skipping every 2nd item from 1

print(even)
print("--------------- ")
print(odd)


#------------012345678910--------------25
my_string = "abcdefghijklmnopqrstuvwxyz"

print(my_string.index('e')) #4
print(my_string[4]) #e

odd_large = range(1,10000,2)
#odd numbers from 1 to 10000

print(odd)

print("1st odd number : {} \n"
      "2nd odd number : {}\n"
      "985 odd number : {}".format(odd_large[0],odd_large[1],odd_large[985]))
print("\n\n\n-------------------------\n")


sevens = range(7,100000,7)
x = int(input(" Please enter a positive number less than one million"))
if x in sevens:
      print("{} is divisible by seven ".format(x))
else:
      print("{} is not divisible by seven ".format(x))