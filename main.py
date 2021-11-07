import os

import telebot
import messages
from Stock import Stock

API_KEY = os.getenv('TELEGRAM_API_KEY')
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['news'])
def handle_news(message):
    try:
        st_name = message.text.split()[1]
        bot.send_chat_action(message.chat.id, "typing")
        stock = Stock(st_name)
        st_news = stock.get_news_data()
        bot.send_message(message.chat.id, st_news)
    except:
        error_handler(message)


@bot.message_handler(commands=['target'])
def handle_target(message):
    try:
        st_name = message.text.split()[1]
        bot.send_chat_action(message.chat.id, "typing")
        stock = Stock(st_name)
        st_target_data = stock.get_trgt_data()
        bot.send_message(message.chat.id, st_target_data)
    except:
        error_handler(message)


@bot.message_handler(commands=['day'])
def handle_day(message):
    try:
        st_name = message.text.split()[1]
        bot.send_chat_action(message.chat.id, "typing")
        stock = Stock(st_name)
        st_day_data = stock.get_day_data()
        bot.send_message(message.chat.id, st_day_data)
    except:
        error_handler(message)


@bot.message_handler(commands=['marketcap'])
def handle_marketcap(message):
    try:
        st_name = message.text.split()[1]
        bot.send_chat_action(message.chat.id, "typing")
        stock = Stock(st_name)
        st_marketcap = stock.get_marketcap()
        bot.send_message(message.chat.id, st_marketcap)
    except:
        error_handler(message)


@bot.message_handler(commands=['history'])
def handle_history(message):
    try:
        st_name = message.text.split()[1]
        bot.send_chat_action(message.chat.id, "typing")
        stock = Stock(st_name)
        st_history = stock.get_history_data()
        bot.send_message(message.chat.id, st_history)
    except:
        error_handler(message)


@bot.message_handler(commands=['list'])
def list_stocks(message):
    bot.send_chat_action(message.chat.id, "typing")
    st_list = Stock.get_list()
    bot.send_message(message.chat.id, st_list)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, messages.start_msg)


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, messages.help_msg)


def stock_request(message):
    request = message.text.split()
    if len(request) < 2 or request[0].lower() not in "price":
        return False
    else:
        return True


@bot.message_handler(commands=['price'])
def handle_price(message):
    try:
        stock_name = message.text.split()[1]
        stock = Stock(stock_name)
        price_msg = stock.get_price_msg()
        bot.send_message(message.chat.id, price_msg)
    except:
        error_handler(message)


def error_handler(message):
    error_msg = """Command is incorrect !!
  Please do refer /help for command Structuring
  """
    bot.send_message(message.chat.id, error_msg)


print("Bot Started")
bot.polling()
