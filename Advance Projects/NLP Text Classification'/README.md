# 📨 NLP Spam Classifier
## Advanced Text Analysis with Scikit-Learn

This project implements an **NLP (Natural Language Processing)** pipeline to automatically detect and classify "Spam" vs "Ham" (legitimate) messages.

---

### 🧠 How the AI "Reads"
This project uses three major advanced concepts to process language:

#### 1. Regex Cleaning (`re` module)
Human text is messy. We use **Regular Expressions** to strip out symbols (£, $, !) and numbers. This ensures the AI focuses on the *meaning* of the words rather than the specific currency or date mentioned.

#### 2. TF-IDF Vectorization
We don't just count words. **TF-IDF** calculates the "uniqueness" of a word. 
- If the word "Free" appears in many spam emails but rarely in normal emails, it gets a **high score**.
- If the word "The" appears everywhere, it gets a **low score**.
- This creates a mathematical "fingerprint" for every message.

#### 3. Naive Bayes Theorem
The model uses **Bayesian Probability**. It asks: *"Given that the word 'WINNER' is in this message, what is the mathematical probability that the message is Spam?"* It multiplies the probabilities of every word in the message together to reach a final verdict.

---

### 🚀 Key Features
* **Stop-Word Filtering**: Automatically ignores common filler words (a, an, the).
* **Probability-Based Logic**: Uses the Multinomial Naive Bayes algorithm.
* **Generalization**: Because it learns patterns rather than exact sentences, it can catch spam messages it has never seen before.