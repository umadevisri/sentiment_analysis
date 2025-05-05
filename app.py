import streamlit as st
import pandas as pd
from textblob import TextBlob

st.set_page_config(page_title="Sentiment Analyzer", layout="centered")

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        return "Positive 😊"
    elif polarity < -0.1:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# App title and description
st.title("🧠 Sentiment Analyzer")
st.write("This app analyzes the sentiment of your text using TextBlob.")

# Text input
user_input = st.text_area("Enter your sentence here:")

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        sentiment = analyze_sentiment(user_input)
        st.success(f"**Sentiment:** {sentiment}")


