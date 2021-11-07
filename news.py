import os
import requests


def get_news(stock_name, company_name):
    STOCK_NAME = stock_name
    COMPANY_NAME = company_name;
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    first_three_articles = articles[:3]

    formatted_articles = [
        f"{STOCK_NAME}: \nHeadline: {article['title']}. \nBrief: {article['description']} \nURL : {article['url']}" for
        article in first_three_articles]

    return formatted_articles
