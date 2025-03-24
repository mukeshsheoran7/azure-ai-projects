import requests
import json

# Replace with your endpoint and API key

API_KEY = "DRZXgERx7RXMkNaX1z5cVk6vtLX56ioeDFctPQZ9s3kvovYnzk6BJQQJ99BCACYeBjFXJ3w3AAAaACOGSVYD"
ENDPOINT = "https://sentiment-analysis-ai3.cognitiveservices.azure.com/"

# Sample customer reviews
documents = {
    "documents": [
        {"id": "1", "language": "en", "text": "The camera quality of this phone is amazing, but the battery life is disappointing."},
        {"id": "2", "language": "en", "text": "The service was slow, but the food was delicious."},
        {"id": "3", "language": "en", "text": "Great value for money! Highly recommended."}
    ]
}

# Function for sentiment analysis
def analyze_sentiment(documents):
    sentiment_url = f"{ENDPOINT}/text/analytics/v3.1/sentiment"
    headers = {
        "Ocp-Apim-Subscription-Key": API_KEY,
        "Content-Type": "application/json"
    }
    
    response = requests.post(sentiment_url, headers=headers, json=documents)
    sentiments = response.json()
    return sentiments

# Function for key phrase extraction
def extract_key_phrases(documents):
    key_phrase_url = f"{ENDPOINT}/text/analytics/v3.1/keyPhrases"
    headers = {
        "Ocp-Apim-Subscription-Key": API_KEY,
        "Content-Type": "application/json"
    }
    
    response = requests.post(key_phrase_url, headers=headers, json=documents)
    key_phrases = response.json()
    return key_phrases

# Run both functions and display results
sentiment_results = analyze_sentiment(documents)
key_phrase_results = extract_key_phrases(documents)

# Print results
print("\n=== Sentiment Analysis Results ===")
print(json.dumps(sentiment_results, indent=4))

print("\n=== Key Phrase Extraction Results ===")
print(json.dumps(key_phrase_results, indent=4))
