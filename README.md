# stock-alert-bot

## Usage:
/get
[STOCK_NAME] [COMPANY_NAME]

## Working behind the scenes: 
1. Get the command from Slack bot
2. Get the stock name
3. Get the stock details from the Alphavantage API
4. Get the news from the newsapi
5. Display the stop price with other details (change in value, news)

## API used: 
Stock Price Endpoint : "https://www.alphavantage.co/query"

News API Endpoint : "https://newsapi.org/v2/everything"
