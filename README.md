
# NewsAPI Integration

This is a Python project that integrates with the [NewsAPI](https://newsapi.org/) to fetch the latest top news articles. It uses the API to pull headlines from a specific country and category, printing the top 5 articles with their details.

## Features
- Fetches top headlines from NewsAPI.
- Filters news based on country and category.
- Displays the top 5 news articles with titles, sources, and publication dates.

## Prerequisites

- Python 3.x
- A NewsAPI account (you can get your free API key [here](https://newsapi.org/)).

## Getting Started

Follow these steps to get the project up and running on your local machine.

## Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/Alirezaesfa/API-Integration.git
cd API-Integration

### Install Dependencies
Use the following command to install the required Python dependencies from requirements.txt:

```bash
pip install -r requirements.txt

### Set Up Your API Key
Go to NewsAPI and sign up for an account.
After signing up, you'll get an API key.
Create a .env file in the root directory of the project and add the following line:

```ini
API_KEY=your_newsapi_api_key_here

Replace your_newsapi_api_key_here with the actual API key you received from NewsAPI.

### Run the Script
Run the Python script to fetch the top 5 news articles:

```bash
python api_project.py

The script will print the top 5 news articles from the US, under the "technology" category. You can change the country and category parameters in the script to get news for other regions or categories.
