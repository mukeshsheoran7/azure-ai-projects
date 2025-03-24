import json

def display_results (sentiment, key_phrases):
    """Display Sentiment and Key Phrase Extraction results"""
    print("\n=== Sentiment Analysis Result===")
    print(json.dumps(sentiment,indent=4))

    print("\n=== Key Phrase Extraction Results ===")
    print(json.dumps(key_phrases, indent=4))

def load_reviews(file_path):
    """Load customer reviews from a JSON file"""
    with open(file_path, "r") as file:
        return json.load(file)