print(" please guess a number b/w 1 and 10 ")
guess = int(input())
if guess < 5 :
     print(" please guess higher ")
     guess = int(input())
if guess < 5:
    print(" guess higher ")
    guess=int(input())
    if guess == 5:
        print(" well done ")
    else:
        print(" sorry wrong guess ")
elif guess > 5 :
    print(" please guess lower ")
    guess = int(input())
    if guess == 5 :
        print(" well done ")
    else :
        print(" sorry wrong guess ")
else :
    print(" YOU got it in first time")
