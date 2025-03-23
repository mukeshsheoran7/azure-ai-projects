# azure-ai-projects
# Azure Sentiment Analysis with Python

## Description
This project uses Azure Cognitive Services and Python to perform sentiment analysis on text data.

## Technologies Used
- Python
- Azure Cognitive Services (Language Service)
- VS Code

## ⚙️ How to Run
1. Clone the repo: `git clone <YOUR_GITHUB_REPO_URL>`
2. Install dependencies: `pip install requests`
3. Run the script: `python sentiment_analysis.py`

## Sample Output
{ "documents": [ { "id": "1", "sentiment": "positive", "confidenceScores": { "positive": 0.98, "neutral": 0.01, "negative": 0.01 } } ] }

## 📊 Sample Data
You can test the sentiment analysis using the following sample data:
```json
{
  "documents": [
    { "id": "1", "text": "I love this product! It's amazing." },
    { "id": "2", "text": "The service was terrible. I'm disappointed." },
    { "id": "3", "text": "It was an average experience, nothing special." }
  ]
}

```

## Author
Mukesh Sheoran

