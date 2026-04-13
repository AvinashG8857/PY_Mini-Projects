from recommender import get_recommendations

def run_app():
    print("📚 Welcome to the Book Recommender!")
    print("Available books: The Hobbit, Harry Potter, Foundation, Dune, The Great Gatsby, The Martian")
    
    user_input = input("\nEnter a book you liked: ").strip()
    
    # We call our logic from the other file
    results = get_recommendations(user_input)
    
    print("\n--- Because you liked that, you might enjoy: ---")
    for book in results:
        print(f"⭐ {book}")

if __name__ == "__main__":
    run_app()