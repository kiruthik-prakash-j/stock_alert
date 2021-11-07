# STOCK-ALERT-BOT

## FUNCTIONS:
It can help you get the following : 
 - Stock News
 - Stock Current Price
 - Stock taget LOW/HIGH price
 - Stock day LOW/HIGH
 - Stock MarketCap
 - Stock history


## SETUP:

### Cloning the Repo

```
 git clone https://github.com/kiruthik-prakash-j/stock_alert.git
```

### Creating the Bot

- Create a bot using BOTFATHER
- Save the BOTAPI in a notepad

### Getting the NEWS API

- Go to https://newsapi.org/
- Select GET API Key
- Sve the NEWS_API_KEY in a notepad

### Setting up the environment variables

- Open Commandline : 
```
 export TELEGRAM_API_KEY=<YOUR-TELEGRAM-API-KEY>
 export NEWS_API_KEY=<YOUR-NEWS-API-KEY>
```

In case of Windows, open Powershell :
```
 set TELEGRAM_API_KEY=<YOUR-TELEGRAM-API-KEY>
 set NEWS_API_KEY=<YOUR-NEWS-API-KEY>
```

### Installing the packages

```
pip install -r requirements.txt
```

### Run
```
python main.py
```

## USAGE
To get the Stock News : 

/news stock_name

To get the target HIGH/LOW price

/target stock_name

To get the day HIGH/LOW

/day stock_name

To get the MarketCap

/marketcap stock_name

To get stock history

/history stock_name

To get the price for the last 5 mins

/price stock_name

To get a list of top performing stocks

/list

