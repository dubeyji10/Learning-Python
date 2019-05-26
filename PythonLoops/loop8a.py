# modifying loop8 program to allow us as many guesses as necessary

import random
highest = 10
answer = random.randint(1,highest)

print(" Please guess a number b/w 1 and {} or press {} to exit"
      " : ".format(highest,0))
guess = int(input())

if guess == answer:
    print(" You got it in first time ")

while guess != answer:
    if guess == 0:
        print(" you quit ")
        break
    if guess < answer:
        print(" Please guess higher ")
    else:
        print(" Please guess lower ")
    guess = int(input())
    if guess == answer:
        print(" Well done , you guessed it ")
    else:
        print(" Sorry , you have not guessed correctly  ")
