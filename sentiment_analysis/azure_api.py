import requests
import json
from config import API_KEY, ENDPOINT

def analyze_sentiment(documents):
    """ Function to call Azure Sentiment Analysis"""
    sentiment_url = f"{ENDPOINT}/text/analytics/v3.1/sentiment"
    headers = {
        "Ocp-Apim-Subscription-Key": API_KEY,
        "Content-Type": "application/json"
    }
    response = requests.post(sentiment_url,headers=headers, json=documents)
    return response.json()

def extract_key_phrases(documents):
    """Function to call Azure Key Phrase Extraction"""
    key_phrase_url = f"{ENDPOINT}/text/analytics/v3.1/keyPhrases"
    headers = {
        "Ocp-Apim-Subscription-Key": API_KEY,
        "Content-Type": "application/json"
    }
    response = requests.post(key_phrase_url, headers=headers, json=documents)
    return response.json()