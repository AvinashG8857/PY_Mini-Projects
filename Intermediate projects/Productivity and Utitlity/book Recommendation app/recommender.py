import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Create a mini-dataset (In a real app, you'd load a CSV with thousands of books)
data = {
    'title': [
        "The Hobbit", "Harry Potter", "Foundation", 
        "Dune", "The Great Gatsby", "The Martian"
    ],
    'description': [
        "A fantasy adventure with hobbits, dragons, and magic rings.",
        "A young boy discovers he is a wizard in a world of magic.",
        "A galactic empire falls and a scientist tries to save knowledge.",
        "A sci-fi epic about a desert planet and spice wars.",
        "A classic novel about wealth, love, and the American dream.",
        "An astronaut is stranded on Mars and must survive using science."
    ]
}

df = pd.DataFrame(data)

def get_recommendations(target_title):
    # TF-IDF (Term Frequency-Inverse Document Frequency)
    # This turns words into 'importance scores'. 
    # Words like 'the' get low scores, 'magic' or 'space' get high scores.
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['description'])

    # Cosine Similarity: Calculates the angle between book vectors.
    # 1.0 = identical, 0.0 = completely different.
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Find the index of our book in the dataframe
    try:
        idx = df[df['title'] == target_title].index[0]
    except IndexError:
        return ["Book not found!"]

    # Get similarity scores for all books compared to our target
    # enumerate() keeps track of the original index
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort books based on similarity scores (highest first)
    # x[1] refers to the score in the (index, score) tuple
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get top 2 results (excluding the book itself which is always #1)
    recommended_indices = [i[0] for i in sim_scores[1:3]]

    return df['title'].iloc[recommended_indices].tolist()