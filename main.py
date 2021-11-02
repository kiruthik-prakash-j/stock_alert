import os
import yfinance as yf
from yfinance import Ticker
import telebot
import messages

API_KEY = os.getenv('TELEGRAM_API_KEY')
bot = telebot.TeleBot(API_KEY, parse_mode=None)


def get_stock_ticker(stock_name):
    return yf.Ticker(stock_name)


def get_stock_info_data(stock_name):
    stock_ticker: Ticker = get_stock_ticker(stock_name)
    stock_info = stock_ticker.info
    return stock_info


def get_stock_history_data(stock_name, st_period):
    stock_ticker: Ticker = get_stock_ticker(stock_name)
    stock_history_data = stock_ticker.history(period=st_period)
    return stock_history_data


def get_stock_news_data(stock_name):
    stock_ticker: Ticker = get_stock_ticker(stock_name)
    stock_news_data = stock_ticker.news
    return stock_news_data


def get_stock_price_data(stock_name, st_period, st_interval):
    print(stock_name, st_period, st_interval)
    stock_price_data = yf.download(
        tickers=stock_name,
        period=st_period,
        interval=st_interval,
    )
    return stock_price_data


def get_st_trgt_data(stock_name):
    stock_info_data = get_stock_info_data(stock_name)
    st_trgt_low = stock_info_data["targetLowPrice"]
    st_trgt_high = stock_info_data["targetHighPrice"]
    st_trgt_data = f"""Target Low : {st_trgt_low}
    Target High : {st_trgt_high}
    """
    return st_trgt_data


def get_st_day_data(stock_name):
    stock_info_data = get_stock_info_data(stock_name)
    st_day_low = stock_info_data["dayLow"]
    st_day_high = stock_info_data["dayHigh"]
    st_day_data = f"""Day Low : {st_day_low}
    Day High : {st_day_high}
    """
    return st_day_data


def get_st_marketcap(stock_name):
    stock_info_data = get_stock_info_data(stock_name)
    st_marketcap = stock_info_data["marketCap"]
    return st_marketcap


@bot.message_handler(commands=['news'])
def handle_news(message):
    st_name = message.text.split()[1]
    st_news = get_stock_news_data(stock_name=st_name)
    bot.send_message(message.chat.id, st_news)


@bot.message_handler(commands=['target'])
def handle_target(message):
    st_name = message.text.split()[1]
    st_target_data = get_st_trgt_data(stock_name=st_name)
    print(st_target_data)
    bot.send_message(message.chat.id, st_target_data)


@bot.message_handler(commands=['day'])
def handle_day(message):
    st_name = message.text.split()[1]
    st_day_data = get_st_day_data(stock_name=st_name)
    bot.send_message(message.chat.id, st_day_data)


@bot.message_handler(commands=['marketcap'])
def handle_marketcap(message):
    st_name = message.text.split()[1]
    st_marketcap = get_st_marketcap(stock_name=st_name)
    bot.send_message(message.chat.id, st_marketcap)


@bot.message_handler(commads=['history'])
def handle_history(message):
    st_name = message.text.split()[1]
    st_prd = message.text.split()[2]
    st_history = get_stock_history_data(stock_name=st_name, st_period=st_prd)
    bot.send_message(message.chat.id, st_history)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, messages.start_msg)


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, messages.help_msg)


@bot.message_handler(commands=['wsb'])
def get_stocks(message):
    response = ""
    stocks = ['gme', 'amc', 'nok']
    stock_data = []
    for stock in stocks:
        data = yf.download(tickers=stock, period='2d', interval='1d')
        data = data.reset_index()
        response += f"-----{stock}-----\n"
        stock_data.append([stock])
        columns = ['stock']
        for index, row in data.iterrows():
            stock_position = len(stock_data) - 1
            price = round(row['Close'], 2)
            format_date = row['Date'].strftime('%m/%d')
            response += f"{format_date}: {price}\n"
            stock_data[stock_position].append(price)
            columns.append(format_date)
        print()

    response = f"{columns[0] : <10}{columns[1] : ^10}{columns[2] : >10}\n"
    for row in stock_data:
        response += f"{row[0] : <10}{row[1] : ^10}{row[2] : >10}\n"
    response += "\nStock Data"
    print(response)
    bot.send_message(message.chat.id, response)


def stock_request(message):
    request = message.text.split()
    if len(request) < 2 or request[0].lower() not in "price":
        return False
    else:
        return True


@bot.message_handler(commands=['price'])
def handle_price(message):
    request = message.text.split()[1]
    data = yf.download(tickers=request, period='5m', interval='1m')
    if data.size > 0:
        data = data.reset_index()
        data["format_date"] = data['Datetime'].dt.strftime('%m/%d %I:%M %p')
        data.set_index('format_date', inplace=True)
        print(data.to_string())
        bot.send_message(message.chat.id, data['Close'].to_string(header=False))
    else:
        bot.send_message(message.chat.id, "No data!?")


print("Bot Started")
bot.polling()
