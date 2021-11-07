import yfinance as yf
from yfinance import Ticker

import news
import stock_list


class Stock:
    def __init__(self, stock_name):
        self.name = stock_name
        self.ticker: Ticker = yf.Ticker(self.name)

    def get_info_data(self):
        stock_info = self.ticker.info
        return stock_info

    def get_history_data(self):
        stock_history_data = self.ticker.info["longBusinessSummary"]
        return stock_history_data

    def get_news_data(self):
        company_name = self.get_company_name()
        news_data = news.get_news(self.name.upper(), company_name)
        return news_data

    def get_price_msg(self):
        data = yf.download(tickers=self.name, period='5m', interval='1m')
        if data.size > 0:
            data = data.reset_index()
            data["format_date"] = data['Datetime'].dt.strftime('%m/%d %I:%M %p')
            data.set_index('format_date', inplace=True)
            print(data.to_string())
            price_msg = data['Close'].to_string(header=False)
        else:
            price_msg = "No data!?"
        return price_msg

    def get_trgt_data(self):
        info_data = self.get_info_data()
        trgt_low = info_data["targetLowPrice"]
        trgt_high = info_data["targetHighPrice"]
        trgt_data = f"""Target Low : {trgt_low}
        Target High : {trgt_high}
        """
        return trgt_data

    def get_day_data(self):
        info_data = self.get_info_data()
        day_low = info_data["dayLow"]
        day_high = info_data["dayHigh"]
        day_data = f"""Day Low : {day_low}
        Day High : {day_high}
        """
        return day_data

    def get_marketcap(self):
        info_data = self.get_info_data()
        marketcap = info_data["marketCap"]
        return marketcap

    def get_company_name(self):
        info_data = self.get_info_data()
        company_name = info_data["longName"]
        return company_name

    @staticmethod
    def get_list():
        st_list_msg = "Some famous Stocks are : \n"
        for stock_name, company_name in stock_list.stock_list.items():
            st_list_msg = st_list_msg + f"{stock_name} - {company_name} \n"
        return st_list_msg
