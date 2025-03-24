import requests
import json

# Azure Language Service Config
ENDPOINT = "https://sentiment-analysis-ai3.cognitiveservices.azure.com"
API_KEY = "DRZXgERx7RXMkNaX1z5cVk6vtLX56ioeDFctPQZ9s3kvovYnzk6BJQQJ99BCACYeBjFXJ3w3AAAaACOGSVYD"
API_URL = f"{ENDPOINT}/text/analytics/v3.1/sentiment"

# File path containing the reviews
file_path = "reviews/reviews1.txt"

# Read the review content
with open(file_path, "r") as file:
    reviews = [file.read()]

# Prepare the request body
documents = [{"id": str(i + 1), "language": "en", "text": review} for i, review in enumerate(reviews)]

headers = {
    "Ocp-Apim-Subscription-Key": API_KEY,
    "Content-Type": "application/json"
}

# Make the API call
response = requests.post(API_URL, headers=headers, json={"documents": documents})
result = response.json()

def display_results (sentiment):
    """Display Sentiment and Key Phrase Extraction results"""
    print("\n=== Sentiment Analysis Result===")
    print(json.dumps(sentiment,indent=4))
  
display_results(result)

# Improved Output Formatting
print("\n--- Sentiment Analysis Results ---\n")
for doc in result['documents']:
    print(f"📄 **Document ID:** {doc['id']}")
    print(f"🛑 Sentiment: {doc['sentiment'].capitalize()}")
    
    confidence = doc['confidenceScores']
    print(f"✔️ Positive: {confidence['positive']:.2%}")
    print(f"⚠️ Neutral: {confidence['neutral']:.2%}")
    print(f"❌ Negative: {confidence['negative']:.2%}")
    
    if 'sentences' in doc:
        print("\n🔍 **Key Sentences:**")
        for sentence in doc['sentences']:
            print(f"- {sentence['text']} (Sentiment: {sentence['sentiment'].capitalize()})")

    print("\n" + "="*50 + "\n")
    
    
