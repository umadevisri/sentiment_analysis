
import pandas as pd
from textblob import TextBlob

# Load the dataset (optional for expansion)
try:
    data = pd.read_csv("data_sentiment.csv")  # Use if you're processing multiple rows
except FileNotFoundError:
    print("Dataset not found. Continuing with single sentence analysis.")

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # Range from -1 (negative) to 1 (positive)

    if polarity > 0.1:
        return "Positive 😊"
    elif polarity < -0.1:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# Main function to interact with user
def main():
    print("Welcome to the Sentiment Analyzer!")
    while True:
        text = input("\nEnter a sentence (or type 'exit' to quit): ")
        if text.lower() == 'exit':
            print("Goodbye!")
            break
        sentiment = analyze_sentiment(text)
        print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    main()
