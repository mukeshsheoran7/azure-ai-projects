from azure_api import analyze_sentiment, extract_key_phrases
from utils import load_reviews, display_results

# Load sample reviews
reviews = load_reviews("sample_reviews.json")

# Run sentiment and key phrase extraction
sentiment_results = analyze_sentiment(reviews)
key_phrase_results = extract_key_phrases(reviews)

# Display results
display_results(sentiment_results, key_phrase_results)