import random

print ("||||| Number guess game |||||".upper())
number = random.randint(1,100)

attempts =0
while True:
    try:
        guess= int(input("Guess a number between 1 and 100 : "))
        attempts+=1

        if guess==number:
            print("great guess")
        else :
            print("try again")

    except ValueError:
        print("ENter correct number")