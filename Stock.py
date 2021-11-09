import yfinance as yf
from yfinance import Ticker

import news
import stock_list

PERIOD = '5m'
INTERVAL = '1m'


class Stock:
    def __init__(self, stock_name):
        self.name = stock_name
        self.ticker: Ticker = yf.Ticker(self.name)

    def get_info(self):
        """Gets the info data from the Ticker
        and returns stock info as a dictionary
        """
        stock_info = self.ticker.info
        return stock_info

    def get_history(self):
        """From the Ticker , gets the history data
        and returns the stock history as a String
        """
        stock_history_data = self.ticker.info["longBusinessSummary"]
        return stock_history_data

    def get_news(self):
        """From the Ticker , gets the company name
        Using the company name gets the news using the NEWS API
        returns the news as a String
        """
        company_name = self.get_company_name()
        news_data = news.get_news(self.name.upper(), company_name)
        return news_data

    def get_price_msg(self):
        """Using the Yahoo Finance API, gets the price of the given stock
        for a period of PERIOD and for each interval INTERVAL
        returns the price message as a string
        """
        data = yf.download(tickers=self.name, period=PERIOD, interval=INTERVAL)
        if data.size > 0:
            data = data.reset_index()
            data["format_date"] = data['Datetime'].dt.strftime('%m/%d %I:%M %p')
            data.set_index('format_date', inplace=True)
            print(data.to_string())
            price_msg = data['Close'].to_string(header=False)
        else:
            price_msg = "No data!?"
        return price_msg

    def get_trgt(self):
        """From the stock info dictionary,
        gets the target high, target low
        returns the stock target as a string
        """
        info_data = self.get_info_data()
        trgt_low = info_data["targetLowPrice"]
        trgt_high = info_data["targetHighPrice"]
        trgt_data = f"""Target Low : {trgt_low}
        Target High : {trgt_high}
        """
        return trgt_data

    def get_day(self):
        """From the stock info dictionary,
        gets the day low, day high
        returns the stock day data as string"""
        info_data = self.get_info_data()
        day_low = info_data["dayLow"]
        day_high = info_data["dayHigh"]
        day_data = f"""Day Low : {day_low}
        Day High : {day_high}
        """
        return day_data

    def get_marketcap(self):
        """From the stock info dictionary,
        gets the marketcap of the stock and
        returns the marketcap as string
        """
        info_data = self.get_info_data()
        marketcap = info_data["marketCap"]
        return marketcap

    def get_company_name(self):
        """From the stock info dictionary,
        gets the company name and
        returns the company name as a string
        """
        info_data = self.get_info_data()
        company_name = info_data["longName"]
        return company_name