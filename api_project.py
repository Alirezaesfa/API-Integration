import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from .env
api_key = os.getenv("API_KEY")

# Define the URL for the NewsAPI endpoint
url = "https://newsapi.org/v2/top-headlines"

# Define parameters for the request
params = {
    'apiKey': api_key,  # API key from the .env file
    'country': 'us',  # You can change this to the desired country code (e.g., 'us' for the United States)
    'category': 'technology',  # You can change this to 'business', 'sports', etc.
}

# Make the GET request to the NewsAPI endpoint
response = requests.get(url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response JSON
    data = response.json()
    articles = data['articles']
    
    # Print the top 5 news articles
    print("Top 5 News Articles:")
    for i, article in enumerate(articles[:5]):
        print(f"{i + 1}. {article['title']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   Published At: {article['publishedAt']}")
        print(f"   URL: {article['url']}\n")
else:
    print(f"Failed to retrieve news: {response.status_code}")
