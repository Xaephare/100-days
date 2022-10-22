import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
TWILIO_SID = 'AC211aff4bdedf4fe4e089961597d463a9'

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv()
PHONE_NUM = os.getenv('PHONE')
STOCK_API_KEY = os.getenv('STOCK_KEY')
NEWS_API_KEY = os.getenv('NEWS_KEY')
TWILIO_KEY = os.getenv('TWILIO_KEY')

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY
}

news_params = {
    'q': COMPANY_NAME,
    'apiKey': NEWS_API_KEY
}

# Stock Information
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = stock_response.json()['Time Series (Daily)']
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
day_before_data = data_list[1]

# Calc percentage difference
abs_difference = abs(float(yesterday_data['4. close']) - float(day_before_data['4. close']))
percentage_diff = abs_difference / float(day_before_data['4. close']) * 100

# News Articles
news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_data = news_response.json()['articles']
top3 = news_data[:3]
formatted_articles = [f"Headline:\n{article['title']}.\nBrief:\n{article['description']}." for article in top3]

# Format and print percentage change
if float(yesterday_data['4. close']) > float(day_before_data['4. close']):
    percentage_format = f"{STOCK_NAME}: 🔺{round(percentage_diff)}%"
else:
    percentage_format = f"{STOCK_NAME}: 🔻{round(percentage_diff)}%"

# Check
print(percentage_format)

# Send SMS
if percentage_diff >= 5:
    for item in formatted_articles:
        client = Client(TWILIO_SID, TWILIO_KEY)
        message = client.messages \
            .create(
            body=f"\n{percentage_format}\n{item}",
            from_='+16614664633',
            to=PHONE_NUM
        )
        print(message.status)
