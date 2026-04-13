import random

flashcards = {
    "what is the capital of france?":"paris",
    "who developed python?": "Giudo van Rossum",
    "what does ML stands for ?":"Machine Learning",
    "2+2=?":"4"
}

def flashcard():
    print("Welcome to FlashCard game ")
    questions= list(flashcards.keys())
    random.shuffle(questions)

    for question in questions:
        answer= flashcards[question]
        user_input= input(f"{question}\n Your answer: ")
        if user_input.lower() == "q":
            break
        elif user_input.strip().lower() == answer.lower():
            print("correct")
        else:
            print(f" Wrong answer : {answer}\n")

flashcard()