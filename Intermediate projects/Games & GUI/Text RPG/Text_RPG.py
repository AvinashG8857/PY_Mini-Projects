import random

def intro():
    print("Welcome to the Text RPG!")
    print("You are a hero on a quest to defeat the dragon.")
    print("Your journey begins in a dark forest...\n")

def battle(enemy):
    player_health = 100
    enemy_health = 50
    while player_health > 0 and enemy_health > 0:
        print(f"\nYour Health: {player_health} | {enemy} Health: {enemy_health}")
        action = input("Do you want to (A)ttack or (R)un? ").lower()
        if action == "a":
            damage = random.randint(10, 20)
            enemy_health -= damage
            print(f"You hit the {enemy} for {damage} damage!")
        elif action == "r":
            print("You ran away!")
            return False
        else:
            print("Invalid choice!")

        if enemy_health > 0:
            enemy_damage = random.randint(5, 15)
            player_health -= enemy_damage
            print(f"The {enemy} hits you for {enemy_damage} damage!")

    if player_health <= 0:
        print("You have been defeated...")
        return False
    else:
        print(f"You defeated the {enemy}!")
        return True

def game():
    intro()
    choice = input("Do you want to go to the (C)ave or (V)illage? ").lower()
    if choice == "c":
        print("You enter the cave and encounter a goblin!")
        battle("Goblin")
    elif choice == "v":
        print("You arrive at the village and rest at the inn.")
    else:
        print("You wander aimlessly and get lost...")

game()