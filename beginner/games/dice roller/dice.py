import random
def dice_roller():
    while True:
        user_input= input("Roll The Dice? (y /n)").lower()

        if  user_input=="y":
            result= random.randint(1,6)
            print(f" you rolled {result}")
        elif user_input=="n":
            print("Game Over. Good bye ")
            break
        else:
            print("Invalid Input! Please type y or n")

dice_roller()
