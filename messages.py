from stock_list import stock_list

start_msg = """
Hi ! I am Stock Bot
I can help you get the following : 
 - Stock News
 - Stock Current Price
 - Stock taget LOW/HIGH price
 - Stock day LOW/HIGH
 - Stock MarketCap
 - Stock history
"""

help_msg = """
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

To get the price at Intervals over a period of 5m
/price stock_name

To get a list of top performing stocks
/list
"""

error_msg = """Command is incorrect !!
  Please do refer /help for command Structuring
  """


def get_stock_list_msg():
    """Converts the stock_list dictionary into strings
    and returns the stock list message as a string"""
    st_list_msg = "Some famous Stocks are : \n"
    for stock_name, company_name in stock_list.items():
        st_list_msg = st_list_msg + f"{stock_name} - {company_name} \n"
    return st_list_msg
