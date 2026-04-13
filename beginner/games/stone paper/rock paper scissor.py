import random


choices= [item.lower() for item in ["stone","paper","scissor"]]

while True:
    user_choice = input("Enter Stone , Paper or scissor (q for quit):  ")

    if user_choice=="q".lower():
        print("Thanks for playing! Goodbye")
        break

    if user_choice not in choices:
        print("Invalid choice! please try' again")

    computer_choice = random.choice(choices)

    if user_choice==computer_choice:
        print("Draw!!")
    elif(user_choice== "stone" and computer_choice=="scissor") or \
        (user_choice== "scissor" and computer_choice=="paper") or \
        (user_choice== "paper" and computer_choice=="stone"):
        print("You win !!")
    else:
        print("Computer Wins!!")

