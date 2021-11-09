import os

import telebot
import messages
from Stock import Stock

API_KEY = os.getenv('TELEGRAM_API_KEY')
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['news'])
def handle_news(message):
    """Handles the /news command
    Gets the stock name from the message and
    prints the news to the bot
    """
    try:
        st_name = message.text.split()[1]
        bot.send_chat_action(message.chat.id, "typing")
        stock = Stock(st_name)
        st_news = stock.get_news()
        bot.send_message(message.chat.id, st_news)
    except:
        error_handler(message)


@bot.message_handler(commands=['target'])
def handle_target(message):
    """Handles the /target command
    Gets the stock name from the message and
    prints the stock target to the bot
    """
    try:
        st_name = message.text.split()[1]
        bot.send_chat_action(message.chat.id, "typing")
        stock = Stock(st_name)
        st_target_data = stock.get_trgt()
        bot.send_message(message.chat.id, st_target_data)
    except:
        error_handler(message)


@bot.message_handler(commands=['day'])
def handle_day(message):
    """Handles the /day command
    Gets the stock name from the message and
    prints the stock day data to the bot
    """
    try:
        st_name = message.text.split()[1]
        bot.send_chat_action(message.chat.id, "typing")
        stock = Stock(st_name)
        st_day_data = stock.get_day()
        bot.send_message(message.chat.id, st_day_data)
    except:
        error_handler(message)


@bot.message_handler(commands=['marketcap'])
def handle_marketcap(message):
    """Handles the /marketcap command
    Gets the stock name from the message and
    prints the stocks' marketcap to the bot
    """
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
    """Handles the /history command
    Gets the stock name from the message and
    prints the stock's history to the bot
    """
    try:
        st_name = message.text.split()[1]
        bot.send_chat_action(message.chat.id, "typing")
        stock = Stock(st_name)
        st_history = stock.get_history()
        bot.send_message(message.chat.id, st_history)
    except:
        error_handler(message)


@bot.message_handler(commands=['list'])
def list_stocks(message):
    """Handles the /list command
    Gets the stock list message from messages.py and
    prints the list of good performing stocks to the bot
    """
    bot.send_chat_action(message.chat.id, "typing")
    st_list = messages.get_stock_list_msg()
    bot.send_message(message.chat.id, st_list)


@bot.message_handler(commands=['start'])
def handle_start(message):
    """Handles the /start command
    Gets the start message from messages.py and
    prints the start message to the bot
    """
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, messages.start_msg)


@bot.message_handler(commands=['help'])
def handle_help(message):
    """Handles the /help command
    Gets the help message from messages.py and
    prints the help message to the bot
    """
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, messages.help_msg)


def stock_request(message):
    """Helper function to find if the given command is structured correctly
    Returns a Boolean value
    """
    request = message.text.split()
    if len(request) < 2 or request[0].lower() not in "price":
        return False
    else:
        return True


@bot.message_handler(commands=['price'])
def handle_price(message):
    """Handles the /price command
    Gets the stock name from the message and
    prints the stock price
    """
    try:
        stock_name = message.text.split()[1]
        stock = Stock(stock_name)
        price_msg = stock.get_price_msg()
        bot.send_message(message.chat.id, price_msg)
    except:
        error_handler(message)


def error_handler(message):
    bot.send_chat_action(message.chat.id, "typing")
    bot.send_message(message.chat.id, messages.error_msg)


print("Bot Started")
bot.polling()
