import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

#data set

data = {
    'text': [
    
        "WINNER! Claim your prize now!",
        "URGENT! Cash bonus awaits you. Click here.",
        "Free entry to win a car. Text STOP.",
        "Congratulations! You won a $1000 gift card.",
  
        "Hi how are you? lets go out for coffee",
        "Are we still meeting for lunch today?",
        "Can you send me that file by 5pm?",
        "Hey, call me when you have a second.",
        "I'm running late, see you in ten minutes.",
        "I love grabbing coffee on Sunday mornings."
    ],
    'label': ['spam', 'spam', 'spam', 'spam', 'not spam', 'not spam', 'not spam', 'not spam', 'not spam', 'not spam']
}

df=pd.DataFrame(data)

df_copied= df.copy()

def clean_text(text):
    text= text.lower()
    text= re.sub(r'[^a-z\s]','',text)
    return text

df["text"]= df['text'].apply(clean_text)

vectorizzer= TfidfVectorizer(stop_words="english")
X= vectorizzer.fit_transform(df['text'])
y= df["label"]

#training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#the model
model= MultinomialNB()
model.fit(X_train,y_train)

prediction = model.predict(X_test)
print(f"Model Accuracy : {accuracy_score(y_test,prediction)*100}%")
print("/nDeatiled Report:/n", classification_report(y_test,prediction))\


def predict_message(msg):
    cleaned= clean_text(msg)
    vec= vectorizzer.transform([cleaned])
    result= model.predict(vec)
    return result[0]

sampleTxt= "Hi how are you? lets go out for coffee"
print(f"\nTesting message: {sampleTxt}")
print(f"Prediction: { predict_message(sampleTxt).upper()}")