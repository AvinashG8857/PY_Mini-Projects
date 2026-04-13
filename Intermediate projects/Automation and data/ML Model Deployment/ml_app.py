import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'YearsExperience': [1.1, 2.0, 3.2, 4.0, 5.1, 6.0, 7.1, 8.2, 9.0, 10.5],
    'Salary': [39343, 46205, 54445, 63525, 66029, 81363, 93940, 101302, 113812, 121872]
}

df = pd.DataFrame(data)

X = df[["YearsExperience"]]
y = df["Salary"]

model = LinearRegression()
model.fit(X, y)

st.title("AI Salary Predictor")
st.write("This app uses a machine learning model to predict salary based on experience.")

st.sidebar.header("User Input")
experience = st.sidebar.slider("Years of Experience", 0.0, 20.0, 5.0)

input_df = pd.DataFrame({"YearsExperience": [experience]})
prediction = model.predict(input_df)[0]

st.subheader(f"Predicted Salary for {experience} years:")
st.header(f"${prediction:,.2f}")

st.write("### Training Data Trend")
st.line_chart(df, x="YearsExperience", y="Salary")