print(" Guess a number b/w 1 and 10 ")
guess = int(input())

#always put code in right indentation


if guess !=5 :
    if guess < 5 :
        print(" guess higer ")
    else :
        print(" guess lower ")
    guess = int(input())
    if guess == 5 :
        print(" well done ")
    else :
        print(" sorry wrong guess ")

else :
    print(" you got it in first time ")