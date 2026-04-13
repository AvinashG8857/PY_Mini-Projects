import random


def hangman():
    words=[ item.lower() for item in  ["python","hangman","dice","game","developer"]]
    word= random.choice(words)
    guessed=["_"]*len(word)
    attempt= 6
    used_letter=set()

    print("Welcome to Hnagman")
    print("word","".join(guessed))

    while attempt>0 and "_" in guessed:
        guess= input("Guess a Letter : ").lower()

        if len(guess)!= 1 or not guess.isalpha():
            print("Please Enter a single alphabet")
            continue
        if guess in used_letter:
            print("You already guessed that letter.")
            continue
        used_letter.add(guess)

        if guess in word:
            for i ,letter in enumerate(word):
                if letter== guess:
                    guessed[i] = guess
            print("Good guess ! Word :", "".join(guessed))
        else:
            attempt-=1
            print(f"Wrong guess ! attempt left {attempt}")

    if "_" not in guessed:
         print("Congratulations, you won! 🎉")
    else:
        print(f"Game over! The word was '{word}'.")

hangman()