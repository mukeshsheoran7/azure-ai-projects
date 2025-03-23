import requests
import json

# Replace with your Azure endpoint and API key
endpoint = "https://sentiment-analysis-ai3.cognitiveservices.azure.com/text/analytics/v3.1/sentiment"
api_key = "DRZXgERx7RXMkNaX1z5cVk6vtLX56ioeDFctPQZ9s3kvovYnzk6BJQQJ99BCACYeBjFXJ3w3AAAaACOGSVYD"

# Review sample
data = {
    "documents": [
        {"id": "1", "language": "en", "text": "I absolutely love this product, but the delivery was terrible."},
        {"id": "2", "language": "en", "text": "The item was broken on arrival. I am very disappointed."},
        {"id": "3", "language": "en", "text": "Great quality and fast delivery. Highly recommended!"}
    ]
}

# Send the request
headers = {
    "Ocp-Apim-Subscription-Key": api_key,
    "Content-Type": "application/json"
}

response = requests.post(endpoint, headers=headers, json=data)

# Print the result
if response.status_code == 200:
    results = response.json()
    for doc in results["documents"]:
        print(f"Review ID: {doc['id']}")
        print(f"Sentiment: {doc['sentiment']}")
        print(f"Confidence Scores: {doc['confidenceScores']}")
        print("-" * 50)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
